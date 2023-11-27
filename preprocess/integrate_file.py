import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--jsonrows",  help="Required json.rows file of DramaCaption", type=str, default="../DramaCap_train_shot.json.rows")
parser.add_argument("--tupletxt",  help="Required txt file of DramaCaption tuples", type=str, default="../processed/DramaCap_train_shotscene_wo_sent.txt")
parser.add_argument("--output", help="Processed file output file path", type=str, default="./DramaCap_test_ep118_test.txt")

args = parser.parse_args()
out_file = open(args.output, 'w')

open_file = open(args.jsonrows, 'r')
txt_file = open(args.tupletxt, 'r')

#serials = {'img_id': [], 'sentence': [], 'tuples': []}
#print('Loading and integrating', fpath)
count = 0

for file_json in open_file:
    data = json.loads(file_json)
    img_id = data['shot_id']
    sentence = data['sent']
    line = txt_file.readline()
    tuples = line.strip('\n')
    serials = {'img_id': img_id, 'sentence': sentence, 'tuples': tuples}

    out_file.write(json.dumps(serials))
    out_file.write('\n')
out_file.close()
print("Done integrating")

