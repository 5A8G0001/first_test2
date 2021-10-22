import tkinter as tk
#視窗排版用的函式
def define_layout(obj, cols=1, rows=1):
    
    def method(trg, col, row):
        
        for c in range(cols):    
            trg.columnconfigure(c, weight=1)
        for r in range(rows):
            trg.rowconfigure(r, weight=1)

    if type(obj)==list:        
        [ method(trg, cols, rows) for trg in obj ]
    else:
        trg = obj
        method(trg, cols, rows)


#註冊賬密視窗
def ID_Window():
    #帳密讀取
    var1 = tk.StringVar()
    var2 = tk.StringVar()


    newWindow = tk.Toplevel(div3)
    newWindow.title("註冊")
    newWindow.config(bg="white")
    newWindow.geometry("230x100")
    #帳密標籤
    lb_id = tk.Label(newWindow, text='帳號', bg='white', fg='#323232')
    lb_ps = tk.Label(newWindow, text='密碼', bg='white', fg='#323232')

    #帳密Entry
    et_id = tk.Entry(newWindow,bg='#323232',fg='white',textvariable=var1)
    et_ps = tk.Entry(newWindow,bg='#323232',fg='white',textvariable=var2)
    
    #確認按鈕
    bt_ok = tk.Button(newWindow, text='確認', bg='#323232', fg='white',command=lambda: user(var1.get(),var2.get()))

    lb_id.grid(column=0, row=0)
    lb_ps.grid(column=0, row=1)

    et_id.grid(column=1, row=0)
    et_ps.grid(column=1, row=1)

    bt_ok.grid(column=1, row=2)

    
#按下按鈕後的帳密讀出函式
def user(id,ps):
    print(id,ps)


    

    

'''---------------------視窗排版---------------------'''
window = tk.Tk()
window.title('Window')

align_mode = 'nswe'
pad = 5

#視窗分割成三塊分別是div1(左),div2(右上),div3(右下) -> 視窗大小在這調整
div_size = 200
div1_hsize = div_size * 2.5
div3_hsize = div_size * 1.5
div1 = tk.Frame(window,  width=div_size , height=div1_hsize , bg='#323232')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='#5e5d5d')
div3 = tk.Frame(window,  width=div_size , height=div3_hsize , bg='#5e5d5d')

div1.grid(column=0, row=0, rowspan=2)
div2.grid(column=1, row=0)
div3.grid(column=1, row=1)

window.update()
win_size = min( window.winfo_width(), window.winfo_height())
print(win_size)

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

define_layout(window, cols=2, rows=2)
define_layout([div1, div2, div3])
'''----------------------------分隔線---以下是按鈕.標籤等物件---------------------------------------------'''

#註冊登入標籤
sigon_1 = tk.Label(div3, text='sigon up', bg='white', fg='#323232')
sigon_2 = tk.Label(div3, text='sigon up', bg='white', fg='#323232')
sigon_3 = tk.Label(div3, text='sigon up', bg='white', fg='#323232')
sigon_4 = tk.Label(div3, text='sigon up', bg='white', fg='#323232')

#註冊按鈕
bt_sigon_up_1 = tk.Button(div3, text='註冊', bg='#5e5d5d', fg='white',command=ID_Window)
bt_sigon_up_2 = tk.Button(div3, text='註冊', bg='#5e5d5d', fg='white',command=ID_Window)
bt_sigon_up_3 = tk.Button(div3, text='註冊', bg='#5e5d5d', fg='white',command=ID_Window)
bt_sigon_up_4 = tk.Button(div3, text='註冊', bg='#5e5d5d', fg='white',command=ID_Window)

#登入按鈕
bt_sigon_in_1 = tk.Button(div3, text='登入', bg='#5e5d5d', fg='white')
bt_sigon_in_2 = tk.Button(div3, text='登入', bg='#5e5d5d', fg='white')
bt_sigon_in_3 = tk.Button(div3, text='登入', bg='#5e5d5d', fg='white')
bt_sigon_in_4 = tk.Button(div3, text='登入', bg='#5e5d5d', fg='white')






'''-----------物件排版------------'''
#註冊登入標籤排版
sigon_1.grid(column=0, row=1, sticky=align_mode)
sigon_2.grid(column=0, row=2, sticky=align_mode)
sigon_3.grid(column=0, row=3, sticky=align_mode)
sigon_4.grid(column=0, row=4, sticky=align_mode)

#註冊按鈕排版
bt_sigon_up_1.grid(column=1, row=1, sticky=align_mode)
bt_sigon_up_2.grid(column=1, row=2, sticky=align_mode)
bt_sigon_up_3.grid(column=1, row=3, sticky=align_mode)
bt_sigon_up_4.grid(column=1, row=4, sticky=align_mode)

#登入按鈕排版
bt_sigon_in_1.grid(column=2, row=1, sticky=align_mode)
bt_sigon_in_2.grid(column=2, row=2, sticky=align_mode)
bt_sigon_in_3.grid(column=2, row=3, sticky=align_mode)
bt_sigon_in_4.grid(column=2, row=4, sticky=align_mode)












window.mainloop()