import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method = 'ffill')
df2.info()

df2.rename(columns= {'일강수량':'ran_temp'}, inplace=True)

df2.head(3)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(df2['일시'], df2['ran_temp'], label='최고기온', c= 'r')


plt.xlabel('일')
plt.ylabel('강수량')
plt.legend()
plt.show()
