import json

# character_emotion.json 파일 로드
with open("character_emotion.json", "r", encoding="utf-8") as f:
    character_emotions = json.load(f)

# AnotherMissOh_train.json 파일 로드
with open("AnotherMissOh_test.json", "r", encoding="utf-8") as f:
    train_data = json.load(f)

# character_emotion.json의 정보를 train_data에 추가
for episode_data in train_data:
    for scene_key, scene_data in episode_data.items():
        #if scene_key == "episode" or scene_key == "episode_sum" or scene_key == "episode_kg" or scene_key == "episode_addqas" or scene_key == "episode_qas" or scene_key == "related_scene":
        #    continue
        #print(scene_key)
        #exit(0)
        if "AnotherMissOh" in scene_key:
            #print("HERE")
            scene_numb = scene_key[:19]
            #print(scene_numb)
            #exit(0)
            for shot_key, shot_data in character_emotions.items():
                #print(shot_key)
                #exit(0)
                if scene_numb in shot_key:
                    if bool(shot_data) == False:
                        #print(shot_data)
                        #exit(0)
                        continue
                    else:
                        for character, emotions in shot_data.items():
                            #print(character)
                            #print(emotions)
                            if character in scene_data["scene_level_graph"]:
                                #print(scene_data["scene_level_graph"][character])
                                if shot_key not in scene_data["scene_level_graph"][character]["emotions"].keys():
                                    #print(shot_key)
                                    print(scene_data["scene_level_graph"][character]["emotions"])
                                    #print(shot_key)
                                    #exit(0)
                                    existing_emotions = scene_data["scene_level_graph"][character]["emotions"]
                                    scene_data["scene_level_graph"][character]["emotions"] = {**existing_emotions, shot_key: emotions}
                                    scene_data["scene_level_graph"][character]["emotions"] = dict(sorted(scene_data["scene_level_graph"][character]["emotions"].items()))
                                else:
                                    continue
                            else:
                                continue
                else:
                    continue
                                #scene_data["scene_level_graph"][character] = {"emotions": {}}
                            #scene_data["scene_level_graph"][character]["emotions"].update(emotions)
        else:
            continue

# 수정된 train_data를 파일로 저장
with open("AnotherMissOh_test_modified.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

