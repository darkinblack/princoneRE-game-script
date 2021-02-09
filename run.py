import subprocess

import pyautogui
import win32api
# subprocess.Popen('D:\\Program Files\\DMMgames\\priconner\\PrincessConnectReDive.exe')
# win32api.ShellExecute(0, 'open', 'notepad.exe', '', '', 1)
import win32gui
import win32con
import time

hwnd = win32gui.FindWindow(0, u"PrincessConnectReDive")
print(hwnd)
# print(hwnd)
# windowRec = win32gui.GetWindowRect(hwnd)
# print(windowRec)
# pyautogui.click(600, 600)
# child= win32gui.FindWindowEx(parent,None,ChildClass, None)


def doClick(cx, cy, hwnd):
    long_position = win32api.MAKELONG(cx, cy)  # 模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)  # 模拟鼠标按下
    time.sleep(1)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)  # 模拟鼠标弹起


# doClick(300,500,15994496)

from pprint import pprint


def gbk2utf8(s):
    return 0


def show_window_attr(hWnd):
    '''
    显示窗口的属性
    :return:
    '''
    if not hWnd:
        return

    # 中文系统默认title是gb2312的编码
    title = win32gui.GetWindowText(hWnd)
    title = gbk2utf8(title)
    clsname = win32gui.GetClassName(hWnd)

    # print('窗口句柄:%s ' % (hWnd))
    # print('窗口标题:%s' % (title))
    # print('窗口类名:%s' % (clsname))



def show_windows(hWndList):
    for h in hWndList:
        show_window_attr(h)


def demo_top_windows():
    '''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    show_windows(hWndList)

    return hWndList


def demo_child_windows(parent):
    '''
    演示如何列出所有的子窗口
    :return:
    '''
    if not parent:
        return

    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hWndChildList)
    show_windows(hWndChildList)
    return hWndChildList


hWndList = demo_top_windows()
assert len(hWndList)

parent = hwnd
# 这里系统的窗口好像不能直接遍历，不知道是否是权限的问题
hWndChildList = demo_child_windows(parent)

print('-----top windows-----')
# pprint(hWndList)

print('-----sub windows:from %s------' % (parent))
pprint(hWndChildList)
