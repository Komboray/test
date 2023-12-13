import threading
import time

def eat_break():
    time.sleep(2)
    print("I have eaten")

def read_book():
    time.sleep(4)
    print("Book understood")

def go_to_work():
    time.sleep(8)
    print("I am at work")



x = threading.Thread(target=eat_break(), args=())
x.start()

z = threading.Thread(target=read_book(), args=())
z.start()

y = threading.Thread(target=go_to_work(), args=())
y.start()


x.join()
z.join()
y.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())