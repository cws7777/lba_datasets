import json

file_path = '../originals/DramaCap_train.json'
qa_file = '../originals/AnotherMissOhQA_train_set.json'
output_file = './AnotherMissOh_integrated_train.json.rows'
sent_list = []
shot_key = []
with open(file_path, 'r') as f:
    data = json.load(f)

    for i, key in enumerate(data):
        if "0000" in key:
            continue
        caption = data[key]
        shot_key.append(key)
        sent_list.append(caption)

qa_que = []
qa_vid = []
with open(qa_file, 'r') as f:
    qa_data = json.load(f)
    leng = len(qa_data)

    for i in range(leng):
        if qa_data[i]["videoType"] == "shot":
            qa = qa_data[i]["que"]
            vid = qa_data[i]["vid"]

            qa_que.append(qa)
            qa_vid.append(vid)

            #ans_num = qa_data[i]["correct_idx"]
            #ans = qa_data[i]["answers"][ans_num]

integrated_dict = {}
with open(output_file, 'w') as outfile:
    for vid_id, qa in zip(qa_vid, qa_que):
        for shot_id, cap in zip(shot_key, sent_list):
            if shot_id == vid_id:
                integrated_dict["shot_id"] = shot_id
                integrated_dict["sent"] = cap
                integrated_dict["qa"] = qa
                outfile.write(json.dumps(integrated_dict))
                outfile.write('\n')
    """
    for shot, cap in zip(shot_key, amrbart_list):
        amrbart_dict["shot_id"] = shot
        amrbart_dict["sent"] = cap
        amrbart_dict["qa"] = qa
        #amrbart_dict["answer"] = ans
        outfile.write(json.dumps(amrbart_dict))
        outfile.write('\n')
    """
