import json

file_path = '../DramaCap_train.json'
output_file = './DramaCap_train_scene.json.rows'
amrbart_list = []
shot_key = []
with open(file_path, 'r') as f:
    data = json.load(f)

    for i, key in enumerate(data):
        if "0000" not in key:
            continue
        caption = data[key]
        shot_key.append(key)
        amrbart_list.append(caption)

amrbart_dict = {}
with open(output_file, 'w') as outfile:
    for shot, cap in zip(shot_key, amrbart_list):
        amrbart_dict["scene_id"] = shot
        amrbart_dict["sent"] = cap
        outfile.write(json.dumps(amrbart_dict))
        outfile.write('\n')
