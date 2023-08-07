import json
import argparse
from transformers import pipeline

summarizer = pipeline("summarization", model="linydub/bart-large-samsum")

parser = argparse.ArgumentParser()
parser.add_argument("--capjson",  help="Required json file of DramaCaption", type=str, default="./DramaCap_test_script.json")
parser.add_argument("--output", help="Processed file output file path", type=str, default="./DramaCap_test_ep118_test.txt")

args = parser.parse_args()
scene_episode = ['01', '02', '03', '05', '07', '08', '09', '11', '15', '17', '22', '23', '24', '26', '27', '30', '31', '33', '34', '35', '36', '37', '39', '41']       #Episode 1
orig_desc = ""
out_file = open(args.output, 'w')

with open(args.capjson, 'r') as f:
    caption_dict = json.load(f)
    # train: ep2 53, ep3 64, ep4 59, ep5 29, ep6 43, ep7 52, ep8 47, ep9 34, ep10 47, ep11 26, ep12 46
    # val: ep13 44, ep14 36, ep15 39, ep17 57, ep18 47
    # test: ep16 36
    for i in range(47):
        #i = str(i)
        if i < 10:
            i = '0' + str(i)
        else:
            i = str(i)
        vid = "AnotherMissOh18_0" + i + "_0000"          #For Episode 1 first..!
        #input_text = ""
        for j in range(len(caption_dict)):
            #print(caption_dict[j]['vid'])
            #exit(0)
            input_text = ""
            half_text = ""
            o_half_text = ""
            if caption_dict[j]['vid'] == vid:
                out_file.write(vid + '\n')
                #out_file.write('\'\'\'')
                orig_desc = caption_dict[j]['desc']
                subtitle = caption_dict[j]['subtitle']
                if subtitle == '.':
                    continue
                sub_list = subtitle['contained_subs']
                half_len_sub = int(len(sub_list) / 2)
                #print(len(sub_list))
                #print(half_len_sub)
                #print(half_len_sub)
                #print(type(half_len_sub))
                #exit(0)
                if half_len_sub >= 19:
                    half_sub_list = sub_list[:half_len_sub]
                    other_half = sub_list[half_len_sub:]
                    for k in range(len(half_sub_list)):
                        speaks = half_sub_list[k]['speaker']
                        utter = half_sub_list[k]['utter']
                        utter = utter.strip()
                        speaking = speaks + ": " + utter + '\n'
                        half_text += speaking
                    for l in range(len(other_half)):
                        o_speaks = other_half[l]['speaker']
                        o_utter = other_half[l]['utter']
                        o_utter = o_utter.strip()
                        o_speaking = o_speaks + ": " + o_utter + '\n'
                        o_half_text += o_speaking
                    summarize_half = summarizer(half_text)
                    summarize_other = summarizer(o_half_text)
                    summarize_h = summarize_half[0]['summary_text']
                    summarize_o = summarize_other[0]['summary_text']
                    out_file.write(summarize_h + summarize_o + "\n\n")
                else:
                    for m in range(len(sub_list)):
                        speaks = sub_list[m]['speaker']
                        utter = sub_list[m]['utter']
                        utter = utter.strip()
                        speaking = speaks + ": " + utter + '\n'
                        input_text += speaking
                        #out_file.write(speaking)
                    #print(input_text)
                    #exit(0)
                    summarize_tmp = summarizer(input_text)
                    summary = summarize_tmp[0]['summary_text']
                    #out_file.write('\'\'\'\n\n')
                    out_file.write(summary + "\n\n")
            else:
                continue
    out_file.close()
