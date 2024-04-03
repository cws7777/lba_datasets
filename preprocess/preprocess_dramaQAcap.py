import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--capfile",  help="Required original caption file of DramaQA", type=str, default="../originals/DramaCap_test.json")
parser.add_argument("--qafile",  help="Required original QA file of DramaQA", type=str, default="../originals/AnotherMissOhQA_test_set.json")
parser.add_argument("--tuplefile",  help="Required txt file of DramaCaption tuples", type=str, default="../processed/tuples/DramaCap_test_shotscene_tuple.txt")
parser.add_argument("--output", help="Processed file output file path", type=str, default="../processed/AnotherMissOh_integrated_test_real.json.rows")

args = parser.parse_args()
#out_file = open(args.output, 'w')

#open_file = open(args.jsonrows, 'r')
#txt_file = open(args.tupletxt, 'r')

cap_file = args.capfile
qa_file = args.qafile
tuple_file = args.tuplefile
output_file = args.output

sent_list = []
shot_key = []
with open(cap_file, 'r') as f:
    data = json.load(f)

    for i, key in enumerate(data):
        if "0000" in key:
            continue
        caption = data[key]
        shot_key.append(key)
        sent_list.append(caption)
#print(len(shot_key)) #2189
#print(len(sent_list)) #2189

qa_que = []
qa_vid = []
with open(qa_file, 'r') as q:
    qa_data = json.load(q)
    leng = len(qa_data)

    for i in range(leng):
        if qa_data[i]["videoType"] == "shot":
            qa = qa_data[i]["que"]
            vid = qa_data[i]["vid"]

            qa_que.append(qa)
            qa_vid.append(vid)

            #ans_num = qa_data[i]["correct_idx"]
            #ans = qa_data[i]["answers"][ans_num]
tuple_list = []

with open(tuple_file, 'r') as t:
    for i in range(len(sent_list)):
        line = t.readline()
        tuples = line.strip('\n')
        tuple_list.append(tuples)

#print(len(tuple_list))  #2189
#idx = shot_key.index("AnotherMissOh18_002_0035")
#print(idx)
#cappppp = sent_list[idx]
#tupleeee = tuple_list[idx]
#print(cappppp)
#print(tupleeee)
#exit(0)

integrated_dict = {}
with open(output_file, 'w') as outfile:
    for vid_id, qa in zip(qa_vid, qa_que):
        for shot_id, cap, tupless in zip(shot_key, sent_list, tuple_list):
            if shot_id == vid_id:
                integrated_dict["shot_id"] = shot_id
                integrated_dict["sent"] = cap
                integrated_dict["qa"] = qa
                integrated_dict["tuples"] = tupless 
                outfile.write(json.dumps(integrated_dict))
                outfile.write('\n')
            else:
                continue
    """
    for shot, cap in zip(shot_key, amrbart_list):
        amrbart_dict["shot_id"] = shot
        amrbart_dict["sent"] = cap
        amrbart_dict["qa"] = qa
        #amrbart_dict["answer"] = ans
        outfile.write(json.dumps(amrbart_dict))
        outfile.write('\n')
    """
