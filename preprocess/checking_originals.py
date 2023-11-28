import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--qajson",  help="Required json file of DramaQA", type=str, default="../originals/AnotherMissOh_train_set.json")
parser.add_argument("--output", help="Processed file output file path", type=str, default="../processed/DramaQA_train_set.txt")

args = parser.parse_args()
out_file = open(args.output, 'w')

with open(args.qajson) as f:
    data = json.load(f)
    leng = len(data)
    for i in range(leng):
        shot_level = data[i]["videoType"]
        summary = ""
        if shot_level == "shot":
            vid_id = data[i]["vid"]
            q_level = data[i]["q_level_logic"]
            summary = shot_level + vid_id + str(q_level)
            out_file.write(summary)
            out_file.write('\n')
        else:
            pass
