import json

def integrate_scene_level(data_file, output_file):
    # Load the JSON data
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    # Initialize a list to store the integrated data
    integrated_data = []
    
    # Iterate through each item in the data
    for item in data:
        integrated_item = {
            "episode": item["episode"],
            "episode_summary": item["episode_sum"],
            "episode_knowledge": item["episode_kg"],
            "related_scene": item["related_scene"],
            "episode_qas": item["episode_qas"],
            "episode_addqas": item["episode_addqas"],
            "scene-level": []
        }
        # Iterate through keys of the item
        for key, value in item.items():
            if key.startswith("AnotherMissOh") and key.endswith("_0000"):
                integrated_item["scene-level"].append({key: value})
        integrated_data.append(integrated_item)

    # Write the modified data to the output file
    with open(output_file, 'w') as f:
        json.dump(integrated_data, f, indent=4)

# Usage example
integrated_data = integrate_scene_level("AnotherMissOh_test_integrated_emotion.json", "AnotherMissOh_test_scene_recon.json")

# Print or save integrated data
#print(json.dumps(integrated_data, indent=4))

