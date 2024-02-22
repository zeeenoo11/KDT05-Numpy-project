import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns


file = 'DATA/김성윤 분석 - 시트3.csv'

df = pd.read_csv(file, header=0, encoding='utf-8-sig')
print(df)
print(df.dtypes)
# 파일 내 '-'를 0으로 바꾸기
df = df.replace('-', 0)
df['AVG'] = df['AVG'].astype(float)


def coef_SB(player):
    ar1 = df[df['선수명'] == player].loc[:, 'AVG']
    ar2 = df[df['선수명'] == player].loc[:, 'SB']
    return np.corrcoef(ar1, ar2)


# 선수의 상관계수 뽑기
players = ['이용규', '이대형', '이종욱', '정근우', '박해민']
# data = df[df['선수명'] == players[0]].iloc[:, 3:]
# print(data.corr())
# print(coef_SB('이용규'))
# # heatmap 그리기
plt.figure(figsize=(15, 10))
for player in players[1:]:
    data = df[df['선수명'] == player].iloc[:, 3:]

    plt.subplot(2, 2, players.index(player))
    sns.heatmap(data.corr(), cmap='Blues')
# 플롯 보이기
plt.show()


# 따라서 ㅇㅇㅇ 변수가 도루에 큰 영향을 준다

# 타율을 높이려면 어떻게 해야할까?

# 5명 선수들의 AVG 그래프로 표현하기
plt.figure(figsize=(8, 6))
for player in players:
    df_2 = df[df['선수명'] == player]
    df_3 = df_2[df_2['AVG'] > 0.1 ]
    xs = df_3['연도']
    ys = df_3['AVG']    # ['AVG'].astype(float)
    ys2 = df_3['SB']
    ys3 = df_3['OBP']
    print(xs, ys)
    # data = df[df['선수명'] == player].loc[:, 'AVG']
    plt.plot(xs, ys.astype(str), label='AVG')
    plt.plot(xs, ys2, label='SB')
    # plt.ylim(0.15, 0.30)
    # plt.yticks(np.arange(0.15, 0.30, 0.01))
    plt.plot(xs, ys3, label='OBP')
    # plt.ylim(0.20, 0.38)
    # plt.xticks(np.arange(2005, 2023, 3))
    # plt.yticks(np.arange(0.20, 0.38, 0.01))
    plt.legend()
    plt.show()

plt.stackplot(xs, ys)
plt.stackplot(xs, ys2)
plt.show()