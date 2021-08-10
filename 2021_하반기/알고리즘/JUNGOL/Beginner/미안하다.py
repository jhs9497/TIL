import time

def sorry(message):
    print(message)
    time.sleep(1)
    sorry(message)
message = '미안하다'
sorry(message)
