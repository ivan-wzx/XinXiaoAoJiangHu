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


confirm_loc=[0.761, 0.789]
confirm_loc2=[0.633, 0.592]
#thres=0.8
#t_confirm=cv2.imread(".\\templates\\yiriyou_jixu.png")
#t_confirm=cv2.cvtColor(t_confirm, cv2.COLOR_BGR2GRAY)

if __name__ == "__main__":
    print("一日游自动代刷脚本：使用前请先组好队，队伍自动跟随，开好自动攻击，领好一日游任务。本脚本会在每轮一日游完成后自动点确认和继续。")
    print("本纯绿色脚本由肝die冲鸭玩家为您开发")
    screenWidth, screenHeight = pydirectinput.size()
    print("Screen resolution: {}x{}".format(screenWidth, screenHeight))
    input("回车确认，确认后该程序会自动最小化")
    cur_win = pyautogui.getActiveWindow()
    cur_win.minimize()
    while True:
        time.sleep(3)
        #pil_image=ImageGrab.grab()
        #image=numpy.array(pil_image)
        #cv2.imwrite("c.png", image)
        #img_gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        
        loc=[int(screenWidth*confirm_loc[1]), int(screenHeight*confirm_loc[0])]
        #click(*loc)
        loc2=[int(screenWidth*confirm_loc2[1]), int(screenHeight*confirm_loc2[0])]
        try:
            #pydirectinput.moveTo(1, 1)
            pydirectinput.click(*loc)
            time.sleep(1)
            pydirectinput.click(*loc2)
            #pydirectinput.click()
            #pydirectinput.doubleClick()
        except Exception as ex:
            print(str(ex))
        
    
    """     res = cv2.matchTemplate(img_gray, t_confirm, cv2.TM_CCOEFF_NORMED)
        w, h = t_confirm.shape
        res[numpy.where(res<=thres)]=0
        print(str(img_gray.shape))
        print(str(res))
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val<=thres:
            continue
        loc=[max_loc[0]+w/2, max_loc[1]+h/2]
        pyautogui.click(*max_loc) """
