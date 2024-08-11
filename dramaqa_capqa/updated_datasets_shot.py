import json
import os

# Load JSON data from files
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Save JSON data to a file
def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Function to process and merge data
def merge_data(updated_file, test_set_file):
    updated_data = load_json(updated_file)
    test_set_data = load_json(test_set_file)

    for updated_entry in updated_data:
        vid = updated_entry['vid']
        
        # Find the entry in the test set with the same vid
        test_entry = next((item for item in test_set_data if item['vid'] == vid), None)
        
        if test_entry:
            #print("yes")
            # Modify the keys and merge
            #test_entry['answers'] = [updated_entry['answer']]
            #test_entry['que'] = updated_entry['question']
            #test_entry['que_type'] = updated_entry['que_type']
            #test_entry['shot_contained'] = updated_entry['shot_contained']
        #else:
            # Add the new entry with modified keys
            new_entry = {
                'vid': vid,
                'answers': updated_entry['answers'],
                'que': updated_entry['que'],
                'que_type': updated_entry['que_type'],
                'shot_contained': updated_entry['shot_contained']
            }
            test_set_data.append(new_entry)
    
    return test_set_data

# Processing all files (16, 17, 18)
for i in range(1, 13):
    updated_filename = f"./shot_updated/AnotherMissOh{i}_updated_shot.json"
    test_set_filename = "./AnotherMissOhQA_train_set_scnew.json"
    new_filename = "./AnotherMissOhQA_train_set_scshnew.json"

    if i > 1:
        merged_data = merge_data(updated_filename, new_filename)
        save_json(merged_data, new_filename)
    else:
        # Merge data
        merged_data = merge_data(updated_filename, test_set_filename)
        # Save the updated test set
        save_json(merged_data, new_filename)

print("Data merging complete!")

