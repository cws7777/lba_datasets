import json

def integrate_vid_with_scene(input_vid_file, input_scene_file, output_file):
    # Load the input vid JSON file
    with open(input_vid_file, 'r') as f:
        vid_data = json.load(f)
    
    # Load the input scene JSON rows file
    with open(input_scene_file, 'r') as f:
        scene_data = [json.loads(line) for line in f]

    # Create a dictionary to map scene_id to scene objects
    scene_dict = {scene["scene_id"]: scene for scene in scene_data}
    
    # Iterate through each vid item
    for vid_item in vid_data:
        vid = vid_item["vid"]
        vid_suffix = int(vid[-4:])
        vid_prefix = vid[:19]
        
        # Search for the scene_id in scene_data
        for scene in scene_data:
            scene_id = scene["scene_id"]
            related_shot = scene["related_shot"]
            
            # Check if the vid prefix matches the scene_id prefix and if the vid_suffix is in the related_shot range
            if vid_prefix == scene_id[:19] and related_shot[0] <= vid_suffix <= related_shot[1]:
                # Add the vid to the scene's list of vids
                if "vids" not in scene:
                    scene["vids"] = []
                scene["vids"].append(vid)
                break
    
    # Write the modified scene data to the output file
    with open(output_file, 'w') as f:
        for scene in scene_data:
            f.write(json.dumps(scene) + '\n')

# Usage example
integrate_vid_with_scene("extracted_test_vid.json", "AnotherMissOh_integrated_test_scene.json.rows", "integrated_vid_with_scene_test.json.rows")

