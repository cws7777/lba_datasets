import json

# JSON 파일 읽기
with open('./AnotherMissOhQA_train_set_scshnew.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 각 항목에 대해 correct_idx 확인 및 추가
for item in data:
    if 'correct_idx' not in item:
        item['correct_idx'] = 0

# 수정된 데이터를 새 JSON 파일로 저장
with open('updated_AnotherMissOhQA_train_set_scshnew.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("처리가 완료되었습니다. 'updated_AnotherMissOhQA_train_set_scshnew_sample.json' 파일을 확인해주세요.")
