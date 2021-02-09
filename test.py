import win32gui
import win32api
import win32con
import time

# handle0 = win32gui.FindWindow (None, "PrincessConnectReDive")
# print(handle0)
# # win32gui.SetForegroundWindow(handle0)
# # win32gui.SetActiveWindow(handle0)
# handle1 = win32gui.FindWindowEx(handle0, None, None, None)
# print(handle1)
# handle0 = 8850708
#
# def doClick(cx, cy, hwnd):
#     long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
#     win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
#     time.sleep(1)
#     win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起
# print("ready")
# time.sleep(2)
# print("go")
# doClick(500, 500,handle0)
print(time.localtime())