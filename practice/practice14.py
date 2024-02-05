#%%
# 基礎編14

#%%
# ライブラリのインストール
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import japanize_matplotlib
%matplotlib inline

#%%
# 1
X = np.arange(0,400,1)

# 平均身長
height_mean = 140
# 身長標準偏差
height_sd = 20
Y = norm.pdf(X, height_mean , height_sd)
plt.plot(X , Y, label='身長')

# 平均座高
s_height_mean = 100
# 座高標準偏差
s_height_sd = 10
Y2 = norm.pdf(X, s_height_mean , s_height_sd)
plt.plot(X , Y2 , label='座高')

Y3 = norm.pdf(X, height_mean + s_height_mean , height_sd + s_height_sd)
plt.plot(X , Y3, label='身長+座高')

plt.xlabel('高さ')
plt.legend()
plt.show()


# %%
#2
(1 - norm.cdf(2)) * 100

#%%
#3
norm.ppf(0.90)


#%%
#4
height_mean = 172
height_sd = 5.5

#4-1 平均身長以下の人の割合
norm.cdf(height_mean, loc=height_mean, scale=height_sd) * 100

#4-2 平均±1標準偏差の間に収まる人の割合

#平均 + 標準偏差 以下の人の割合
upper = norm.cdf(height_mean + height_sd, loc=height_mean, scale=height_sd)

#平均 - 標準偏差 以下の人の割合
lower = norm.cdf(height_mean - height_sd, loc=height_mean, scale=height_sd)

(upper - lower) * 100

#4-3 180cm以上となる人の割合

#180cm以下の人の割合
lower = norm.cdf(180, loc=height_mean, scale=height_sd)

(1 - lower) * 100


#%%
#5
eng = 79
math = 82

eng_mean = 85
eng_sd = 4

math_sd = 10

#5-1
X = np.arange(0,100,1)
Y = norm.pdf(X, eng_mean , eng_sd)
plt.plot(X , Y , label='英語')
plt.vlines( eng , 0.1 ,0, label='A君')
plt.xlabel('点数')
plt.title('英語試験')
plt.legend()

norm.cdf(eng, loc=eng_mean, scale=eng_sd) * 100

#5-2
percentile = 0.95
z_value = norm.ppf(percentile)

math_mean = math - z_value * math_sd
print(math_mean)
# %%
