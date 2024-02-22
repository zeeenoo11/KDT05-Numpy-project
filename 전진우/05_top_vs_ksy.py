import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns

file_ksy = 'DATA/김성윤 분석 - 김성윤 개인 기록.csv'
file_player = 'DATA/김성윤 분석 - 시트3.csv'

print(pd.read_csv(file_ksy, encoding='utf-8'))
print(pd.read_csv(file_player, encoding='utf-8'))

ksy_df = pd.read_csv(file_ksy, encoding='utf-8')
player_df = pd.read_csv(file_player, encoding='utf-8')

player_df.replace('-', np.NAN, inplace=True)
player_df['SLG'].astype(float)
print(player_df.dtypes)

# player의 SLG, OBP 를 추출
plt.figure(figsize=(10, 6))

xs = player_df['연도']
ys = player_df['SLG'].mean()
plt.stackplot(xs, ys)
plt.show()

