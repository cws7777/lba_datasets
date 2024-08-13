import json

# 두 JSON 파일 읽기
with open('AnotherMissOhQA_val_set_epis.json', 'r', encoding='utf-8') as f:
    epis_data = json.load(f)

with open('../originals/AnotherMissOhQA_val_set.json', 'r', encoding='utf-8') as f:
    sample_data = json.load(f)

# sample_data에서 vid를 키로, shot_contained를 값으로 하는 딕셔너리 생성
shot_map = {item['vid']: item['shot_contained'] for item in sample_data}

# epis_data 수정
for item in epis_data:
    if 'scene_contained' in item:
        item['shot_contained'] = shot_map.get(item['vid'], item['scene_contained'])
        del item['scene_contained']

# 수정된 데이터를 새 JSON 파일로 저장
with open('AnotherMissOhQA_val_set_epis_modified.json', 'w', encoding='utf-8') as f:
    json.dump(epis_data, f, ensure_ascii=False, indent=4)

print("처리가 완료되었습니다. 'AnotherMissOhQA_val_set_epis_modified.json' 파일을 확인해주세요.")
