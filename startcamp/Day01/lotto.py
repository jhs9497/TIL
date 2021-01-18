import random

numbers = range(1, 46)
lotto = random.sample(numbers, 6)
print(f'이번 주 행운의 로또 번호는 {sorted(lotto)}입니다!')

