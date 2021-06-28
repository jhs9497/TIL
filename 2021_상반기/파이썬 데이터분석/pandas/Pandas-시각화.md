## Plot 그래프

```python
df.plot()

plt.rcParams["figure.figsize"] = (12,9)\
# 그래프 사이즈 조절

df['분양가'].plot(kind=line)

# kind 옵션을 통해 원하는 그래프를 그릴 수 있다.
line 선그래프

bar 바 그래프

barh 수평 바 그래프

hist 히스토그램

kde 커널 밀도 그래프

hexbin 고밀도 산점도 그래프
df.plot(kind='hexbin', x='분양가', y='연도', gridsize=20)

box 박스 플롯

area 면적 그래프

pie 파이 그래프

scatter 산점도 그래프

```

