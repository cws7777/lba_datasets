import json

def count_dots_in_summaries(episode_list):
    dot_counts = []
    for episode in episode_list:
        summary = episode.get("episode_summary", "")
        dot_count = summary.count('.')
        dot_counts.append(dot_count)
    return dot_counts

# JSON 파일에서 리스트 불러오기
with open('../scenelevel_integrate/AnotherMissOhQA_test_epsc.json', 'r') as file:
    episode_list = json.load(file)

# 에피소드 요약에서 점의 개수를 세기
dot_counts = count_dots_in_summaries(episode_list)
print(f"The number of dots in each episode summary is: {dot_counts}")

