import json
import random

# JSON 파일 읽기
with open('epqas_val.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 새로운 형식의 데이터를 저장할 리스트
new_data = []

for item in data:
    new_item = {}
    
    # Question과 Answer 키 변경
    new_item['que'] = item['Question']
    
    # answers 리스트 생성 및 랜덤 위치에 원래 답변 삽입
    new_item['answers'] = ['null'] * 5
    correct_index = random.randint(0, 4)
    new_item['answers'][correct_index] = item['Answer']
    new_item['correct_idx'] = correct_index
    
    # vid와 scene_contained 설정
    new_item['vid'] = item['Relevant scene'][0]
    new_item['scene_contained'] = item['Relevant scene']
    
    # question category가 있으면 que_type으로 변경
    if 'question category' in item:
        new_item['que_type'] = item['question category']
    
    new_data.append(new_item)

# 새로운 JSON 파일로 저장
with open('formatted_epqas_val.json', 'w', encoding='utf-8') as file:
    json.dump(new_data, file, ensure_ascii=False, indent=4)

print("변환이 완료되었습니다. 'formatted_epqas_val.json' 파일을 확인해주세요.")
