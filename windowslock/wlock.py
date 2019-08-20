# from ctypes import * 
# user32 = windll.user32
# user32.LockWorkStation()
from app import add



if __name__ == "__main__":
    print('start desk')
    desk=add(2,8)
    print('end desk')
    print(desk)
    