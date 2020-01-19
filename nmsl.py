# @File : 喷人软件

import time
import sys, os
import random
import tkinter as tk
import threading

# 键盘控制器
from pynput.keyboard import Key, Listener, Controller as key_cl
from pynput.mouse import Button, Controller
is_start = False
window = tk.Tk()
var = tk.StringVar()
var2 = tk.StringVar()
l = tk.Label(window, textvariable = var, bg = 'green', font = ('Arial', 12), width = 30, height = 2)

# 键盘监听
def on_press(key):
    global is_start, l
    # 开启
    if key == Key.f7:
        is_start = True
        l.configure(bg = 'green')
        var.set('nmsl开启')
    # 轰炸
    if key == Key.f8 and is_start == True:
        boom()
    # 暂停
    if key == Key.f9:
        is_start = False
        l.configure(bg = 'red')
        var.set('nmsl暂停')
    # 关闭
    if key == Key.f10:
        os._exit(0)
        return False
def on_release(key):
    pass

# 读文件
def read_file(filepath):
    with open(filepath, "r") as fp:
        content=fp.readlines()
        fp.close()
    return content

# 键盘控制函数
def keyboard_input(string):
    keyboard = key_cl()
    keyboard.type(string)

# 鼠标控制函数
def send():
    keyboard = key_cl()
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# 开始轰炸
def boom():
    #time.sleep(7)
    content = read_file("./nmsl.txt")
    # print(content[0])
    for i in range(1):
        keyboard_input(content[random.randint(0, len(content) - 1)])
        # send()
        time.sleep(0.5)

# 键盘监控线程入口函数
def threading_start():
    # 开启键盘监控
    global is_start
    is_start = True
    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

def main():
    # 设置界面
    global var, window, l
    var.set('nmsl开启')
    window.title('nmsl')
    window.geometry('300x100')
    l.pack()
    l2 = tk.Label(window, text = 'F7开启，F8开炮，F9暂停，F10关闭', bg = 'blue', font = ('Arial', 10), width = 35, height = 2)
    l2.pack()
    t1 = threading.Thread(target=threading_start)
    t1.start()
    window.mainloop()
    os._exit(0)


main()



