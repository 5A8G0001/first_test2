# -*- encoding=utf8 -*-
__author__ = "a0973_ecy1f7c"

from airtest.core.api import *
import tkinter as tk
import csv

ST.OPDELAY = 0.3  # 每條步驟間執行間隔
ST.THRESHOLD = 0.7  # 預設臨界值
ST.FIND_TIMEOUT = 15  # wait預設最長等待時間


# auto_setup(__file__,devices=["Android://127.0.0.1:5555"])

# dev = connect_device('Android:///')  # 連接到當前連接設備


def to_index():  # 前往主頁
    wait(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    touch(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 回到主頁


def test_game_start():  # 把遊戲打開進入主頁之一連串操作
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


def test_exp_vent():  # 經驗值冒險關卡
    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 點擊冒險
    wait(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))
    touch(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))  # 點擊探索
    wait(Template(r"prc_v_e_expvent.png", record_pos=(0.113, -0.034), resolution=(3040, 1440)))  # 等待Exp冒險出現
    if exists(Template(r"prc_v_e_expvent.png", record_pos=(0.113, -0.034), resolution=(3040, 1440))):
        touch(Template(r"prc_v_e_expvent.png"))  # 點擊Exp冒險
        wait(Template(r"prc_v_e_expvent_Lv2.png", record_pos=(0.075, -0.004),
                      resolution=(3040, 1440)))  # 等待選擇Lv ()的Exp冒險
        touch(
            Template(r"prc_v_e_expvent_Lv2.png", record_pos=(0.075, -0.004), resolution=(3040, 1440)))  # 選擇Lv ()的Exp冒險
        wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩兩次
        wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 藍色ok按鈕
        wait(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
        touch(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))  # 繼續前往瑪那冒險
        wait(Template(r"prc_v_e_manavent_Lv2.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
        touch(Template(r"prc_v_e_manavent_Lv2.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))  # 選擇Lv()的瑪那冒險
        wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩兩次
        wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 藍色ok按鈕
        wait(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # 回到探索top
        to_index()  # 呼叫回到主頁函式
    else:
        print('expvent is not open')


def test_dungeon():
    print('地下城')


def test_survey():
    print('調查，判斷聖蹟調查與神殿調查各自有沒有開，有機會跳限定商店，要按白色取消')


def test_holy():
    print('聖蹟')


def test_temple():
    print('神殿')


def login():
    print('登入帳號小幫手')


# 主要值行區塊

# root = tk.Tk()
# root.geometry('500x500')

dungeon_lv = []  # 地下城難度選擇
exp_vent_lv = []  # 經驗值冒險難度選擇
mana_vent_lv = []  # 瑪那冒險難度選擇
temple_lv = []  # 神殿難度選擇
holy_ly = []  # 聖蹟難度選擇
with open('Account.csv', newline='',encoding='utf-8') as csvfile:
    rows = csv.DictReader(csvfile,delimiter=',')

    for row in rows:
        print(row['UserName'],row['Account'],row['Password'])
    csvfile.close()
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

  # 寫入一列資料
    writer.writerow(['UserName', 'Account', 'Password'])

  # 寫入另外幾列資料
    writer.writerow(['院', '12345678', 'password'])
    writer.writerow(['帳號2', '21345678', 'password2'])
    csvfile.close()
# root.mainloop()
