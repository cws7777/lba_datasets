import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--episode",  help="Required json.rows file of episode", type=str, default="./AnotherMissOh_integrated_val_episode.json.rows")
parser.add_argument("--scene",  help="Required json.rows file of scene", type=str, default="./AnotherMissOh_integrated_val_scene.json.rows")
parser.add_argument("--shot",  help="Required json.rows file of shot", type=str, default="./AnotherMissOh_integrated_val_shot.json.rows")
parser.add_argument("--output",  help="Required json file of DramaQA", type=str, default="./AnotherMissOh_val_onlyscene_wo_kg.json")

args = parser.parse_args()
out_file = open(args.output, 'w')
episode = open(args.episode, 'r')
scene = open(args.scene, 'r')
shot = open(args.shot, 'r')

valid_dict = {}

epi_list = []
for episode_json in episode:
    epidata = json.loads(episode_json)
    #print(epidata)
    epi_list.append(epidata)

sce_list = []
for scene_json in scene:
    scedata = json.loads(scene_json)
    #print(scedata)
    sce_list.append(scedata)

sho_list = []
for shot_json in shot:
    shodata = json.loads(shot_json)
    #print(shodata)
    sho_list.append(shodata)

whole_dict = {}

for i in range(len(epi_list)):
    episode_dict = {}
    epi_info = epi_list[i]
    epi_numb = epi_info["episode"]
    epi_sum = epi_info["summary"]
    epi_kg = epi_info["knowledge_graph"]
    epi_related = epi_info["related_scene"]

    episode_dict["episode"] = epi_numb
    episode_dict["episode_sum"] = epi_sum
    episode_dict["episode_kg"] = epi_kg
    episode_dict["related_scene"] = epi_related
    episode_dict["epi_qas"] = {}

    for j in range(len(sce_list)):
        sce_info = sce_list[j]
        #print(sce_info)
        sce_id = sce_info["scene_id"]
        sce_des = sce_info["scene_description"]
        #sce_kg = sce_info["knowledge_graph"]
        sce_related = sce_info["related_shot"]
        #print(sce_related)
        epinumber = epi_numb[:15]
        #print(epinumber)
        #print(sce_id)
        #print(sce_id[16:19])
        #exit(0)
        if epinumber in sce_id:
            #partial_numb = "scene_" + sce_id[16:19] # ex) 003
            partial_numb = sce_id
            episode_dict[partial_numb] = {}
            episode_dict[partial_numb]["scene_description"] = sce_des
            #episode_dict[partial_numb]["scene_graph"] = sce_kg
            #episode_dict[partial_numb]["related_shot"] = sce_related
            #episode_dict[partial_numb]["scene_qas"] = {}
            scenumber = sce_id[:19]
            #print(scenumber)
            #exit(0)

            """
            for k in range(len(sho_list)):
                sho_info = sho_list[k]
                sho_id = sho_info["shot_id"]
                sho_desc = sho_info["shot_description"]
                sho_graph = sho_info["scene_graph"]

                if scenumber in sho_id:
                    #shoid_numb = "shot_" + sho_id[20:24]
                    shoid_numb = sho_id
                    if shoid_numb in episode_dict[partial_numb]:
                        episode_dict[partial_numb][shoid_numb]["shot_desc"].append(sho_desc)
                        episode_dict[partial_numb][shoid_numb]["shot_graph"].append(sho_graph)
                    else:
                        episode_dict[partial_numb][shoid_numb] = {}
                        episode_dict[partial_numb][shoid_numb]["shot_desc"] = []
                        episode_dict[partial_numb][shoid_numb]["shot_graph"] = []
                        episode_dict[partial_numb][shoid_numb]["shot_desc"].append(sho_desc)
                        episode_dict[partial_numb][shoid_numb]["shot_graph"].append(sho_graph)
                else:
                    continue
            """
        else:
            continue
    out_file.write(json.dumps(episode_dict, indent=4))
        #else:
            #continue

            #episode_dict[]
