import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 불러오기
file = 'DATA/김성윤 분석 - 타자순위_2023.csv'
df = pd.read_csv(file, encoding='utf-8')
print(df)
print(df.dtypes)

# 평균 경기수 G를 바 그래프로 출력
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

ax.bar(df['선수명'], df['G'], width=1)
plt.hlines(y=101, xmin=-1, xmax=len(df['선수명']), color='red', linestyle='-')
ax.set_xticks([])
plt.ylim(95, 160)
# ax.set_xlabel('타자 순위권 선수 명단')
# ax.set_ylabel('경기 수')
plt.show()

# AVG 순위

plt.figure(figsize=(8, 6))
xs = df['순위'].sort_values(ascending=False)
ys = df['AVG']
x_ksy = 0.314

plt.stackplot(xs, ys)
plt.vlines(43, 0.2, 0.35, colors='red', linestyles='--')
plt.ylim(0.2, 0.35)
plt.xticks([])
plt.show()

