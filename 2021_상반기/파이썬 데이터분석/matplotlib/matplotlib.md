## matplotlib

- 파이썬 표준 시각화 도구라고 불릴만큼 다양한 기능지원
- 세부 옵션을 통하여 아름다운 스타일링 가능
- 보다 다양한 그래프를 그릴 수 있음
- pandas와 연동이 용이함

https://matplotlib.org/



```python
import matplotlib.pyplot as plt

# 단일 그래프
data = np.arange(1, 100)
plt.plot(data)
plt.show()

# 다중 그래프
data1 = np.arange(1, 51)
data2 = np.arange(51, 101)

plt.plot(data1)
plt.plot(data2)
plt.plot(data2+50)

plt.show()

# 2개의 figure로 나누어서 다중 그래프 그리기
# figure()는 새로운 그래프 canvas를 생성한다.

data1 = np.arange(1, 51)
data2 = np.arange(51, 101)
plt.plot(data1)
plt.figure()
plt.plot(data2)
plt.show()

```



