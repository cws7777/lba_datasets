import json
import re

# JSON 파일 읽기
with open('AnotherMissOhQA_train_set_edited.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 각 항목에 대해 처리
for item in data:
    # answers 리스트의 각 항목 처리
    for i, answer in enumerate(item['answers']):
        # "related_shot:" 이후의 내용 제거 및 점으로 대체
        item['answers'][i] = re.sub(r'related_shot:.*', '.', answer)

    # answers 리스트의 길이가 1인 경우 5로 늘리기
    if len(item['answers']) == 1:
        item['answers'].extend(["null"] * 4)
    
    # answers 리스트의 길이가 5보다 작은 경우 5로 늘리기
    while len(item['answers']) < 5:
        item['answers'].append("null")

# 수정된 데이터를 새 JSON 파일로 저장
with open('updated_AnotherMissOhQA_train_set_edited.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("처리가 완료되었습니다. 'updated_AnotherMissOhQA_train_set_edited_sample.json' 파일을 확인해주세요.")
