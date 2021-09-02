학습 출처 : https://www.youtube.com/channel/UCHcG02L6TSS-StkSbqVy6Fg



## Single Responsibility(단일 책임 원칙)

모든 함수나 class는 하나의 part에 대해서만 책임을 가져야한다!

```python
# 잘못된 예시
class Cat:
  def __init__(self,age,name):
    self.age = age
    self.name = name
  
  def eat(self):
    print("eating..")

  def walk(self):
    print("walking..")

  def speak(self):
    print("meow~")
    
  def print(self):
    print(f"age:{self.age} name:{self.name}")
    
  def log(self, logger):
    logger.log(f"age:{slef.age} name:{self.name}")
    logger.log(datetime.now())
    
# why? 고양이라는 class를 생각했을 때 print나 log라는 행위는 고양이라는 class와 맞지 않음
```



```python
# 옳바른 예시

class Cat:
  def __init__(self,age,name):
    self.age = age
    self.name = name
  
  def eat(self):
    print("eating..")

  def walk(self):
    print("walking..")

  def speak(self):
    print("meow~")
  
  # 상태를 나타내는 함수를 만들고
  def repr(self):
    return f"name:{self.name}, age:{self.age}"
  
kitty = Cat(3,"kitty")
kitty.eat()
kitty.walk()
kitty.speak()

# 상태를 나타내는 함수를 불러서 print해준다
print(kitty.repr())
#Logger.log(kitty.repr()) ,  If you have the logger object
```

