# 打包操作
# 安装pyinstaller
# cmd输入 pip install pyinstaller
# shift+右击文件夹 点击在此处打开命令窗口
# pyinstaller -F -w love.py  //打包程序

# 引用tkinter工具包
from tkinter import *   #__all__=[a,b]
from tkinter import messagebox

# 定义关闭窗口提示
def closeWindow():
    messagebox.showinfo(title="警告",message ="望穿秋水,只为一人憔悴")
    return

# 定义喜欢按钮的提示
def Love():
    love = Toplevel(window)
    love.geometry("300x100+250+260")
    love.title("我也喜欢你")
    label = Label(love, text = "我也喜欢你!",font = ("微软雅黑",20))
    label.pack()
    btn = Button(love,text = "好呀",width = 10,height = 2,command=closeallwindow)
    btn.pack()
    love.protocol("WM_DELETE_WINDOW", closelove)
def closelove():
    return

# 关闭所有窗口
def closeallwindow():
    window.destroy()

# 定义不喜欢按钮的提示
def noLove():
    no_love = Toplevel(window)
    no_love.geometry("300x100+520+260")
    no_love.title("重新选")
    label = Label(no_love,text="弱水三千，只取一瓢",font = ("微软雅黑",18))
    label.pack()
    btn = Button(no_love,text="好呀", width=10, height=2,command=no_love.destroy)
    btn.pack()
    no_love.protocol("WM_DELETE_WINDOW",closenolove)

# 窗口不能关
def closenolove():
    noLove()

# 创建窗口
window = Tk()
# 窗口标题
window.title("May I love you？")
# 窗口大小
window.geometry("380x470+600+240")
# love.title("哈哈")
btn=Button(text="确定")
# 窗口位置
# window.geometry("+500+240")
window.protocol("WM_DELETE_WINDOW",closeWindow )
#标签控件
label = Label(window,text = "hey,王晓炎",font = ("微软雅黑",15),fg = "red")
label.grid(row = 0, column = 0 )

label = Label(window,text = "开心最重要哦",font = ("微软雅黑",30))
label.grid(row = 1, column = 1,sticky = E)

# 插入图片
"""
photo = PhotoImage(file = "123.png")
imageLable = Label(window,image = photo)
imageLable.grid(row = 2,columnspan = 2)
"""
# 喜欢按钮插件
btn = Button(window,text="喜欢",width=15,height=2,command=Love)
btn.grid(row=3,column=0,sticky= W)

# 不喜欢按钮插件
btn = Button(window,text="不喜欢" ,command=noLove)
btn.grid(row=3,column=1,sticky= E)
# 显示窗口 消息循环
window.mainloop()
