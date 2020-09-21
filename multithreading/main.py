import threading
from queue import Queue
import time
def new():
   for x in range(6):
      print("Thread 1 Here!!")
def new_():
   for x in range(6):
      print("Thread 2 Here!!")
t1=threading.Thread(target=new)

t2=threading.Thread(target=new_)

t2.start()
t1.start()
#t2.join()
#t1.join()
#print("Main Thread Here!!")
