### 0323 django HW

---

#### 1.

---

- is_active

- is_staff
- is_superuser



#### 2.

---

- 150글자



#### 3.

---

- is_authenticated



#### 4.

---

- (a) AuthenticationForm

- (b) login
- (c) form.get_(user)



#### 5.

---

- AnonymousUser



#### 6.

---

- algorithm: PBKDF2
- hash function: SHA256



#### 7.

---



```python
# Wrong
def logout(request):
    logout(request) # Error. 재귀 호출 발생
    return redirect('accounts:login')

# Correct
def logout(request):
    auth_logout(request) # import logout as auth_logout으로 이름 바꿔줌
    return redirect('accounts:login')
```





