import json

def integrate_vids_with_scenes(epsc_file, scene_file, output_file):
    # Load the episode data
    with open(epsc_file, 'r') as f:
        epsc_data = json.load(f)
    
    # Load the scene data
    with open(scene_file, 'r') as f:
        scene_data = [json.loads(line) for line in f]

    # Create a dictionary to map scene_id to vids
    scene_vids_dict = {scene["scene_id"]: scene["vids"] for scene in scene_data}
    
    # Iterate through each episode in epsc_data
    for episode in epsc_data:
        # Iterate through each scene in scene_level
        for scene in episode["scene_level"]:
            scene_id_key = list(scene.keys())[0]
            # Check if the scene_id matches any key in scene_vids_dict
            if scene_id_key in scene_vids_dict:
                # Add the vids to the scene
                scene[scene_id_key]["vids"] = scene_vids_dict[scene_id_key]
    
    # Write the updated episode data to the output file
    with open(output_file, 'w') as f:
        json.dump(epsc_data, f, indent=4)

# Usage example
integrate_vids_with_scenes("AnotherMissOhQA_train_epsc.json", "integrated_vid_with_scene_train.json.rows", "integrated_epsc_with_vids_train.json")

