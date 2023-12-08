import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--subqafile",  help="Required original caption file of DramaQA", type=str, default="../processed/AnotherMissOh_integrated_val.txt")
parser.add_argument("--output",  help="Required jsonrows file for output file", type=str, default="../processed/subqa_val.json.rows")

args = parser.parse_args()

output_file = args.output
subqa_file = args.subqafile
outfile = open(output_file, 'w')

#def load_amr_graph_sent(fpath):
    #entries = {'amrs':[]}
with open(subqa_file) as f:
    data = f.read()
total_list = []
for entry in data.split('\n\n'):
        #sent     = None
        #vid__list = []
    integ_dict = {}
    que_list = []
    ans_list = []
    vid = ""
    for line in entry.splitlines():
            #line = line.strip()
        #print(line)
        #exit(0)
            #if line.startswith('# ::snt'):
            #    sent = line[len('# ::snt'):].strip()
        if line.startswith('shot_id:'):
            vid = line[line.find(':')+2:]
            vid = vid.replace(",","")

        if line.startswith('Q'):
            que_list.append(line[line.find(':')+2:])
        if line.startswith('1.'):
            que_list.append(line[line.find('.')+2:])
        if line.startswith('2.'):
            que_list.append(line[line.find('.')+2:])

        if line.startswith('A'):
            ans_list.append(line[line.find(':')+2:])

    #print(vid)
    #print(que_list)
    #print(ans_list)

    integ_dict["shot_id"] = vid
    integ_dict["subq"] = que_list
    integ_dict["suba"] = ans_list
    outfile.write(json.dumps(integ_dict))
    outfile.write('\n')
