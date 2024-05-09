import json

def merge_emotions(train_data, emotion_data):
    # Load character emotion data
    with open(emotion_data, 'r') as f:
        character_emotions = json.load(f)
    
    # Load train data
    with open(train_data, 'r') as f:
        train_json = json.load(f)
    
    # Iterate through train data episodes
    for episode in train_json:
        # Iterate through scene level graph of each episode
        for scene_key, scene_data in episode.items():
            if "AnotherMissOh" in scene_key:
                #print(scene_key[:19])
                #exit(0)
                for character, emotions in scene_data["scene_level_graph"].items():
                    #print(character)
                    #print(emotions)
                    #exit(0)
                    # Check if the character exists in character_emotions
                    if character in character_emotions:
                        print(character_emotions[""])
                        # If emotions key exists in character data
                        if "emotions" in emotions:
                            # Add emotions from character_emotions to the existing emotions
                            emotions["emotions"].update(character_emotions[character])
                        else:
                            # If emotions key doesn't exist, add it and add emotions from character_emotions
                            emotions["emotions"] = character_emotions[character]

            else:
                continue
    # Write the modified train data back to file
    with open(train_data, 'w') as f:
        json.dump(train_json, f, indent=4)

# Usage example
merge_emotions("AnotherMissOh_train.json", "character_emotion.json")

