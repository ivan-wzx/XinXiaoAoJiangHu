from PIL import ImageGrab
import pyautogui
import pydirectinput
import win32api, win32con
#import cv2
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
confirm_loc2=[0.633, 0.570]
#thres=0.8
#t_confirm=cv2.imread(".\\templates\\yiriyou_jixu.png")
#t_confirm=cv2.cvtColor(t_confirm, cv2.COLOR_BGR2GRAY)

if __name__ == "__main__":
    print("一日游自动代刷脚本设置：模拟器开全屏，使用前请先组好队，队伍自动跟随，开好自动攻击，领好一日游任务。本脚本会在每轮一日游完成后自动点确认和继续。")
    print("本纯绿色脚本由玩家*肝die冲鸭*为您开发")
    screenWidth, screenHeight = pydirectinput.size()
    print("Screen resolution: {}x{}".format(screenWidth, screenHeight))
    input("回车确认，确认后该程序会自动最小化")
    cur_win = pyautogui.getActiveWindow()
    cur_win.minimize()
    while True:
        time.sleep(5)
        pil_image=ImageGrab.grab()
        image=numpy.array(pil_image)
        gray=image.sum(axis=2)/3.0
        left_stripe_intensity = numpy.percentile(gray[:, 10:int(screenWidth*0.1125)],99)
        right_stripe_intensity = numpy.percentile(gray[:, int(screenWidth*0.925):screenWidth-10],99)
        if left_stripe_intensity > 100 or right_stripe_intensity > 100:
            continue
        
        loc=[int(screenWidth*confirm_loc[1]), int(screenHeight*confirm_loc[0])]
        #click(*loc)
        loc2=[int(screenWidth*confirm_loc2[1]), int(screenHeight*confirm_loc2[0])]
        try:
            #pydirectinput.moveTo(1, 1)
            pydirectinput.click(*loc)
            #pydirectinput.click()
            #pydirectinput.doubleClick()
        except Exception as ex:
            print(str(ex))

