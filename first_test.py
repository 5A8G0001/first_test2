# -*- encoding=utf8 -*-
__author__ = "a0973_ecy1f7c"

# 版本 2021/10/24 00:01
# 所有touch前都接了一個wait防止網路問題
# 特殊地方使用try

import csv
import time
from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# 全域變數
file_path_Label = ""  # 上傳檔案路徑
settings_file = ['不選擇']  # 設定檔名稱
cb_Text = None  # cb元件讀取值
flipA = ""  # 帳號
flipP = ""  # 密碼
time1 = ""  # 日期
time2 = ""  # 時間
from airtest.core.api import *

ST.OPDELAY = 0.3  # 每條步驟間執行間隔
ST.THRESHOLD = 0.7  # 預設臨界值
ST.FIND_TIMEOUT = 15  # wait預設最長等待時間

# auto_setup(__file__,devices=["Android://127.0.0.1:7555"])

dev = connect_device('Android:///')  # 連接到當前連接設備，沒連接設備就註解掉


def test_to_index():  # 前往主頁
    try:
        wait(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 回到主頁
    except TargetNotFoundError:
        test_pop_upwindow('未找到主頁，還是你已經在主頁了呢?')
        return


# 把遊戲打開進入主頁之一連串操作
def test_game_start():
    touch(Template(r"prc_icon.png", record_pos=(-0.34, -0.202), resolution=(3040, 1440)))  # 點擊公主連結開啟遊戲
    wait(Template(r"prc_st_menu .png", record_pos=(-0.34, -0.202), resolution=(3040, 1440)))  # 等待進入到遊戲進入主畫面
    touch(Template("prc_st_t.png"))  # 點擊左下角小圖標
    try:
        wait(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440)))  # 等待確認是否有稍後綁定帳號
    except TargetNotFoundError:
        print('已經綁定帳號')

    if exists(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440))):  # 確認是否有稍後綁定帳號
        touch(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440)))  # 尚未綁定帳號所以點擊稍後綁定帳號
        print('尚未綁定帳號')
    else:
        print('已經綁定帳號')  # 已經綁定帳號所以執行下面一行
        touch(Template("prc_st_t.png"))  # 點擊左下角小圖標
    # 至此已經開使進入遊戲主頁畫面
    wait(Template(r"prc_ev_end.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)))
    touch(Template(r"prc_ev_end.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)))  # 關閉公告
    try:
        wait(Template(r"prc_st_no.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)), timeout=5)  # 等待是否有更多活動
    except TargetNotFoundError:
        print('沒有更多活動')

    while exists(Template(r"prc_st_no.png", record_pos=(0.02, 0.184), resolution=(3040, 1440))):  # 如果有更多活動，關閉
        touch(Template(r"prc_st_no.png"))
        try:
            wait(Template(r"prc_st_no.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)), timeout=5)
            touch(Template(r"prc_st_no.png"))
        except TargetNotFoundError:
            print('沒有更多活動')
            break
    # 正式進入主頁


# 經驗值冒險關卡 需要傳入經驗值關卡的難度選擇
def test_exp_vent():
    print(exp_vent_lv_cbText.get(), "exp_vent_lv_cbText")  # exp_vent_lv_cbText.get() 經驗值冒險關卡傳入的關卡難度  與  "不選擇"

    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    wait(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))
    touch(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))  # 點擊探索
    wait(Template(r"prc_v_e_expvent.png", record_pos=(0.113, -0.034), resolution=(3040, 1440)))  # 等待Exp冒險出現
    touch(Template(r"prc_v_e_expvent.png"))  # 點擊Exp冒險
    try:
        # 等待選擇Lv ()的Exp冒險
        wait(Template(r"exp_" + cb_exp_vent_lv.get() + ".png", record_pos=(0.075, -0.004), resolution=(3040, 1440),
                      rgb=True))
        # 選擇Lv ()的Exp冒險
        touch(Template(r"exp_" + cb_exp_vent_lv.get() + ".png", record_pos=(0.075, -0.004), resolution=(3040, 1440),
                       rgb=True))
    except TargetNotFoundError:
        test_pop_upwindow('經驗值關卡難度選擇錯誤!')
        return
    try:
        wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩兩次
    except TargetNotFoundError:  # 如果有買月卡會有五次掃蕩次數
        wait(Template(r"prc_button_add.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_button_add.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)), duration=5)  # 增加掃蕩次數
        try:
            wait(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
            touch(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩五次
        except TargetNotFoundError:
            test_pop_upwindow('錯誤')
            return
    wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440), rgb=True))
    touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440), rgb=True))  # 藍色ok按鈕
    sleep(2)
    try:
        wait(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(1600, 900), threshold=0.7, rgb=True),
             timeout=7)
        touch(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(1600, 900), threshold=0.7,
                       rgb=True))  # 繼續前往瑪那冒險
        return
    except TargetNotFoundError:
        try:
            wait(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
            touch(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 回到探索top
            return
        except TargetNotFoundError:
            test_pop_upwindow('錯誤')
            return


# 瑪那冒險關卡

def test_mana_vent():
    print(mana_vent_lv_cbText.get(), "mana_vent_lv_cbText")  # mana_vent_lv_cbText.get()瑪娜關卡傳入的關卡難度  與  "不選擇"

    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    wait(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))
    touch(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))  # 點擊探索
    wait(Template(r"prc_v_e_manavent.png", record_pos=(0.113, -0.034), resolution=(3040, 1440)))  # 等待Mana冒險出現
    touch(Template(r"prc_v_e_manavent.png"))  # 點擊Mana冒險
    try:
        # 等待選擇Lv ()的Mana冒險
        wait(Template(r"mana_" + cb_mana_vent_lv.get() + ".png", record_pos=(0.075, -0.004), resolution=(3040, 1440),
                      rgb=True))
        # 選擇Lv ()的Exp冒險
        touch(Template(r"mana_" + cb_mana_vent_lv.get() + ".png", record_pos=(0.075, -0.004), resolution=(3040, 1440),
                       rgb=True))
    except TargetNotFoundError:
        test_pop_upwindow('瑪那關卡難度選擇錯誤!')
        return

    try:
        wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩兩次
    except TargetNotFoundError:  # 如果買月卡會有五次掃蕩次數
        wait(Template(r"prc_button_add.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_button_add.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)), duration=5)  # 增加掃蕩次數
        try:
            wait(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
            touch(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩五次
        except TargetNotFoundError:
            test_pop_upwindow('錯誤')
            return
    wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 藍色ok按鈕
    sleep(2)
    try:
        wait(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 回到探索top
        return
    except TargetNotFoundError:
        wait(Template(r"前往經驗值冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"前往經驗值冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))  # 繼續前往瑪那冒險
        return


# 需要有一個傳入值，為地下城難度
def test_dungeon():
    print(dungeon_lv_cbText.get(),
          cb_dungeon_lv.current())  # dungeon_lv_cbText.get() 傳入的關卡名稱  與  "不選擇", cb_dungeon_lv.current() int  數值從0到7

    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    wait(Template(r"prc_vent_dungeon.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_vent_dungeon.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊地下城
    try:
        wait(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                      resolution=(3040, 1440)), timeout=7)
        touch(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                       resolution=(3040, 1440)))  # 對應難度關卡
    except TargetNotFoundError:
        if cb_dungeon_lv.current() > 3:
            try:
                wait(Template(r"dungeon_b.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
                touch(Template(r"dungeon_b.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 選擇畫面右移

                wait(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                              resolution=(3040, 1440)))
                touch(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                               resolution=(3040, 1440)))  # 對應難度關卡
            except TargetNotFoundError:
                print('n')
                test_pop_upwindow('地下城難度選擇錯誤!')
                test_to_index()
                return
        elif cb_dungeon_lv.current() < 3:
            try:
                wait(Template(r"dungeon_s.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
                touch(Template(r"dungeon_s.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 選擇畫面左移
                wait(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                              resolution=(3040, 1440)))
                touch(Template(r"dungeon_lv" + str(cb_dungeon_lv.current() + 1) + ".png", record_pos=(0.027, 0.214),
                               resolution=(3040, 1440)))  # 對應難度關卡
            except TargetNotFoundError:
                print('n')
                test_pop_upwindow('地下城難度選擇錯誤!')
                test_to_index()
                return
    wait(Template(r"prc_button_jump.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_button_jump.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊跳過
    wait(Template(r"prc_button_w_ok.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_button_w_ok.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊白色ok按鈕


def test_survey():  # 目前未使用 (10/31 0:00)
    print('調查，判斷聖蹟調查與神殿調查各自有沒有開，有機會跳限定商店，要按白色取消')
    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往冒險

    # try防止程式遇到錯誤直接結束

    try:  # 判斷調查是不是有開啟
        wait(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往調查
    except TargetNotFoundError:  # 如果調查未開放
        print('調查未開啟')
        test_to_index()  # 回到主頁
        return
    try:  # 判斷聖跡是不是有開啟
        wait(Template(r"prc_survey_holy.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_survey_holy.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往聖跡
        test_holy()
    except TargetNotFoundError:  # 如果聖跡未開放
        print('聖跡未開啟')
        test_to_index()  # 回到主頁
        return


def test_holy():  # 需要有一個傳入值，為聖跡難度
    print(holy_lv_cbText.get(), "holy_lv_cbText")  # holy_lv_cbText.get() 聖跡難度
    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    try:  # 判斷調查是不是有開啟
        wait(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往調查
    except TargetNotFoundError:  # 如果調查未開放
        test_pop_upwindow('調查未開起')
        test_to_index()  # 回到主頁
        return

    try:  # 判斷聖跡是不是有開啟
        wait(Template(r"prc_survey_holy.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_survey_holy.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True))  # 前往聖跡
    except TargetNotFoundError:
        test_pop_upwindow('聖跡未開啟')  # 如果聖跡未開放
        test_to_index()  # 回到主頁
        return

    try:  # 選擇聖跡難度
        # 等待選擇Lv ()的聖跡調查
        wait(Template(r"holy_" + holy_lv_cbText.get() + ".png", record_pos=(0.284, 0.066), resolution=(1600, 900),
                      threshold=0.8, rgb=True))
        # 選擇Lv ()的聖跡調查
        touch(Template(r"holy_" + holy_lv_cbText.get() + ".png", record_pos=(0.284, 0.066), resolution=(1600, 900),
                       threshold=0.8, rgb=True))
    except TargetNotFoundError:
        test_pop_upwindow('聖跡調查難度選擇錯誤!')
        return
    # 增加掃蕩次數並掃蕩
    try:
        wait(Template(r"prc_button_add.png", record_pos=(0.284, 0.056), resolution=(1600, 900)))
        touch(Template(r"prc_button_add.png", record_pos=(0.284, 0.056), resolution=(1600, 900)), duration=4)  # 增加掃蕩次數
        wait(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩五次
    except TargetNotFoundError:
        test_pop_upwindow('錯誤')
        return
    wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 藍色ok按鈕
    wait(Template(r"prc_button_w_ok.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_button_w_ok.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色ok按鈕
    # 按下所有取消按紐
    try:
        wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
        sleep(1)
        wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
        return
    except TargetNotFoundError:
        try:
            sleep(1)
            wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
            touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
            return
        except TargetNotFoundError:
            # test_pop_upwindow('意外')
            return


def test_temple():  # 需要有一個傳入值，為神殿難度
    print(temple_lv_cbText.get(), "temple_lv_cbText")  # temple_lv_cbText.get() 傳入的神殿難度
    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    try:  # 判斷調查是不是有開啟
        wait(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_vent_survey.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往調查
    except TargetNotFoundError:  # 如果調查未開放
        test_pop_upwindow('調查未開起')
        test_to_index()  # 回到主頁
        return

    try:  # 判斷神殿是不是有開啟
        wait(Template(r"prc_survey_temple.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_survey_temple.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True))  # 前往神殿
    except TargetNotFoundError:
        test_pop_upwindow('神殿未開啟')  # 如果神殿未開放
        test_to_index()  # 回到主頁
        return

    try:  # 選擇神殿難度
        # 等待選擇Lv ()的神殿調查
        wait(Template(r"temple_" + temple_lv_cbText.get() + ".png", record_pos=(0.284, 0.066), resolution=(1600, 900)))
        # 選擇Lv ()的神殿調查
        touch(Template(r"temple_" + temple_lv_cbText.get() + ".png", record_pos=(0.284, 0.066), resolution=(1600, 900)))
    except TargetNotFoundError:
        test_pop_upwindow('神殿調查難度選擇錯誤!')
        return
    # 增加掃蕩次數並掃蕩
    try:
        wait(Template(r"prc_button_add.png", record_pos=(0.284, 0.056), resolution=(1600, 900)))
        touch(Template(r"prc_button_add.png", record_pos=(0.284, 0.056), resolution=(1600, 900)), duration=4)  # 增加掃蕩次數
        wait(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_5.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩五次
    except TargetNotFoundError:
        test_pop_upwindow('錯誤')
        return
    wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 藍色ok按鈕
    wait(Template(r"prc_button_w_ok.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_button_w_ok.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色ok按鈕
    # 按下所有取消按紐
    try:
        wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
        sleep(1)
        wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
        return
    except TargetNotFoundError:
        try:
            sleep(1)
            wait(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)), timeout=7)
            touch(Template(r"prc_st_no.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 白色no按鈕
            return
        except TargetNotFoundError:
            # test_pop_upwindow('意外')
            return


def test_login(user_number):  # user_number用來判斷是第幾個按鈕被點擊
    id = ''  # ID
    ps = ''  # 密碼

    try:
        with open('Account' + user_number + '.csv', 'r', newline='') as csvfile:  # 根據點擊的登入按鈕開啟存放帳密的檔案
            rows = csv.DictReader(csvfile)  # 將檔案內容依照欄位讀取出來
            # 下面迴圈式將欄位內容存到id ps內
            for row in rows:
                id = row['Id']
                ps = row['Password']
                if row['Id'] == '' or row['Password'] == '':  # 如果沒有存東西會結束
                    print('此欄位未存帳號')  # 可以考慮做成彈窗
                    test_pop_upwindow('此欄位未存帳號')
                    return
    except FileNotFoundError:  # 如果沒有檔案也會結束
        test_pop_upwindow('此欄位未存帳號')
        print('此欄位未存帳號')  # 可以考慮做成彈窗
        return

    try:  # 確定是不是有在登入帳號的畫面，也就是資料連動是不是在畫面上
        wait(Template(r"prc_login_1.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_login_1.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 有資料連動的話就點擊
    except TargetNotFoundError:  # 不在時的錯誤處理 結束函式
        test_pop_upwindow('不在登入帳號畫面')
        print('不在登入帳號畫面')  # 可以考慮幫我做成彈窗
        return
    #  以下是整個過程
    wait(Template(r"prc_login_2.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
    touch(Template(r"prc_login_2.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 點擊帳號引繼
    wait(Template(r"prc_login_3.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
    touch(Template(r"prc_login_3.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 點擊進入輸入帳號密碼頁面
    wait(Template(r"prc_login_id.png", record_pos=(-0.001, -0.075), resolution=(1600, 900)))
    touch(Template(r"prc_login_id.png", record_pos=(-0.001, -0.075), resolution=(1600, 900)))  # 點擊ID輸入框
    sleep(1)
    text(id, enter=False)  # 輸入ID ， 這要在手機上，且手機有yosemite軟體
    wait(Template(r"prc_login_4.png", record_pos=(0.001, -0.149), resolution=(1600, 900)))
    touch(Template(r"prc_login_4.png", record_pos=(0.001, -0.149), resolution=(1600, 900)))
    sleep(2)
    wait(Template(r"prc_login_ps.png", record_pos=(-0.002, 0.01), resolution=(1600, 900)))
    touch(Template(r"prc_login_ps.png", record_pos=(-0.002, 0.01), resolution=(1600, 900)))  # 點擊密碼輸入框
    sleep(1)
    text(ps, enter=False)  # 輸入密碼 ， 這要在手機上，且手機有yosemite軟體
    wait(Template(r"prc_login_4.png", record_pos=(0.001, -0.149), resolution=(1600, 900)))
    touch(Template(r"prc_login_4.png", record_pos=(0.001, -0.149), resolution=(1600, 900)))
    sleep(2)
    wait(Template(r"prc_button_ok.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
    touch(Template(r"prc_button_ok.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 按下ok

    print('登入帳號小幫手完成')  # 可以考慮幫我做成彈窗


def test_main():
    if cb_dungeon_lv.get() != '不選擇':
        test_dungeon()
        test_to_index()
        test_pop_upwindow('地下城自動結束')
        sleep(3)
    if cb_exp_vent_lv.get() != '不選擇':
        test_exp_vent()
        test_to_index()
        test_pop_upwindow('經驗值冒險自動結束')
        sleep(3)
    if cb_mana_vent_lv.get() != '不選擇':
        test_mana_vent()
        test_to_index()
        test_pop_upwindow('瑪那冒險自動結束')
        sleep(3)
    if temple_lv_cbText.get() != '不選擇':
        test_temple()
        test_to_index()
        test_pop_upwindow('神殿調查自動結束')
        sleep(3)
    if holy_lv_cbText.get() != '不選擇':
        test_holy()
        test_to_index()
        test_pop_upwindow('聖跡調查自動結束')





def test_lodding(div1):
    driver = Chrome(executable_path='chromedriver_win32\chromedriver.exe')  # 提供chromedriver路徑

    to_FlipClass = 'https://flipclass.stust.edu.tw/'  # flipclass網址
    to_google = 'https://www.google.com/'

    driver.get(to_FlipClass)  # 使用瀏覽器開啟網址

    login_Account = driver.find_element_by_name("account")  # 找到帳號標籤
    login_Account.send_keys(flipA)  # 輸入帳號
    login_Password = driver.find_element_by_name("password")  # 找到密碼標籤
    login_Password.send_keys(flipP)  # 輸入密碼
    login_Password.send_keys(Keys.ENTER)  # 在密碼輸入盒按Enter


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='text-right fs-small']//span[text()='more']"))).click()  # 可以省略到只有span  # 點取more

    tab = driver.find_element_by_id('recentEventTable')
    tab_html = tab.get_attribute('outerHTML')
    tab_dfs = pd.read_html(tab_html)
    # soup = pd.read_html(driver.find_element_by_id('recentEventTable').get_attribute('outerHTMK'))[0]
    df = tab_dfs[0]
    df.columns = ["標題", "來源", "期限"]
    test_display_hw(df, div1)
'''圖形化視窗函式'''


# flipclass主視窗
def test_FlipClass_window(oldwindow, a, p):
    if a.get() == "" or p.get() == "":
        return
    global flipA
    global flipP
    flipA = a.get()
    flipP = p.get()

    oldwindow.destroy()

    newWindow = tk.Toplevel(window)
    newWindow.attributes("-topmost",True)
    newWindow.config(bg="white")
    newWindow.title("FlipClass")
    newWindow.iconbitmap("stust.ico")
    newWindow.geometry("450x250")
    newWindow.resizable(0, 0)

    div1 = tk.Frame(newWindow, width=150, height=300, bg='#323232')
    div2 = tk.Frame(newWindow, width=300, height=300, bg='white')

    div1.grid(column=0, row=0)
    div2.grid(column=1, row=0)

    # 數值讀取
    var1 = tk.StringVar()  # 作業名稱Entry值
    NradioValue_hw_choose = tk.IntVar()  # 作業 固定是0 不固定是1 要用.get()
    TradioValue_hw_choose = tk.IntVar()  # 作業 自動是0 排程是1

    # 登出鍵
    bt_logout = tk.Button(newWindow, text='登出', bg='white', fg='#323232',
                          command=lambda: test_flipclass_ID_Window(newWindow))
    # 新增設定鍵
    bt_settings = tk.Button(newWindow, text='新增設定', bg='#323232', fg='white',
                            command=lambda: test_FlipClass_settings_window(var1, div1, c=1))
    # 檔案選擇鍵
    bt_file = tk.Button(newWindow, text='檔案選擇', bg='#323232', fg='white',
                        command=lambda: test_FlipClass_bt_file(newWindow))

    # 執行鍵
    bt_go = tk.Button(newWindow, text='執行', bg='white', fg='#323232',
                      command=lambda: test_FlipClass_bt_go(var1.get(), NradioValue_hw_choose.get(),
                                                           TradioValue_hw_choose.get(), file_path_Label,div1))

    # 刪除設定鍵
    bt_del_settings = tk.Button(newWindow, text='刪除設定', bg='#323232', fg='white',
                                command=lambda: test_del_settings(var1, div1, c=None))

    lb_id = tk.Label(newWindow, text=flipA, bg='#323232', fg='white')
    lb_id.place(x=10, y=10)

    # 排版
    bt_logout.place(x=100, y=10)
    bt_settings.place(x=185, y=150)
    bt_file.place(x=350, y=150)
    bt_go.place(x=55, y=150)
    bt_del_settings.place(x=250, y=150)

    # 作業標籤
    lb_hw = tk.Label(newWindow, text='作業', bg='white', font='Arial', fg='#323232')
    lb_hw.place(x=200, y=10)

    lb_hw_n = tk.Label(newWindow, text='名稱', bg='white', fg='#323232')
    lb_hw_n.place(x=200, y=60)
    lb_hw_t = tk.Label(newWindow, text='方式', bg='white', fg='#323232')
    lb_hw_t.place(x=320, y=60)

    # 作業名稱Entry
    et_hw = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var1)
    et_hw.place(x=245, y=12)
    # 作業Radiobutton是否固定名稱
    Nrd_hw_choose1 = tk.Radiobutton(newWindow, text='固定', bg='white',
                                    variable=NradioValue_hw_choose, value=0)
    Nrd_hw_choose2 = tk.Radiobutton(newWindow, text='不固定', bg='white',
                                    variable=NradioValue_hw_choose, value=1)
    Nrd_hw_choose1.place(x=200, y=80)
    Nrd_hw_choose2.place(x=200, y=100)

    # 作業Radiobutton 繳交方式(自動或輸入時間)
    Trd_hw_choose1 = tk.Radiobutton(newWindow, text='自動繳交', bg='white',
                                    variable=TradioValue_hw_choose, value=0)
    Trd_hw_choose2 = tk.Radiobutton(newWindow, text='排程繳交', bg='white',
                                    variable=TradioValue_hw_choose, value=1,
                                    command=lambda: test_Trd_hw_choose(div2,newWindow))
    Trd_hw_choose1.place(x=320, y=80)
    Trd_hw_choose2.place(x=320, y=100)

    cb_Text = tk.StringVar()
    cb = ttk.Combobox(div1, textvariable=cb_Text, state='readonly', width=7)
    cb['values'] = settings_file
    cb.current(0)
    cb.place(x=40, y=70)

    test_lodding(div1)





# 刪除設定
def test_del_settings(var1, div1, c):
    global settings_file
    global cb_Text
    if cb_Text == '不選擇':
        return
    if cb_Text.get() in settings_file:
        settings_file.remove(cb_Text.get())
    print(cb_Text.get())
    print(settings_file)

    test_FlipClass_settings_window(var1, div1, c)


# flipclass主視窗開始執行按鈕
def test_FlipClass_bt_go(hw_name, name_type, time_type, path,div1):
    global flipA,flipP,time1,time2
    print(hw_name, name_type, time_type, path)
    # 基本上傳完成
    driver = Chrome(executable_path='chromedriver_win32\chromedriver.exe')  # 提供chromedriver路徑

    to_FlipClass = 'https://flipclass.stust.edu.tw/'  # flipclass網址
    to_google = 'https://www.google.com/'

    driver.get(to_FlipClass)  # 使用瀏覽器開啟網址

    login_Account = driver.find_element_by_name("account")  # 找到帳號標籤
    login_Account.send_keys(flipA)  # 輸入帳號
    login_Password = driver.find_element_by_name("password")  # 找到密碼標籤
    login_Password.send_keys(flipP)  # 輸入密碼
    login_Password.send_keys(Keys.ENTER)  # 在密碼輸入盒按Enter
    work = hw_name  # 作業名稱
    # /course/homework/課程編號(29396) span[text()='作業名稱']

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='text-right fs-small']//span[text()='more']"))).click()  # 可以省略到只有span  # 點取more

    tab = driver.find_element_by_id('recentEventTable')
    tab_html = tab.get_attribute('outerHTML')
    tab_dfs = pd.read_html(tab_html)
    # soup = pd.read_html(driver.find_element_by_id('recentEventTable').get_attribute('outerHTMK'))[0]
    df = tab_dfs[0]
    df.columns = ["標題", "來源", "期限"]
    #test_display_hw(df,div1)

    '''WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='text']//span[text()='%s']" % work))).click()  # 可以省略到只有span  # 點取作業名稱的作業
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='text-center fs-margin-default']//span[text()='交作業']"))).click()  # 進入交作業畫面

    driver.switch_to.frame(driver.find_element_by_class_name('fs-modal-iframe'))  # 交作業畫面為一個內嵌的iframe 要 switch到裡面

    path1 = path  # 要上傳的檔案的絕對路徑

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="上傳檔案"]'))).click()  # 點擊上傳檔案按鈕

    time.sleep(2)

    driver.find_element_by_name('files[]').send_keys(path1)  # 因為學校上傳檔案的方式是input，故可以直接send_keys(路徑)
    time.sleep(5)  # 不可在上傳過程中做其他事
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close'))).click()  # 關閉上傳畫面
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="media-edit-form"]/div[7]/div/button[1]/span'))).click()  # 繳交 ， 同時可能會離開iframe
'''

def test_display_hw(df,div1):
    '''newWindow = tk.Toplevel(window)
    newWindow.iconbitmap("stust.ico")
    newWindow.title("作業顯示")
    newWindow.config(bg="white")
    newWindow.geometry("720x480+10+50")
    newWindow.resizable(0, 0)'''
    global settings_file
    global cb_Text
    cb_Text = tk.StringVar()  # cb元件讀取值(檔案選擇)
    lb_1=[]
    lb_2=[]
    lb_3=[]


    for x in df["標題"]:
        settings_file.append(x)
        print(x)

    cb = ttk.Combobox(div1, textvariable=cb_Text, state='readonly', width=15)
    cb['values'] = settings_file
    cb.current(0)
    cb.place(x=10, y=70)


'''
    df_sum = 0
    for i in df["標題"]:
        lb_1.append(tk.Label(newWindow, text='%s'%i, bg='white', fg='black'))
        lb_1[df_sum].grid(column=0, row=df_sum)
        df_sum+=1

    df_sum = 0
    for i in df["來源"]:
        lb_2.append(tk.Label(newWindow, text='%s'%i, bg='white', fg='black'))
        lb_2[df_sum].grid(column=1, row=df_sum)
        df_sum+=1

    df_sum = 0
    for i in df["期限"]:
        lb_3.append(tk.Label(newWindow, text='%s'%i, bg='white', fg='black'))
        lb_3[df_sum].grid(column=2, row=df_sum)
        df_sum+=1
'''



# 設定
def test_FlipClass_settings_window(var1, div1, c):
    global settings_file
    global cb_Text
    cb_Text = tk.StringVar()  # cb元件讀取值(檔案選擇)
    if c != None:
        if var1.get() != '':
            settings_file.append(var1.get())
    print(settings_file)

    cb = ttk.Combobox(div1, textvariable=cb_Text, state='readonly', width=7)
    cb['values'] = settings_file
    cb.current(0)
    cb.place(x=40, y=70)


# 檔案開啟
def test_FlipClass_bt_file(newWindow):
    newWindow.attributes("-topmost", False)
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    file_path = ''
    file_path = filedialog.askopenfilename()
    print((file_path))
    global file_path_Label
    file_path_Label = file_path
    tk.Label(newWindow, text='                                                                                                     ', bg='white', fg='white').place(x=170, y=200)
    tk.Label(newWindow, text='%s' % file_path_Label, bg='#323232', fg='white').place(x=170, y=200)
    root.attributes("-topmost", False)
    newWindow.attributes("-topmost", True)

# 排程時間設定
def test_Trd_hw_choose(div2,oldWindow):
    # 時間讀取
    var1 = tk.StringVar()  # 日期
    var2 = tk.StringVar()  # 時間
    oldWindow.attributes("-topmost", False)


    newWindow = tk.Toplevel(div2)
    newWindow.title("時間設定")
    newWindow.config(bg="white")
    newWindow.geometry("200x100")
    newWindow.resizable(0, 0)
    newWindow.attributes("-topmost", True)

    # 標籤
    lb_t1 = tk.Label(newWindow, text='日期', bg='white', fg='#323232')
    lb_t2 = tk.Label(newWindow, text='時間', bg='white', fg='#323232')

    tk.Label(newWindow, text=' ', bg='white', fg='#323232').grid(column=1, row=2)

    # Entry
    et_id = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var1)
    et_ps = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var2)

    # 確認按鈕
    bt_ok = tk.Button(newWindow, text='OK', bg='#323232', fg='white',
                      command=lambda: test_Trd_hw_choose_OK(newWindow, var1, var2))

    lb_t1.grid(column=0, row=0)
    lb_t2.grid(column=0, row=1)

    et_id.grid(column=1, row=0)
    et_ps.grid(column=1, row=1)

    bt_ok.grid(column=1, row=3)


# 排程時間設定的確定按鈕事件
def test_Trd_hw_choose_OK(oldwindow, var1, var2):
    # 關閉排程時間設定視窗
    oldwindow.destroy()

    global time1, time2
    time1 = var1.get()
    time2 = var2.get()
    print(var1.get(), var2.get())
    print(time.strftime("%Y-%m-%d %H:%M", time.localtime()))


# flipclass登入視窗
def test_flipclass_ID_Window(oldwindow):
    global file_path_Label, settings_file, cb_Text, flipA, flipP, time1, time2

    if oldwindow != None:
        # 初始化
        file_path_Label = ""
        settings_file = ['不選擇']
        cb_Text = None
        flipA = ""
        flipP = ""
        time1 = ""
        time2 = ""
        # 關閉Flip主視窗
        oldwindow.destroy()

    # 帳密讀取
    var1 = tk.StringVar()
    var2 = tk.StringVar()

    newWindow = tk.Toplevel(div2)
    newWindow.title("FlipClass登入")
    newWindow.config(bg="white")
    newWindow.geometry("200x100")
    newWindow.resizable(0, 0)
    # 帳密標籤
    lb_id = tk.Label(newWindow, text='帳號', bg='white', fg='#323232')
    lb_ps = tk.Label(newWindow, text='密碼', bg='white', fg='#323232')
    tk.Label(newWindow, text=' ', bg='white', fg='#323232').grid(column=1, row=2)

    # 帳密Entry
    et_id = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var1)
    et_ps = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var2, show='*')

    # 確認按鈕
    bt_ok = tk.Button(newWindow, text='登入', bg='#323232', fg='white',
                      command=lambda: test_FlipClass_window(newWindow, var1, var2))

    lb_id.grid(column=0, row=0)
    lb_ps.grid(column=0, row=1)

    et_id.grid(column=1, row=0)
    et_ps.grid(column=1, row=1)

    bt_ok.grid(column=1, row=3)



# 註冊賬密視窗
def test_ID_Window(bt_number):  # bt_number用來判斷是第幾個按鈕被點擊
    # 帳密讀取
    var1 = tk.StringVar()
    var2 = tk.StringVar()

    newWindow = tk.Toplevel(div3)
    newWindow.title("註冊")
    newWindow.config(bg="white")
    newWindow.geometry("200x100")
    newWindow.resizable(0, 0)
    # 帳密標籤
    lb_id = tk.Label(newWindow, text='帳號', bg='white', fg='#323232')
    lb_ps = tk.Label(newWindow, text='密碼', bg='white', fg='#323232')

    # 帳密Entry
    et_id = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var1)
    et_ps = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var2)
    tk.Label(newWindow, text=' ', bg='white', fg='#323232').grid(column=1, row=2)

    # 確認按鈕
    bt_ok = tk.Button(newWindow, text='確認', bg='#323232', fg='white',
                      command=lambda: test_user(var1.get(), var2.get(), bt_number, newWindow))

    lb_id.grid(column=0, row=0)
    lb_ps.grid(column=0, row=1)

    et_id.grid(column=1, row=0)
    et_ps.grid(column=1, row=1)

    bt_ok.grid(column=1, row=3)


# 按下按鈕後的帳密讀出函式
def test_user(id, ps, btn, oldwindow):  # btn用來判斷是第幾個按鈕被點擊
    oldwindow.destroy()
    with open('Account' + btn + '.csv', 'w', newline='') as csvfile:  # 寫入模式，如果檔案已存在會覆寫
        fieldnames = ['Id', 'Password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 設定欄位
        writer.writeheader()
        writer.writerow({'Id': id, 'Password': ps})  # 讀兩個欄位的資料
        csvfile.close()
        #  根據按下是第幾個按鈕來判斷要設定哪個標籤為ID
        if btn == '1':
            sigon_1.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_1.config(text='Sign up')
                test_pop_upwindow('帳密清空')
                print('帳密清空')  # 可以考慮做成彈窗
                return
        elif btn == '2':
            sigon_2.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_2.config(text='Sign up')
                test_pop_upwindow('帳密清空')
                print('帳密清空')  # 可以考慮做成彈窗
                return
        elif btn == '3':
            sigon_3.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_3.config(text='Sign up')
                test_pop_upwindow('帳密清空')
                print('帳密清空')  # 可以考慮做成彈窗
                return
        elif btn == '4':
            sigon_4.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_4.config(text='Sign up')
                test_pop_upwindow('帳密清空')
                print('帳密清空')  # 可以考慮做成彈窗
                return
    print(id, ps)

def test_get_homework():
    pass


# 彈窗
def test_pop_upwindow(str):
    newWindow = tk.Toplevel(window)
    newWindow.iconbitmap("pop_kokoro.ico")
    newWindow.title("溫馨小提示 (:3 」∠ )_")
    newWindow.config(bg="white")
    newWindow.geometry("330x170+10+50")
    newWindow.resizable(0, 0)
    lb_1 = tk.Label(newWindow, text=str, bg='white', fg='black')
    lb_2 = tk.Label(newWindow, text=str, bg='white', fg='black')

    lb_1.grid(column=1, row=1)
    lb_2.grid(column=1, row=2)

    '''改變grid和text多加一點空白能排版
    tk.Label(newWindow, text='', bg='white', fg='white').grid(column=1, row=0)
    tk.Label(newWindow, text='', bg='white', fg='white').grid(column=0, row=1)
    '''


'''---------------------視窗---------------------'''
window = tk.Tk()

window.title('超異域公主連結自動化控制視窗')

window.resizable(0, 0)

window.iconbitmap("prc_test_icon1.ico")
align_mode = 'nswe'
pad = 5

# 視窗分割成三塊分別是div1(左),div2(右上),div3(右下) -> 視窗大小在這調整
div_size = 200
div1_hsize = div_size * 2.5
div3_hsize = div_size * 1.5
div1 = tk.Frame(window, width=div_size, height=div1_hsize, bg='#323232')
div2 = tk.Frame(window, width=div_size, height=div_size, bg='#5e5d5d')
div3 = tk.Frame(window, width=div_size, height=div3_hsize, bg='white')

div1.grid(column=0, row=0, rowspan=2)
div2.grid(column=1, row=0)
div3.grid(column=1, row=1)

window.update()
win_size = min(window.winfo_width(), window.winfo_height())
print(win_size)
div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)
test_pop_upwindow('請選擇自己已經通關過的難度!!並確保每日掃蕩次數未消耗\n經驗值與瑪那冒險請選擇"已開放掃蕩之最高進度"')
'''div3'''
'''----------------------------分隔線---以下是按鈕.標籤等物件---------------------------------------------'''

# 註冊登入標籤
sigon_1 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_2 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_3 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_4 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')

REDIVE_png = tk.PhotoImage(file="REDIVE.png")
imgLabel = tk.Label(div3, image=REDIVE_png)
imgLabel.grid(column=0, row=0)

# 註冊按鈕
bt_sigon_up_1 = tk.Button(div3, text='註冊', bg='#ffffff', fg='black', command=lambda: test_ID_Window('1'))  # 傳入按鈕編號
bt_sigon_up_2 = tk.Button(div3, text='註冊', bg='#ffffff', fg='black', command=lambda: test_ID_Window('2'))
bt_sigon_up_3 = tk.Button(div3, text='註冊', bg='#ffffff', fg='black', command=lambda: test_ID_Window('3'))
bt_sigon_up_4 = tk.Button(div3, text='註冊', bg='#ffffff', fg='black', command=lambda: test_ID_Window('4'))

# 登入按鈕
bt_sigon_in_1 = tk.Button(div3, text='登入', bg='#ffffff', fg='black', command=lambda: test_login('1'))
bt_sigon_in_2 = tk.Button(div3, text='登入', bg='#ffffff', fg='black', command=lambda: test_login('2'))
bt_sigon_in_3 = tk.Button(div3, text='登入', bg='#ffffff', fg='black', command=lambda: test_login('3'))
bt_sigon_in_4 = tk.Button(div3, text='登入', bg='#ffffff', fg='black', command=lambda: test_login('4'))

'''-----------物件排版------------'''
# 註冊登入標籤排版
tk.Label(div3, text='                     ', bg='white', fg='white').grid(column=1, row=1)
tk.Label(div3, text=' ', bg='white', fg='white').grid(column=3, row=1)

sigon_1.grid(column=0, row=1, sticky=align_mode)
sigon_2.grid(column=0, row=2, sticky=align_mode)
sigon_3.grid(column=0, row=3, sticky=align_mode)
sigon_4.grid(column=0, row=4, sticky=align_mode)
# 註冊按鈕排版
bt_sigon_up_1.grid(column=2, row=1, sticky=align_mode)
bt_sigon_up_2.grid(column=2, row=2, sticky=align_mode)
bt_sigon_up_3.grid(column=2, row=3, sticky=align_mode)
bt_sigon_up_4.grid(column=2, row=4, sticky=align_mode)

# 登入按鈕排版
bt_sigon_in_1.grid(column=4, row=1, sticky=align_mode)
bt_sigon_in_2.grid(column=4, row=2, sticky=align_mode)
bt_sigon_in_3.grid(column=4, row=3, sticky=align_mode)
bt_sigon_in_4.grid(column=4, row=4, sticky=align_mode)
'''div2'''
# FlipClass按鈕
bt_flipclass = tk.Button(div2, text='FlipClass', bg='white', fg='black', command=lambda: test_flipclass_ID_Window(None))
bt_flipclass.place(x=10, y=10)

'''div1'''
''' 主要執行區塊 '''

# 地下城下拉式選單
lb_dungeon_lv = tk.Label(div1, text='地下城難度', bg='#323232', fg='white')

dungeon_lv_cbText = tk.StringVar()
cb_dungeon_lv = ttk.Combobox(div1, textvariable=dungeon_lv_cbText, state='readonly', width=7)
cb_dungeon_lv['values'] = ['雲海山脈', '密林大樹', '斷崖遺跡', '蒼海孤塔', '毒瘴闇稜', '綠龍骸嶺', '天上浮游城', '不選擇']
cb_dungeon_lv.current(7)
# cb_dungeon_lv.bind('<<ComboboxSelected>>', test_dungeon)

# 地下城排版
tk.Label(div1, text=' ', bg='#323232', fg='#323232').grid(column=0, row=0)
tk.Label(div1, text=' ', bg='#323232', fg='#323232').grid(column=3, row=0)

lb_dungeon_lv.grid(column=1, row=0)
cb_dungeon_lv.grid(column=1, row=1)

# 經驗值冒險下拉式選單
lb_exp_vent_lv = tk.Label(div1, text='經驗值冒險難度', bg='#323232', fg='white')

exp_vent_lv_cbText = tk.StringVar()
cb_exp_vent_lv = ttk.Combobox(div1, textvariable=exp_vent_lv_cbText, state='readonly', width=7)
cb_exp_vent_lv['values'] = ['LV1', 'LV2', 'LV3', 'LV4', 'LV5', 'LV6', 'LV7', 'LV8', 'LV9', 'LV10', 'LV11', '不選擇']
cb_exp_vent_lv.current(11)
# cb_exp_vent_lv.bind('<<ComboboxSelected>>', test_exp_vent)

# 經驗值冒險排版

lb_exp_vent_lv.grid(column=1, row=2)
cb_exp_vent_lv.grid(column=1, row=3)

# 瑪那冒險下拉式選單
lb_mana_vent_lv = tk.Label(div1, text='瑪那冒險難度', bg='#323232', fg='white')

mana_vent_lv_cbText = tk.StringVar()
cb_mana_vent_lv = ttk.Combobox(div1, textvariable=mana_vent_lv_cbText, state='readonly', width=7)
cb_mana_vent_lv['values'] = ['LV1', 'LV2', 'LV3', 'LV4', 'LV5', 'LV6', 'LV7', 'LV8', 'LV9', 'LV10', 'LV11', '不選擇']
cb_mana_vent_lv.current(11)
# cb_mana_vent_lv.bind('<<ComboboxSelected>>', test_exp_vent)

# 瑪那冒險排版

lb_mana_vent_lv.grid(column=1, row=4)
cb_mana_vent_lv.grid(column=1, row=5)

# 神殿下拉式選單
lb_temple_lv = tk.Label(div1, text='神殿難度', bg='#323232', fg='white')

temple_lv_cbText = tk.StringVar()
cb_temple_lv = ttk.Combobox(div1, textvariable=temple_lv_cbText, state='readonly', width=7)
cb_temple_lv['values'] = ['LV1', 'LV2', '不選擇']
cb_temple_lv.current(2)
# cb_temple_lv.bind('<<ComboboxSelected>>', test_temple)

# 神殿排版

lb_temple_lv.grid(column=1, row=6)
cb_temple_lv.grid(column=1, row=7)

# 聖跡下拉式選單
lb_holy_lv = tk.Label(div1, text='聖跡難度', bg='#323232', fg='white')

holy_lv_cbText = tk.StringVar()
cb_holy_lv = ttk.Combobox(div1, textvariable=holy_lv_cbText, state='readonly', width=7)
cb_holy_lv['values'] = ['LV1', 'LV2', 'LV3', '不選擇']
cb_holy_lv.current(3)
# cb_holy_lv.bind('<<ComboboxSelected>>', test_holy)

# 聖跡排版

lb_holy_lv.grid(column=1, row=8)
cb_holy_lv.grid(column=1, row=9)

# 開始按鈕
cpi = tk.PhotoImage(file="main.PNG")
start = tk.Button(div1, image=cpi, command=test_main)

# 開始按鈕排版
tk.Label(div1, text=' ', bg='#323232', fg='#323232').grid(column=1, row=12)
start.grid(column=1, row=13)

'''------以下 try 功用為將有註冊過的帳號更新到標籤-----'''

try:
    with open('Account1.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_1.config(text='ID:' + row['Id'])
            if row['Id'] == '':
                sigon_1.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account2.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_2.config(text='ID:' + row['Id'])
            if row['Id'] == '':
                sigon_2.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account3.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_3.config(text='ID:' + row['Id'])
            if row['Id'] == '':
                sigon_3.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account4.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_4.config(text='ID:' + row['Id'])
            if row['Id'] == '':
                sigon_4.config(text='Sign up')
except FileNotFoundError:
    pass

'''-----註冊過的帳號更新完成-----'''

window.mainloop()