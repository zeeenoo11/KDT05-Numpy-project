import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 불러오기
file = 'DATA/김성윤 분석 - 전체 선수 기록 (1).csv'
df = pd.read_csv(file, encoding='utf-8')
print(df)
print(df.dtypes)

# 선수별 통산 기록 추출; Top 10
# print(df.선수명.value_counts().head(10))
top10_players = df.선수명.value_counts().head(10).index
print(top10_players)

# 선수별 기록 저장
plt.figure(figsize=(10, 5))
y_sum_list = []
for player in top10_players:
    # 선수명에 해당하는 연도, 팀명, G 출력
    print(player)
    print('평균 순위:', np.mean(df[df['선수명'] == player]['순위']))
    print('평균 도루:', np.mean(df[df['선수명'] == player]['SB']))
    print(df[df['선수명'] == player][['연도', '순위', '팀명', 'G', 'SB']])

    xs = df[df['선수명'] == player]['연도']
    ys = df[df['선수명'] == player]['SB'] / df[df['선수명'] == player]['G'] * 10
    y_sum = df[df['선수명'] == player]['SB'].sum()
    y_sum_list.append(y_sum)

    plt.plot(xs, ys)
    plt.xticks(range(2005, 2023, 5))
    plt.xlabel('Year')
    plt.ylabel('도루수/경기수 (10배수)')

plt.legend(top10_players)
plt.show()

# 또는 선수의 도루수/경기수 총합으로 계산

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)

ax.bar(top10_players, y_sum_list, color=[ '#D32F2F','#E57373','#FFCDD2', '#D32F2F', '#D32F2F', '#EF9A9A', '#D32F2F', '#D32F2F', '#FF8A80','#EF9A9A', '#FFCDD2','#FF8A80', '#EF9A9A'])
ax.set_ylabel('도루수 총합')
plt.show()


# 이제 여기서 선수를 어떻게 뽑을까나
def sb_graph(player):
    plt.figure(figsize=(8, 5))
    xs = df[df['선수명'] == player]['연도']
    ys = df[df['선수명'] == player]['SB']

    plt.bar(xs, ys)
    # plt.plot(xs, df[df['선수명'] == player]['순위'], color='red')
    plt.hlines(np.mean(ys), xs.min()-0.5, xs.max()+0.5, colors='gray', linestyles='--')
    plt.ylabel('도루수')
    plt.show()


def corrcoeff(player):
    ar1 = df[df['선수명'] == player]['SB']
    ar2 = df[df['선수명'] == player]['순위']
    return np.corrcoef(ar1, ar2)[0, 1]


# 1. 이대형
sb_graph('이대형')
print(corrcoeff('이대형'))


# 2. 이종욱 : 롤모델

# 3. 박해민

# 4.

