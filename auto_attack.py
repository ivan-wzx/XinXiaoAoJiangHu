from PIL import ImageGrab
import pyautogui
import pydirectinput
import win32api, win32con
import numpy
import time


shili_icon = [0.509, 0.0577]
shili_loc_changle = [0.299, 0.215]
confirm_loc = [0.638, 0.593]
minimap_loc = [0.941, 0.095]
diaoxiang_loc_changle = [0.502, 0.487]
close_button = [0.936, 0.177]
auto_attack = [0.604, 0.852]
task_loc = [0.117, 0.241]
submit_confirm_loc = [0.810, 0.697]

def click(loc):
    try:
        pydirectinput.click(*loc)
        print("[Debug] click on {},{}".format(loc[0], loc[1]))
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    print("自动打剑脚本设置：模拟器开全屏，使用前先自行寻址到势力地图内。")
    print("启动本脚本后请回到游戏全屏界面，本脚本会自动寻址到目标势力雕像并自动攻击。死亡后会自动回到雕像攻击。每隔固定时间会回交物资。")
    print("本纯绿色脚本由玩家*肝die冲鸭*为您开发")
    screenWidth, screenHeight = pydirectinput.size()
    print("[Debug] Screen resolution: {}x{}".format(screenWidth, screenHeight))
    #input("回车确认，确认后该程序会自动最小化")
    #cur_win = pyautogui.getActiveWindow()
    #cur_win.minimize()
    while True:
        time.sleep(5)
        # 寻址到目标势力
        loc=[int(screenWidth*shili_icon[0]), int(screenHeight*shili_icon[1])]
        click(loc)
        time.sleep(2)
        loc=[int(screenWidth*shili_loc_changle[0]), int(screenHeight*shili_loc_changle[1])]
        click(loc)
        time.sleep(2)
        loc=[int(screenWidth*confirm_loc[0]), int(screenHeight*confirm_loc[1])]
        click(loc)
        time.sleep(60)
        # 寻址到势力雕像
        loc=[int(screenWidth*minimap_loc[0]), int(screenHeight*minimap_loc[1])]
        click(loc)
        time.sleep(2)
        loc=[int(screenWidth*diaoxiang_loc_changle[0]), int(screenHeight*diaoxiang_loc_changle[1])]
        click(loc)
        time.sleep(1)
        loc=[int(screenWidth*close_button[0]), int(screenHeight*close_button[1])]
        click(loc)
        time.sleep(45)
        # 开启自动攻击
        loc=[int(screenWidth*auto_attack[0]), int(screenHeight*auto_attack[1])]
        click(loc)
        time.sleep(1)

        # 定期检查死亡自动寻址
        counter = 0
        while counter < 3000:
            pil_image=ImageGrab.grab()
            image=numpy.array(pil_image)
            gray=image.sum(axis=2)/3.0
            middle_intensity = numpy.percentile(gray[int(screenWidth*0.3):int(screenWidth*0.6), int(screenWidth*0.3):int(screenWidth*0.6)],99)
            print("[Debug] middle area intensity: {}".format(middle_intensity))
            if middle_intensity > 175:
                time.sleep(3)
                counter = counter + 3
                continue
            # 寻址到势力雕像
            time.sleep(30)
            loc=[int(screenWidth*minimap_loc[0]), int(screenHeight*minimap_loc[1])]
            click(loc)
            time.sleep(2)
            loc=[int(screenWidth*diaoxiang_loc_changle[0]), int(screenHeight*diaoxiang_loc_changle[1])]
            click(loc)
            time.sleep(1)
            loc=[int(screenWidth*close_button[0]), int(screenHeight*close_button[1])]
            click(loc)
            time.sleep(30)
            # 开启自动攻击
            #loc=[int(screenWidth*auto_attack[0]), int(screenHeight*auto_attack[1])]
            #click(loc)
            #time.sleep(1)
            counter = counter + 63
        
        # for _ in range(50):
        #     time.sleep(60)
        #     # 寻址到势力雕像
        #     loc=[int(screenWidth*minimap_loc[0]), int(screenHeight*minimap_loc[1])]
        #     click(loc)
        #     time.sleep(2)
        #     loc=[int(screenWidth*diaoxiang_loc_changle[0]), int(screenHeight*diaoxiang_loc_changle[1])]
        #     click(loc)
        #     time.sleep(1)
        #     loc=[int(screenWidth*close_button[0]), int(screenHeight*close_button[1])]
        #     click(loc)
        #     time.sleep(30)
        #     # 开启自动攻击
        #     loc=[int(screenWidth*auto_attack[0]), int(screenHeight*auto_attack[1])]
        #     click(loc)
        #     time.sleep(1)

        # 交物资
        loc=[int(screenWidth*task_loc[0]), int(screenHeight*task_loc[1])]
        click(loc)
        time.sleep(120)
        loc=[int(screenWidth*submit_confirm_loc[0]), int(screenHeight*submit_confirm_loc[1])]
        click(loc)
        time.sleep(1)
        

