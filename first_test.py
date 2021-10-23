# -*- encoding=utf8 -*-
__author__ = "a0973_ecy1f7c"

# 版本 2021/10/22 10:41
# 所有touch前都接了一個wait防止網路問題
# 特殊地方使用try

import csv

from airtest.core.api import *
import tkinter as tk

ST.OPDELAY = 0.3  # 每條步驟間執行間隔
ST.THRESHOLD = 0.7  # 預設臨界值
ST.FIND_TIMEOUT = 15  # wait預設最長等待時間

# auto_setup(__file__,devices=["Android://127.0.0.1:5555"])

dev = connect_device('Android:///')  # 連接到當前連接設備，沒連接設備就註解掉

def test_to_index():  # 前往主頁
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


def test_exp_vent():  # 經驗值冒險關卡 需要傳入瑪娜關卡和經驗值關卡的難度選擇
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
        test_to_index()  # 呼叫回到主頁函式
    else:
        print('expvent is not open')


def test_dungeon():  # 需要有一個傳入值，為地下城難度
    print('地下城')
    #  預想 ， 透過畫面左右會出現的小箭頭還換頁查找，根據傳入的難度給判定是要點左邊箭頭還是右邊箭頭

def test_survey():
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
        test_to_index() # 回到主頁
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
    try:  # 判斷神殿是不是有開啟
        wait(Template(r"prc_survey_temple.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440), rgb=True,
                      threshold=0.8))
        touch(Template(r"prc_survey_temple.PNG", record_pos=(0.027, 0.214), resolution=(3040, 1440)))  # 前往神殿
        test_temple()
    except TargetNotFoundError:
        print('神殿未開啟')  # 如果神殿未開放
        test_to_index()  # 回到主頁
        return


def test_holy():  # 需要有一個傳入值，為聖跡難度
    print('聖跡')


def test_temple():  # 需要有一個傳入值，為神殿難度
    print('神殿')


def test_login(user_number): # user_number用來判斷是第幾個按鈕被點擊
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
                    return
    except FileNotFoundError:  # 如果沒有檔案也會結束
        print('此欄位未存帳號')  # 可以考慮做成彈窗
        return
    try:  # 確定是不是有在登入帳號的畫面，也就是資料連動是不是在畫面上
        wait(Template(r"prc_login_1.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)), timeout=7)
        touch(Template(r"prc_login_1.PNG", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 有資料連動的話就點擊
    except TargetNotFoundError:  # 不在時的錯誤處理 結束函式
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


'''圖形化視窗函式'''


# 視窗排版用的函式
def test_define_layout(obj, cols=1, rows=1):
    def method(trg, col, row):

        for c in range(cols):
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj) == list:
        [method(trg, cols, rows) for trg in obj]
    else:
        trg = obj
        method(trg, cols, rows)


# 註冊賬密視窗
def test_ID_Window(bt_number):  # bt_number用來判斷是第幾個按鈕被點擊
    # 帳密讀取
    var1 = tk.StringVar()
    var2 = tk.StringVar()

    newWindow = tk.Toplevel(div3)
    newWindow.title("註冊")
    newWindow.config(bg="white")
    newWindow.geometry("230x100")
    # 帳密標籤
    lb_id = tk.Label(newWindow, text='帳號', bg='white', fg='#323232')
    lb_ps = tk.Label(newWindow, text='密碼', bg='white', fg='#323232')

    # 帳密Entry
    et_id = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var1)
    et_ps = tk.Entry(newWindow, bg='#323232', fg='white', textvariable=var2)

    # 確認按鈕
    bt_ok = tk.Button(newWindow, text='確認', bg='#323232', fg='white',
                      command=lambda: test_user(var1.get(), var2.get(), bt_number))

    lb_id.grid(column=0, row=0)
    lb_ps.grid(column=0, row=1)

    et_id.grid(column=1, row=0)
    et_ps.grid(column=1, row=1)

    bt_ok.grid(column=1, row=2)


# 按下按鈕後的帳密讀出函式
def test_user(id, ps, btn):  # btn用來判斷是第幾個按鈕被點擊
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
                print('帳密清空')  #可以考慮做成彈窗
                return
        elif btn == '2':
            sigon_2.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_2.config(text='Sign up')
                print('帳密清空')  # 可以考慮做成彈窗
                return
        elif btn == '3':
            sigon_3.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_3.config(text='Sign up')
                print('帳密清空')  # 可以考慮做成彈窗
                return
        elif btn == '4':
            sigon_4.config(text='ID:' + id)  # 設定標籤為ID:
            if id == '' or ps == '':  # 如果ID或密碼沒打就等於清空
                sigon_4.config(text='Sign up')
                print('帳密清空')  # 可以考慮做成彈窗
                return
    print(id, ps)


'''---------------------視窗---------------------'''
window = tk.Tk()
window.title('超異域公主連結自動化控制視窗')

align_mode = 'nswe'
pad = 5

# 視窗分割成三塊分別是div1(左),div2(右上),div3(右下) -> 視窗大小在這調整
div_size = 200
div1_hsize = div_size * 2.5
div3_hsize = div_size * 1.5
div1 = tk.Frame(window, width=div_size, height=div1_hsize, bg='#323232')
div2 = tk.Frame(window, width=div_size, height=div_size, bg='#5e5d5d')
div3 = tk.Frame(window, width=div_size, height=div3_hsize, bg='#5e5d5d')

div1.grid(column=0, row=0, rowspan=2)
div2.grid(column=1, row=0)
div3.grid(column=1, row=1)

window.update()
win_size = min(window.winfo_width(), window.winfo_height())
print(win_size)

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

test_define_layout(window, cols=2, rows=2)
test_define_layout([div1, div2, div3])
'''----------------------------分隔線---以下是按鈕.標籤等物件---------------------------------------------'''

# 註冊登入標籤
sigon_1 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_2 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_3 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')
sigon_4 = tk.Label(div3, text='Sign up', bg='white', fg='#323232')

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
sigon_1.grid(column=0, row=1, sticky=align_mode)
sigon_2.grid(column=0, row=2, sticky=align_mode)
sigon_3.grid(column=0, row=3, sticky=align_mode)
sigon_4.grid(column=0, row=4, sticky=align_mode)
# 註冊按鈕排版
bt_sigon_up_1.grid(column=1, row=1, sticky=align_mode)
bt_sigon_up_2.grid(column=1, row=2, sticky=align_mode)
bt_sigon_up_3.grid(column=1, row=3, sticky=align_mode)
bt_sigon_up_4.grid(column=1, row=4, sticky=align_mode)

# 登入按鈕排版
bt_sigon_in_1.grid(column=2, row=1, sticky=align_mode)
bt_sigon_in_2.grid(column=2, row=2, sticky=align_mode)
bt_sigon_in_3.grid(column=2, row=3, sticky=align_mode)
bt_sigon_in_4.grid(column=2, row=4, sticky=align_mode)

''' 主要執行區塊 '''
dungeon_lv = []  # 地下城難度選擇
exp_vent_lv = []  # 經驗值冒險難度選擇
mana_vent_lv = []  # 瑪那冒險難度選擇
temple_lv = []  # 神殿難度選擇
holy_ly = []  # 聖蹟難度選擇


'''------以下 try 功用為將有註冊過的帳號更新到標籤-----'''

try:
    with open('Account1.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_1.config(text='ID:'+row['Id'])
            if row['Id'] == '':
                sigon_1.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account2.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_2.config(text='ID:'+row['Id'])
            if row['Id'] == '':
                sigon_2.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account3.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_3.config(text='ID:'+row['Id'])
            if row['Id'] == '':
                sigon_3.config(text='Sign up')
except FileNotFoundError:
    pass

try:
    with open('Account4.csv', 'r', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            sigon_4.config(text='ID:'+row['Id'])
            if row['Id'] == '':
                sigon_4.config(text='Sign up')
except FileNotFoundError:
    pass

'''-----註冊過的帳號更新完成-----'''


window.mainloop()
