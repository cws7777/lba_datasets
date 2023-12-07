import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--capfile",  help="Required original caption file of DramaQA", type=str, default="../originals/DramaCap_test.json")
parser.add_argument("--tuplefile",  help="Required txt file of DramaCaption tuples", type=str, default="../processed/DramaCap_test_shotscene_wo_sent.txt")


def load_amr_graph_sent(fpath):
    entries = {'amrs':[]}
    with open(fpath) as f:
        data = f.read()
    for entry in data.split('\n'):
        #sent     = None
        gstrings = []
        for line in entry.splitlines():
            #line = line.strip()
            #if line.startswith('# ::snt'):
            #    sent = line[len('# ::snt'):].strip()
            if line.startswith('shot_id:'):
                gstrings.append( line )
        if gstrings:
            #entries['sent'].append(sent)
            entries['amrs'].append(' '.join(gstrings))
    return entries['amrs']
