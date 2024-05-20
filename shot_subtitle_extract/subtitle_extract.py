import json

def extract_subtitles(input_file, output_file):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Initialize a list to store extracted data
    extracted_data = []
    
    # Iterate through each item in the input data
    for item in data:
        vid = item["vid"]
        subtitle = item["subtitle"]
        
        # Check if the vid ends with "0000" or subtitle is empty or not properly formed
        if vid.endswith("0000") or subtitle == "." or not subtitle.get("contained_subs"):
            continue
        
        # Add item to extracted_data if it has valid subtitles
        extracted_data.append(item)
    
    # Write the extracted data to the output file
    with open(output_file, 'w') as f:
        json.dump(extracted_data, f, indent=4)

# Usage example
extract_subtitles("../originals/DramaCap_test_script.json", "./extracted_test_vid.json")

