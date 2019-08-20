import tkinter as tk
import tkinter.font as tkFont
import datetime
 
def CalcRemainsTime(year=2019, month=7, day=26):
    target_date = datetime.datetime(year, month, day)##设定目标时间
    time_now = datetime.datetime.now()##获取当前时间
    remains_sec = (target_date - time_now).total_seconds()##获取时间差总秒数
    remains_day = remains_sec // (60 * 60 * 24)##剩余天数
    remains_sec -= remains_day * (60 * 60 * 24)##剩余秒数
    remains_hour = remains_sec // (60 * 60)##剩余小时
    remains_sec -= remains_hour * (60 * 60)##剩余秒
    remains_min = remains_sec // (60)##剩余分钟
    remains_sec -= remains_min * 60
    ##返回字符串内容
    content = "Cutdown:" + str(int(remains_day)) + "day," + str(int(remains_hour)) + "hour," + str(int(remains_min)) + "min," + str(int(remains_sec)) + "sec!"
    return content
 
window = tk.Tk()
window.title("Count Down")##窗体标题
window.overrideredirect(True)##隐藏窗体任务栏
window.attributes("-transparentcolor","#ce3366")##窗口对该颜色透明，注意rgb = ce3366
window["background"] = "#ce3366"##设置窗口背景为透明颜色 rgb = ce3366
 
##设置字体，使用名为 Buxton Sketch 的字体，大小36，加粗，还有斜体和下划线等参数，没有使用
ft = tkFont.Font(family="Buxton Sketch", size= 36, weight=tkFont.BOLD)
content = CalcRemainsTime()##获取倒计时时间
##创建一个label实例
cutdown_label = tk.Label(window, text = content, bg="#ce3366", font=ft, fg = "#cd3366")
##fg是label的字体颜色 rgb = cd3366
##bg是label的背景色，取与字体颜色近似的 rgb = ce3366，防止字体边框出现异样，上述取ce3366同理
 
cutdown_label.pack()##放置label
 
##获取屏幕的尺寸
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
##初始窗口放在屏幕正下方
##偷懒了，写了固定值
x = str((screen_width - 888) // 2)
y = str(screen_height - 75)
window.geometry("+"+ x + "+" + y)
 
##用于判断鼠标是否进入窗体（控件）的标志位
mouse_leave_flag = False
 
##显示窗体标题栏
def Display():
    global mouse_leave_flag
    if mouse_leave_flag == False:
        window.overrideredirect(False)
 
##鼠标进入事件的相应操作
def MouseEnter(event):
    mouse_leave_flag = False
    window.overrideredirect(False)
##鼠标离开事件的相应操作
def MouseLeave(event):
    mouse_leave_flag = True
    window.overrideredirect(True)
##更新倒计时
def Refresh():
    content = CalcRemainsTime()##获取倒计时时间
    cutdown_label["text"] = content##更新label内容
    window.after(1000, Refresh)##after是指在此以后1000ms再调用Refresh，这里相当于1s的定时
 
##绑定事件的响应
window.bind("<Enter>", MouseEnter)
window.bind("<Leave>", MouseLeave)
 
##进入主循环之前，进入一次Refresh，相当于开启定时器
window.after(1000, Refresh)
 
window.mainloop()
