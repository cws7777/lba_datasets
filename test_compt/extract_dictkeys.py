import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--capjson",  help="Required json file of DramaQA", type=str, default="../originals/DramaCap_test.json")
parser.add_argument("--output", help="Processed file output file path", type=str, default="./test_shot_keys.txt")

args = parser.parse_args()
out_file = open(args.output, 'w')

with open(args.capjson) as f:
    data = json.load(f)
    data_list = list(data)
    #print(data_list[0])
    #print(data_list[1])
    #exit(0)
    #leng = len(data)
    out_list = []
    for i in range(len(data_list)):
        if "0000" in data_list[i]:
            #if data_list[i] == "AnotherMissOh12_047_0000":
            #    next_key = 0
            out_file.write(data_list[i])
            out_file.write('\n')

            next_key = data_list[i+1]
            if data_list[i] == "AnotherMissOh16_001_0000":
                prev_key = str(0) 
            else:
                prev_key = data_list[i-1]
            #print(prev_key)
            #summary = "[" + prev_key + ", " + next_key + "]"
            #out_file.write(summary)
            #out_file.write('\n')
            out_list.append(prev_key)
            out_list.append(next_key)
        else:
            pass
    print(out_list[0])
    out_list.pop(0)
    print(out_list[0])
    #out_list.append("AnotherMissOh12_047_1201") #train
    #out_list.append("AnotherMissOh15_039_1203") #val
    out_list.append("AnotherMissOh18_047_1326")
    n_indices = 2
    for j in range(0, len(out_list), n_indices):
        #summary = "related_shot" + ": " + "[" + out_list[i:i+n_indices] + "]"
        st = out_list[j]
        ed = out_list[j+1]
        out_file.write(st + ", " + ed)
        out_file.write('\n')

print("Done")
