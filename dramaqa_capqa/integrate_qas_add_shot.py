import json

# Load JSON data
with open('../originals/AnotherMissOhQA_train_set.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Load text data
with open('./additional_qas_shot/shotsAnotherMissOh06_shotaddQA_20240618.txt', 'r', encoding='utf-8') as text_file:
    text_data = text_file.readlines()

# Process text file data
processed_data = []
current_vid = None
current_shot_contained = None

for line in text_data:
    line = line.strip()

    if not line:  # skip empty lines
        continue

    # Detect if this line starts a new video block
    if line.startswith('AnotherMissOh'):
        current_vid = line
        # Find the corresponding shot_contained in the JSON data
        current_shot_contained = next((item['shot_contained'] for item in json_data if item['vid'] == current_vid), None)

    # Process questions and answers
    elif line.startswith('Q'):
        # Extract question and question type
        question_parts = line.split(':')
        #print(question_parts)
        #exit(0)
        que_type = question_parts[0].split(',', 1)[1].strip()
        #print(que_type)
        #exit(0)
        que = question_parts[1].strip()
    
    elif line.startswith('A'):
        # Extract answer
        answer = line.split(':', 1)[1].strip()

        # Create the dictionary entry
        entry = {
            "videoType": "shot",
            "vid": current_vid,
            "que": que,
            "que_type": que_type,
            "answers": [answer],
            "shot_contained": current_shot_contained
        }
        processed_data.append(entry)

# If you want to save the processed data to a new JSON file
with open('./AnotherMissOh06_updated_shot.json', 'w', encoding='utf-8') as output_file:
    json.dump(processed_data, output_file, ensure_ascii=False, indent=4)

print("Processing complete. The processed data has been saved to 'processed_data.json'.")

