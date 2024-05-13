import json

def integrate_qa_with_scene_level_data(qa_file, scene_recon_file, output_file):
    # Load the QA JSON file
    with open(qa_file, 'r') as f:
        qa_data = json.load(f)
    
    # Load the scene reconstruction JSON file
    with open(scene_recon_file, 'r') as f:
        scene_recon_data = json.load(f)
    
    # Initialize a list to store integrated data
    integrated_data = []
    
    # Iterate through each QA item
#    for qa_item in qa_data:
#        scene_id = qa_item["scene_id"]
#        question = qa_item["Question"]
#        answer = qa_item["Answer"]
        
        # Search for the scene_id in scene_recon_data
    for episode_data in scene_recon_data:
        # Check if episode_data contains the "scene-level" key
        if "scene-level" in episode_data:
            scene_level_data = episode_data["scene-level"]
            # Search for scene_id in scene_level_data
            for scene_data in scene_level_data:
                #print(scene_data)
                for k, v in scene_data.items():
                    for qa_item in qa_data:
                        scene_id = qa_item["scene_id"]
                        question = qa_item["Question"]
                        answer = qa_item["Answer"]
                        if scene_id == k:
                            # If scene_id matches, add the QA item to "qas"
                            scene_data[scene_id].setdefault("scene_qas", []).append({"Question": question, "Answer": answer})
                        else:
                            continue
        
        # Append the modified episode_data to integrated_data
        integrated_data.append(episode_data)
    
    # Write the integrated data to the output file
    with open(output_file, 'w') as f:
        json.dump(integrated_data, f, indent=4)

# Usage example
integrate_qa_with_scene_level_data("../sceneQ_collect/AnotherMissOhSceneQA_test.json", "AnotherMissOh_test_scene_recon.json", "AnotherMissOhQA_test_epsc.json")

