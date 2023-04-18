import json

file_path = './DramaCap_test.json'
output_file = './DramaCap_test_amrbart.jsonl'
amrbart_list = []
with open(file_path, 'r') as f:
    data = json.load(f)

    for i, key in enumerate(data):
        caption = data[key]
        amrbart_list.append(caption)

amrbart_dict = {}
with open(output_file, 'w') as outfile:
    for cap in amrbart_list:
        amrbart_dict["sent"] = cap
        amrbart_dict["amr"] = ""
        json.dump(amrbart_dict, outfile)
        outfile.write('\n')
