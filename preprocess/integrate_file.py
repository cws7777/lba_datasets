import json
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("--jsonrows",  help="Required json.rows file of DramaCaption", type=str, default="../DramaCap_train_shot.json.rows")
#parser.add_argument("--tupletxt",  help="Required txt file of DramaCaption tuples", type=str, default="../processed/DramaCap_train_shotscene_wo_sent.txt")
#parser.add_argument("--output", help="Processed file output file path", type=str, default="./DramaCap_test_ep118_test.txt")

parser.add_argument("--jsonrows",  help="Required json.rows file of DramaCaption", type=str, default="../processed/subqa_test.json.rows")
parser.add_argument("--jsonfile",  help="Required json file of DramaQA", type=str, default="../originals/AnotherMissOhQA_test_set.json")
parser.add_argument("--output",  help="Required json file of DramaQA", type=str, default="../originals/AnotherMissOhQA_subQA_test_set.json")


args = parser.parse_args()
out_file = open(args.output, 'w')

jsonrows_file = open(args.jsonrows, 'r')
json_file = open(args.jsonfile, 'r')
qa_data = json.load(json_file)
leng = len(qa_data)
#print(leng)
#serials = {'img_id': [], 'sentence': [], 'tuples': []}
#print('Loading and integrating', fpath)
#count = 0
'''
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
'''
count = 0
count_json = 0
count_s = 0
json_list = []
for file_json in jsonrows_file:
    data = json.loads(file_json)
    json_list.append(data)
leng_data = len(json_list)
total_li = []
for i in range(leng):
    if qa_data[i]['videoType'] == "shot":
        vid = qa_data[i]['vid']
        count = count+1
        new_dict = {}
        for j in range(leng_data):
            sub_li = []
            shot_id = json_list[j]['shot_id']
            sub_q = json_list[j]['subq']
            sub_a = json_list[j]['suba']
            sub_li.append(sub_q)
            sub_li.append(sub_a)

            if shot_id == vid:
                count_s = count_s + 1
                new_dict = qa_data[i]
                new_dict['sub_qas'] = sub_li
                total_li.append(new_dict)
out_file.write(json.dumps(total_li, indent=4))

'''
        for file_json in jsonrows_file:
            count_json = count_json + 1
            subqa_li = []
            data = json.loads(file_json)
            print(data)
            exit(0)
            img_id = data["shot_id"]
            sub_q = data["subq"]
            sub_a = data["suba"]
            #new_dict = {}
            subqa_li.append(sub_q)
            subqa_li.append(sub_a)

            if qa_data[i]["vid"] == data["shot_id"]:
                count_s = count_s + 1
                new_dict = qa_data[i]
                new_dict['sub_qas'] = subqa_li
                json_object = json.dumps(new_dict, indent=4)
                out_file.write(json_object)
print(count)
print(count_json)
print(count_s)
'''
