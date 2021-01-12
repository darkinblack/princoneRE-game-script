from tkinter import *
import tkinter.messagebox
import win32con
import win32gui
import win32api
import pyautogui
import subprocess
import time


# import pcr


class Application(Frame):

    def say_hi(self):
        print("hi there, everyone!")

    # def doBattle(self):
    #     pcr.test.dailyEvent()
    #     # print("111")

    def oneDungeon(self):
        self.pcrclick("+")
        self.pcrclick("+")
        time.sleep(1)
        self.pcrclick("ticket")
        time.sleep(1)
        self.pcrclick("ok")
        time.sleep(7)
        self.pcrclick("wuyiyi")
        time.sleep(1)
        self.pcrclick("wuyiyi")
        time.sleep(1)

    def tansuo(self):
        self.pcrclick("home")
        time.sleep(5)
        self.pcrclick("battle")
        time.sleep(1)
        self.pcrclick("tansuo")
        time.sleep(1)
        self.pcrclick("tansuojingyan")
        time.sleep(1)
        self.pcrclick("lv10")
        time.sleep(1)
        self.pcrclick("+")
        time.sleep(1)
        self.pcrclick("ticket")
        time.sleep(1)
        self.pcrclick("ok")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(2)
        self.pcrclick("wuyiyi")
        time.sleep(2)
        self.pcrclick("lv10")
        time.sleep(1)
        self.pcrclick("+")
        time.sleep(1)
        self.pcrclick("ticket")
        time.sleep(1)
        self.pcrclick("ok")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(2)
        self.pcrclick("wuyiyi")
        time.sleep(2)
        self.pcrclick("home")

    def dailyEvent(self):
        self.pcrclick("home")
        time.sleep(3)
        self.pcrclick("battle")
        time.sleep(3)
        self.pcrclick("event")
        time.sleep(3)
        self.pcrclick("wuyiyi")
        self.pcrclick("wuyiyi")
        self.pcrclick("wuyiyi")
        time.sleep(1)
        self.pcrclick("hard")
        time.sleep(1)
        self.pcrclick("H1-5")
        time.sleep(1)

        self.oneDungeon()
        self.pcrclick("leftpage")
        time.sleep(1)
        self.oneDungeon()
        self.pcrclick("leftpage")
        time.sleep(1)
        self.oneDungeon()
        self.pcrclick("leftpage")
        time.sleep(1)
        self.oneDungeon()
        self.pcrclick("leftpage")
        time.sleep(1)
        self.oneDungeon()
        self.pcrclick("cancel")
        time.sleep(1)
        self.pcrclick("veryhard")
        time.sleep(1)
        self.pcrclick("tiaozhan")
        time.sleep(1)
        self.pcrclick("battlestart")
        time.sleep(60)
        self.pcrclick("next")
        time.sleep(7)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("home")


    def ta(self):
        self.pcrclick("battle")
        time.sleep(3)
        self.pcrclick("ta")
        time.sleep(5)
        self.pcrclick("lvlong")
        time.sleep(5)
        self.pcrclick("ok")
        time.sleep(8)
        self.pcrclick("taweizhi1")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("team")
        time.sleep(5)
        self.pcrclick("team1")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(30)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(5)
        self.pcrclick("taweizhi2")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(30)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(5)
        self.pcrclick("taweizhi3")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(30)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(5)
        self.pcrclick("taweizhi4")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(30)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(5)
        self.pcrclick("taweizhi5")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("team")
        time.sleep(5)
        self.pcrclick("team2")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(100)
        self.pcrclick("taback")
        time.sleep(5)
        self.pcrclick("taweizhi5")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(5)
        self.pcrclick("team")
        time.sleep(5)
        self.pcrclick("team3")
        time.sleep(5)
        self.pcrclick("battlestart")
        time.sleep(100)
        self.pcrclick("next")
        time.sleep(5)
        self.pcrclick("wuyiyi")
        time.sleep(5)
        self.pcrclick("home")

    def shoutili(self):
        self.pcrclick("home")
        time.sleep(5)
        self.pcrclick("house")
        time.sleep(5)
        self.pcrclick("yikuoshouqu")
        time.sleep(2)
        self.pcrclick("wuyiyi")
        time.sleep(1)
        self.pcrclick("wuyiyi")
        time.sleep(1)
        self.pcrclick("home")


    def excute(self):
        if self.var1_daily.get() == 1:
            self.dailyEvent()
            time.sleep(5)
        if self.var2_ta.get() == 1:
            self.ta()
            time.sleep(5)
        if self.var3_tansuo.get() == 1:
            self.tansuo()
            time.sleep(5)
        tkinter.messagebox.showinfo(title='finish', message='执行完成')



    def pcrclick(self, name):
        pos = [int(self.button[name][0]*self.lenth)+self.left,int(self.button[name][1]*self.height)+self.top]
        pyautogui.click(x=pos[0], y=pos[1])
    def click(self):
        if self.hwnd == 0:
            tkinter.messagebox.showinfo(title='error', message='请先获取句柄和位置')
        else:self.pcrclick("home")

    def findhwnd(self):
        self.hwnd = win32gui.FindWindow(0, "PrincessConnectReDive")

        if self.hwnd == 0:
            tkinter.messagebox.showinfo(title='error', message='未检测到pcr启动')
        else:
            tkinter.messagebox.showinfo(title='找到pcr', message='句柄  ' + str(self.hwnd))

    def showhwnd(self):
        tkinter.messagebox.showinfo(title='句柄', message=str(self.hwnd))
    def testbutton(self):
        print(self.var1_daily.get())
        print(self.var2_ta.get())
        print(self.var3_tansuo.get())

    def getposition(self):
        self.left, self.top, self.right, self.bottom = win32gui.GetWindowRect(self.hwnd)
        tkinter.messagebox.showinfo(title='成功获取位置', message=str(self.left)+" "+str(self.top))
        self.lenth = self.right-self.left
        self.height = self.bottom-self.top
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "top"})
        # 获取句柄
        self.gethwnd = Button(self, text="获取句柄", command=self.findhwnd)
        self.gethwnd.pack()
        # 显示句柄
        self.showhwnd = Button(self, text="显示句柄", command=self.showhwnd)
        self.showhwnd.pack()
        # 勾选任务
        c1 = Checkbutton(self, text='daily', variable=self.var1_daily, onvalue=1, offvalue=0)
        c1.pack()
        c2 = Checkbutton(self, text='ta', variable=self.var2_ta, onvalue=1, offvalue=0)
        c2.pack()
        c3 = Checkbutton(self, text='tansuo', variable=self.var3_tansuo, onvalue=1, offvalue=0)
        c3.pack()
        # 测试button
        self.test = Button(self, text="测试", command=self.testbutton)
        self.test.pack()
        # 获取坐标
        self.getposition = Button(self, text="获取位置", command=self.getposition)
        self.getposition.pack()

        self.click = Button(self, text="click", command=self.click)
        self.click.pack()

        self.excute = Button(self, text="执行", command=self.excute)
        self.excute.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.hwnd = 0
        self.var1_daily = IntVar()
        self.var2_ta = IntVar()
        self.var3_tansuo = IntVar()
        self.pack()
        self.createWidgets()
        self.left, self.top, self.right, self.bottom = 0,0,0,0
        self.lenth, self.height = 0,0
        self.button = {"battle": [0.4984591679506934, 0.9413298565840938],
                       "home": [0.09784283513097072, 0.9374185136897001],
                       "event": [0.4275808936825886, 0.7913950456323338], \
                       "N1-15": [0.6448382126348228, 0.516297262059974],
                       "normal": [0.7912172573189522, 0.19556714471968709],
                       "hard": [0.9144838212634823, 0.19426336375488917], \
                       "H1-5": [0.6902927580893683, 0.42633637548891784],
                       "leftpage": [0.032357473035439135, 0.47979139504563234],
                       "+": [0.9090909090909091, 0.6232073011734028], \
                       "ticket": [0.7781201848998459, 0.5958279009126467],
                       "ok": [0.615562403697997, 0.6936114732724902],
                       "popclose": [0.4984591679506934, 0.6870925684485006],
                       "wuyiyi": [0.031587057010785825, 0.15645371577574968],
                       "cancel": [0.6900800985828712, 0.8404588112617309], \
                       "veryhard": [0.9008009858287123, 0.4921793534932221],
                       "tiaozhan": [0.878003696857671, 0.8592283628779979],
                       "battlestart": [0.8607516943930992, 0.8300312825860271], \
                       "next": [0.8428835489833642, 0.9009384775808134],
                       "tansuo": [0.7621688231669748, 0.2857142857142857],
                       "tansuojingyan": [0.6062846580406654, 0.4744525547445255], \
                       "lv10": [0.7430683918669131, 0.3013555787278415],
                       "ta": [0.9081947011706716, 0.28988529718456724],
                       "lvlong": [0.8539741219963032, 0.4807090719499479], \
                       "taweizhi1": [0.7085643869377696, 0.5140771637122002],
                       "team": [0.8946395563770795, 0.19708029197080293],
                       "team1": [0.8213185459026494, 0.40145985401459855], \
                       "team2": [0.8194701170671596, 0.6100104275286757],
                       "team3": [0.8188539741219963, 0.7924921793534933],
                       "taweizhi2": [0.5077017868145409, 0.4984358706986444], \
                       "taweizhi3": [0.23844731977818853, 0.4859228362877998],
                       "taweizhi4": [0.5077017868145409, 0.48279457768508866],
                       "taweizhi5": [0.747381392483056, 0.49635036496350365], \
                       "taback": [0.8391866913123844, 0.9124087591240876],
                       "house": [0.6414048059149723, 0.9374348279457768],
                       "yikuoshouqu": [0.9285274183610598, 0.7977059436913452]}


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
