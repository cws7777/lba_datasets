import json

def extract_example_format(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    result = []
    
    for item in data:
        vid = item["vid"]
        if vid.endswith("_0000"):
            scene_id = vid
            question = item["que"]
            correct_answer = item["answers"][item["correct_idx"]]
            result.append({"scene_id": scene_id, "Question": question, "Answer": correct_answer})
    
    result.sort(key=lambda x: x["scene_id"])
    
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

# Usage example
extract_example_format("../originals/AnotherMissOhQA_test_with_gt.json", "./AnotherMissOhSceneQA_test.json")

