# -*- encoding=utf8 -*-
__author__ = "a0973_ecy1f7c"

from airtest.core.api import *
OPDELAY = 0.5
THRESHOLD = 0.7
#auto_setup(__file__,devices=["Android://127.0.0.1:5555"])

dev = connect_device('Android:///')#連接到雷電模擬器


def test_start():
    touch(Template(r"prc_icon.png", record_pos=(-0.34, -0.202), resolution=(3040, 1440)))
    wait(Template(r"prc_st_menu .png", record_pos=(-0.34, -0.202), resolution=(3040, 1440)))
    touch(Template("prc_st_t.png"))
    wait(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440)))
    if exists(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440))):
        touch(Template(r"prc_st_wt.png", record_pos=(-0.075, 0.087), resolution=(3040, 1440)))
        print(('not wt1'))
    else:
        print('not wt2')
        touch(Template("prc_st_t.png"))
    wait(Template(r"prc_ev_end.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)))
    touch(Template(r"prc_ev_end.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)))
    sleep(2)
    while(exists(Template(r"prc_st_no.png", record_pos=(0.02, 0.184), resolution=(3040, 1440)))):
        touch(Template(r"prc_st_no.png"))
        break
    sleep(3)

def test_expvent():#經驗值冒險關卡
    wait(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    touch(Template(r"prc_main_vent.png", record_pos=(0.027, 0.214), resolution=(3040, 1440)))
    wait(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))
    touch(Template(r"prc_vent_explore.png", record_pos=(0.307, -0.119), resolution=(3040, 1440)))
    sleep(2)
    if (exists(Template(r"prc_v_e_expvent.png", record_pos=(0.113, -0.034), resolution=(3040, 1440)))):
        touch(Template(r"prc_v_e_expvent.png"))
        wait(Template(r"prc_v_e_expvent_Lv2.png", record_pos=(0.075, -0.004), resolution=(3040, 1440)))
        touch(Template(r"prc_v_e_expvent_Lv2.png", record_pos=(0.075, -0.004), resolution=(3040, 1440)))
        wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
        touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩
        wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
        touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # ok按鈕R
        sleep(1)
        wait(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
        touch(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
        #touch(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
    else:
        print('expvent is not open')
#+test_start()#進入遊戲到主畫面
#test_expvent()
#wait(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
#touch(Template(r"前往瑪娜冒險.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
#wait(Template(r"prc_v_e_manavent_Lv2.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
#touch(Template(r"prc_v_e_manavent_Lv2.png", record_pos=(0.018, 0.187), resolution=(3040, 1440)))
#wait(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))
#touch(Template(r"prc_fast_2.png", record_pos=(0.26, 0.056), resolution=(3040, 1440)))  # 確定掃蕩
#wait(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
#touch(Template(r"prc_button_ok.png", record_pos=(0.111, 0.087), resolution=(3040, 1440)))  # ok按鈕R
#wait(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
#touch(Template(r"prc_toexplore_top.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
sleep(1)
wait(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))
touch(Template(r"prc_main_index.PNG", record_pos=(0.111, 0.087), resolution=(3040, 1440)))








