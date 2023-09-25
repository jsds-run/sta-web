#%%
# 基礎編13

#%%
# ライブラリのインストール
from scipy.stats import binom #2項分布
# k=事象の回数 n=試行回数 p=確率

from scipy.stats import poisson #ポワソン分布
# k=事象の回数 mu= n×p n=試行回数 p=確率

from scipy.stats import geom #幾何分布

#%%
#1 2項分布
p1 = binom.pmf(k=6 , p=1/6 , n=10)
print(p1)
#%%
#2 2項分布
p2_1 = binom.pmf(k=3 , p=3/10 , n=5)
p2_2 = binom.pmf(k=4 , p=3/10 , n=5)
p2_3 = binom.pmf(k=5 , p=3/10 , n=5)
print(p2_1 + p2_2 + p2_3)

# %%
#3 ポワソン分布
p3 = poisson.pmf(k=5 , mu= 100 * 1/40)
print(p3)
# %%
#4 ポワソン分布
p4_0 = poisson.pmf(k=0 , mu = 40 * 0.05)
p4_1 = poisson.pmf(k=1 , mu = 40 * 0.05)
p4_2 = poisson.pmf(k=2 , mu = 40 * 0.05)
p4 = 1 - (p4_0 + p4_1 + p4_2)
print(p4)
# %%
#5 幾何分布の期待値
p5 = 0.25
print(1/0.25)
