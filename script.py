from PIL import ImageGrab
import pyautogui
import pydirectinput
import win32api, win32con
import numpy
import time


def click(x,y):
    try:
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    except Exception:
        pass


confirm_loc=[0.761, 0.735]
confirm_loc2=[0.598, 0.639]

if __name__ == "__main__":
    print("一日游自动代刷脚本设置：模拟器开全屏，使用前请先组好队，设置队伍自动跟随，设置自动攻击，先领好一日游任务。")
    print("启动本脚本后请回到游戏全屏界面，本脚本会在每轮一日游完成后自动点确认和继续。")
    print("本纯绿色脚本由玩家*肝die冲鸭*为您开发")
    screenWidth, screenHeight = pydirectinput.size()
    print("[Debug] Screen resolution: {}x{}".format(screenWidth, screenHeight))
    #input("回车确认，确认后该程序会自动最小化")
    #cur_win = pyautogui.getActiveWindow()
    #cur_win.minimize()
    while True:
        time.sleep(5)
        pil_image=ImageGrab.grab()
        image=numpy.array(pil_image)
        gray=image.sum(axis=2)/3.0
        left_stripe_intensity = numpy.percentile(gray[:, 10:int(screenWidth*0.1125)],99)
        right_stripe_intensity = numpy.percentile(gray[:, int(screenWidth*0.925):screenWidth-10],99)
        print("[Debug] left stripe intensity: {}, right stripe intensity: {}".format(left_stripe_intensity, right_stripe_intensity))
        if left_stripe_intensity > 100 or right_stripe_intensity > 100:
            continue
        loc=[int(screenWidth*confirm_loc[1]), int(screenHeight*confirm_loc[0])]
        loc2=[int(screenWidth*confirm_loc2[1]), int(screenHeight*confirm_loc2[0])]
        try:
            pydirectinput.click(*loc)
            time.sleep(1)
            pydirectinput.click(*loc2)
        except Exception as ex:
            print(str(ex))

