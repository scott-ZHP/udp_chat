from threading import Thread
from time import sleep


def music():
    for i in range(3):
        sleep(1.5)
        print("ｄａｎｃing")



t=Thread(target=music)

t.start()

for i in range(3):
    print("")
t.join()