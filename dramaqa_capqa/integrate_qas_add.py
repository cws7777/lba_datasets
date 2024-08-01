import json

# Paths to the input and output files
txt_file_path = './additional_qas/AnotherMissOh11_sceneaddQA_20240522.txt'
json_file_path = '../originals/AnotherMissOhQA_train_set.json'
output_file_path = './AnotherMissOhQA11_updated.json'

# Function to parse the text file and extract vid, questions, answers, and question types
def parse_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')
    
    data = {}
    current_vid = None
    qa_pairs = []

    for line in lines:
        if line.startswith("AnotherMissOh11"):
            if current_vid and qa_pairs:
                data[current_vid] = qa_pairs
                qa_pairs = []
            current_vid = line.strip()
            print(current_vid)
        elif line.startswith('Q'):
            parts = line.strip().split(':')
            #print(parts)
            question = parts[1]
            que_type = parts[0].split(': ')[-1]
            qa_pairs.append({'question': question, 'que_type': que_type})
        elif line.startswith('A'):
            answer = line.strip().split(': ')[-1]
            qa_pairs[-1]['answer'] = answer
    
    if current_vid and qa_pairs:
        data[current_vid] = qa_pairs
    
    return data

# Function to map video IDs to shot_contained values from the JSON data
def map_vid_to_shot_contained(json_data):
    vid_to_shot = {}
    for entry in json_data:
        vid_to_shot[entry['vid']] = entry['shot_contained']
    return vid_to_shot

# Create new JSON data based on parsed text data and shot_contained mapping
def create_new_json_data(txt_data, shot_mapping):
    new_json_data = []
    for vid, qa_list in txt_data.items():
        for qa in qa_list:
            new_entry = {
                'videoType': 'scene',
                'answer': qa['answer'],
                'question': qa['question'],
                'que_type': qa['que_type'],
                'vid': vid,
                'shot_contained': shot_mapping.get(vid, [])
            }
            new_json_data.append(new_entry)
    return new_json_data

# Read and parse the text file
txt_data = parse_txt_file(txt_file_path)

# Read and parse the JSON file
with open(json_file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Map video IDs to shot_contained values
shot_mapping = map_vid_to_shot_contained(json_data)

# Create new JSON data
new_json_data = create_new_json_data(txt_data, shot_mapping)

# Save the new JSON data to a file
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(new_json_data, file, ensure_ascii=False, indent=4)

print(f"Updated JSON data has been saved to {output_file_path}")

