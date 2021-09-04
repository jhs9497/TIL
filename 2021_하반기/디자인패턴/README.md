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



## Open-closed principle

- extension(확장)에 대해서는 open,

- modification(수정)에 대해서는 closed되어야 한다

- code에 대한 제한이 아니라 code behavior에 대한 원칙이다.

```python
# 잘못된 예시

class Animal():
  def __init__(self,type):
    self.type = type


def hey(animal):
  if animal.type == 'Cat':
    print('meow')
  elif animal.type == 'Dog':
    print('bark')

bingo = Animal('Dog')
kitty = Animal('Cat')

#Cow와 Sheep을 추가하기위해 hey함수의 수정이 필요하다. 즉 modification에 대해 closed되어 있지 않으므로 Opne-closed원칙에 위배된다.

hey(bingo)
hey(kitty)
```



```python
# 옳바른 예시

class Animal: 
  def speak(self):  #interface method
    pass

class Cat(Animal):
  def speak(self):
    print("meow")

class Dog(Animal):
  def speak(self):
    print("bark")

class Sheep(Animal):
  def speak(self):
    print("meh")

class Cow(Animal):
  def speak(self):
    print("moo")

def hey(animal):
  animal.speak();

# hey 함수는 전혀 건들필요가 없다. 동물을 추가하고 싶으면 class를 상속해주며 계속 추가해주면된다. 즉 동물의 추가 (확장)은 무한으로 가능하되 hey함수의 수정은 할 필요가 없으므로 Open-Closed 원칙을 준수하는 것이다.

bingo = Dog()
kitty = Cat()
sheep = Sheep()
cow = Cow()

hey(bingo)
hey(kitty)
hey(sheep)
hey(cow)
```

