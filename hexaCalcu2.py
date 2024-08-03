import tkinter as tk
from datetime import datetime
import json
import os

#資料
skillLevel = [0,30,35,40,45,50,55,60,65,200,80,90,100,110,120,130,140,150,160,350,170,180,190,200,210,220,230,240,250,500,0]
masterLevel = [50,15,18,20,23,25,28,30,33,100,40,45,50,55,60,65,70,75,80,175,85,90,95,100,105,110,115,120,125,250,0]
enhancementLevel = [75,23,27,30,34,38,42,45,49,150,60,68,75,83,90,98,105,113,120,263,128,135,143,150,158,165,173,180,188,375,0]
commonLevel = [125,38,44,50,57,63,69,75,82,300,110,124,138,152,165,179,193,207,220,525,234,248,262,275,289,303,317,330,344,750,0]
all_skill_frags = sum(skillLevel)
all_master_frags = sum(masterLevel) 
all_enhance_frags = sum(enhancementLevel)
all_common_frags = sum(commonLevel)
allFrag = all_skill_frags+all_master_frags*2+all_enhance_frags*4+all_common_frags
noCommonAllFrag = all_skill_frags+all_master_frags*2+all_enhance_frags*4

#視窗
win = tk.Tk()
win.title('六轉碎片進度計算機')
#win.iconbitmap('icon.ico')
#win.iconbitmap('F:\MapleStory楓谷\楓谷資料\六轉碎片進度計算\icon.ico')
win.geometry('470x510')

# 保存文件名
data_file = "hexacalcu.json"

# 從文件中加載數據
def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {}

# 將數據保存到文件
def save_data():
    data = {
        "sk1v": sk1v.get(),
        "ma1v": ma1v.get(),
        "ma2v": ma2v.get(),
        "en1v": en1v.get(),
        "en2v": en2v.get(),
        "en3v": en3v.get(),
        "en4v": en4v.get(),
        "co1v": co1v.get(),
        "remain_frags": remain_frags.get(),
        "dungeon_var": dungeon_var.get()
    }
    with open(data_file, "w") as file:
        json.dump(data, file)

labels = ['技能核心','精通核心1','精通核心2','強化核心1','強化核心2','強化核心3','強化核心4','共用核心','剩餘碎片','','總消耗碎片:','還需碎片:','碎片進度:','純每日天數:']
for i, label_text in enumerate(labels):
    label = tk.Label(win, text=label_text, font=('華康皮皮體W5', 12))
    label.grid(row=i, column=0, padx=5, pady=7, sticky='w')

labels2 = ['不計共用還需:','不計共用進度:','不計共用天數:']
for i, label_text in enumerate(labels2):
    label = tk.Label(win, text=label_text, font=('華康皮皮體W5', 12))
    label.grid(row=i+11, column=3, padx=5, pady=7, sticky='w')

def validate_input(text):
    if text.isdigit():
        value = int(text)
        return 0 <= value <= 30
    elif text == "":
        return True  # 允許空輸入
    else:
        return False
validate_input_cmd = win.register(validate_input)  # 將驗證函數註冊到視窗

def on_entry_click(event):
    event.widget.delete(0, tk.END)  # 刪除 Entry 中的所有文字
    event.widget.config(fg='black')  # 將文字顏色設置為黑色

def on_focus_out(event, entry):
    if not entry.get():
        entry.insert(0, '0')  # 如果 Entry 是空的，插入預設值為 0
        entry.config(fg='grey')  # 將文字顏色設置為灰色

def create_entry_with_validation(row, textvariable):
    entry = tk.Entry(win, width=8, fg='grey', validate="key", validatecommand=(validate_input_cmd, '%P'), textvariable=textvariable)
    entry.grid(row=row, column=2, padx=5, pady=3, sticky='w')
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', lambda event, entry=entry: on_focus_out(event, entry))
    return entry

sk1v=tk.IntVar()
sk1v.set(1)  # 設定技能核心的預設值為1
ma1v=tk.IntVar()
ma2v=tk.IntVar()
en1v=tk.IntVar()
en2v=tk.IntVar()
en3v=tk.IntVar()
en4v=tk.IntVar()
co1v=tk.IntVar()
remain_frags=tk.IntVar()
sk1 = create_entry_with_validation(0, sk1v)
ma1 = create_entry_with_validation(1, ma1v)
ma2 = create_entry_with_validation(2, ma2v)
en1 = create_entry_with_validation(3, en1v)
en2 = create_entry_with_validation(4, en2v)
en3 = create_entry_with_validation(5, en3v)
en4 = create_entry_with_validation(6, en4v)
co1 = create_entry_with_validation(7, co1v)
remain_frags_Label = tk.Entry(win, width=8, fg='grey', textvariable=remain_frags)
remain_frags_Label.grid(row=8, column=2, padx=5, pady=3, sticky='w')
remain_frags_Label.bind('<FocusIn>', on_entry_click)
remain_frags_Label.bind('<FocusOut>', lambda event, entry=remain_frags_Label: on_focus_out(event, entry))


dungeon_var = tk.BooleanVar()
dungeon_check = tk.Checkbutton(win, text="副本", font=('華康皮皮體W5', 12), variable=dungeon_var)
dungeon_check.grid(row=9, column=0, padx=5, pady=3, sticky='w')

# 加載數據並設置初始值
data = load_data()
sk1v.set(data.get("sk1v", 0))
ma1v.set(data.get("ma1v", 0))
ma2v.set(data.get("ma2v", 0))
en1v.set(data.get("en1v", 0))
en2v.set(data.get("en2v", 0))
en3v.set(data.get("en3v", 0))
en4v.set(data.get("en4v", 0))
co1v.set(data.get("co1v", 0))
remain_frags.set(data.get("remain_frags", 0))
dungeon_var.set(data.get("dungeon_var", False))

def cacul_level_need():
    current_level = [sk1v.get(),ma1v.get(),ma2v.get(),en1v.get(),en2v.get(),en3v.get(),en4v.get(),co1v.get(),remain_frags.get()]
    s1 = sum(skillLevel[:current_level[0]])
    m1 = sum(masterLevel[:current_level[1]])
    m2 = sum(masterLevel[:current_level[2]])
    e1 = sum(enhancementLevel[:current_level[3]])
    e2 = sum(enhancementLevel[:current_level[4]])
    e3 = sum(enhancementLevel[:current_level[5]])
    e4 = sum(enhancementLevel[:current_level[6]])
    c1 = sum(commonLevel[:current_level[7]])
    current_consumed =  s1+m1+m2+e1+e2+e3+e4+c1+current_level[8]        #總消耗
    noCommon_current_consumed =  s1+m1+m2+e1+e2+e3+e4+current_level[8]  #不計共用總消耗
    need_frag = allFrag - current_consumed                              #總剩餘
    noCommon_need_frag = noCommonAllFrag - noCommon_current_consumed    #不計共用總剩餘
    current_consumed_Label['text'] = current_consumed
    need_frags_Label['text'] = allFrag-current_consumed
    frags_progress_Label['text'] = "{:.2%}".format(current_consumed/allFrag)
    noCommon_need_frags_Label['text'] = noCommonAllFrag-noCommon_current_consumed
    noCommon_frags_progress_Label['text'] = "{:.2%}".format(noCommon_current_consumed/noCommonAllFrag)
    consumed_frags = [s1,m1,m2,e1,e2,e3,e4,c1]
    need_frags = [all_skill_frags-s1,all_master_frags-m1,all_master_frags-m2,all_enhance_frags-e1,all_enhance_frags-e2,all_enhance_frags-e3,all_enhance_frags-e4,all_common_frags-c1]
    next_level = [skillLevel[current_level[0]],masterLevel[current_level[1]],masterLevel[current_level[2]],enhancementLevel[current_level[3]],enhancementLevel[current_level[4]],enhancementLevel[current_level[5]],enhancementLevel[current_level[6]],commonLevel[current_level[7]]]
    
    # 獲取當前星期幾
    now_weekday = datetime.now().weekday()  # 0: 星期一, 1: 星期二, ..., 6: 星期日
    dungeon_var_value = dungeon_var.get()  # 獲取副本勾選狀態
    
    # 根據當天星期計算當周碎片數量
    if now_weekday < 3:
        fragments_collected = now_weekday * 12 + (now_weekday // 3) * 50
        if not dungeon_var_value:
            fragments_collected += (now_weekday >= 3) * 30
        days_needed = 6 - now_weekday
    elif now_weekday == 3 and not dungeon_var_value:
        fragments_collected = 66
        days_needed = 3
    elif now_weekday == 4 and not dungeon_var_value:
        fragments_collected = 54
        days_needed = 2
    elif now_weekday == 5 and not dungeon_var_value:
        fragments_collected = 42
        days_needed = 1
    elif now_weekday == 6 and not dungeon_var_value:
        fragments_collected = 30
        days_needed = 0
    elif now_weekday >= 3 and dungeon_var_value:
        fragments_collected = 84 - (7 - now_weekday) * 12
        days_needed = now_weekday - 3
    else:
        fragments_collected = 84 - (7 - now_weekday) * 12
        days_needed = now_weekday - 3
    noCommon_days_needed = days_needed
    noCommon_fragments_collected = fragments_collected
    # 計算當周以外的剩餘天數
    while (need_frag - fragments_collected) > 164:
        days_needed += 7
        fragments_collected += 164
    
    remaining_fragments = need_frag - fragments_collected
    if remaining_fragments <= 12:
        days_needed += 1
    elif remaining_fragments <= 24:
        days_needed += 2
    elif remaining_fragments <= 86:
        days_needed += 3
    elif remaining_fragments <= 128:
        days_needed += 4
    elif remaining_fragments <= 140:
        days_needed += 5
    elif remaining_fragments <= 152:
        days_needed += 6
    elif remaining_fragments <= 164:
        days_needed += 7

    # 計算不計共用碎片的剩餘天數
    while (noCommon_need_frag - noCommon_fragments_collected) > 164:
        noCommon_days_needed += 7
        noCommon_fragments_collected += 164
    
    noCommon_remaining_fragments = noCommon_need_frag - noCommon_fragments_collected
    if noCommon_remaining_fragments <= 12:
        noCommon_days_needed += 1
    elif noCommon_remaining_fragments <= 24:
        noCommon_days_needed += 2
    elif noCommon_remaining_fragments <= 86:
        noCommon_days_needed += 3
    elif noCommon_remaining_fragments <= 128:
        noCommon_days_needed += 4
    elif noCommon_remaining_fragments <= 140:
        noCommon_days_needed += 5
    elif noCommon_remaining_fragments <= 152:
        noCommon_days_needed += 6
    elif noCommon_remaining_fragments <= 164:
        noCommon_days_needed += 7
    
    # 更新顯示
    current_consumed_Label['text'] = current_consumed
    need_frags_Label['text'] = need_frag
    frags_progress_Label['text'] = "{:.2%}".format(current_consumed / allFrag)
    noCommon_need_frags_Label['text'] = noCommon_need_frag
    noCommon_frags_progress_Label['text'] = "{:.2%}".format(noCommon_current_consumed / noCommonAllFrag)
    remain_days_Label['text'] = "{:.0f}".format(days_needed)
    noCommon_remain_days_Label['text'] = "{:.0f}".format(noCommon_days_needed)

    for widget in win.grid_slaves(column=3):
        row = int(widget.grid_info()["row"])
        if row <= 8:
            widget.config(text='')
    for widget in win.grid_slaves(column=4):
        row = int(widget.grid_info()["row"])
        if row <= 8:
            widget.config(text='')
    for i, consumed_frags_value in enumerate(consumed_frags):
        if consumed_frags_value != 0:
            label_text = f'已消耗碎片: {consumed_frags_value}'
            econ = tk.Label(win, text=label_text, font=('華康皮皮體W5', 12))
            econ.grid(row=i, column=3, padx=5, pady=3, sticky='w')
    for i, need_frags_value in enumerate(need_frags):
        if need_frags_value != 0:
            label_text = f'共還需碎片: {need_frags_value} \n下一級: {next_level[i]}'
            erem = tk.Label(win, text=label_text, font=('華康皮皮體W5', 9))
            erem.grid(row=i, column=4, padx=5, pady=3, sticky='w')

current_consumed_Label = tk.Label(win,width=8, text='0' ,font=('華康皮皮體W5', 12))
current_consumed_Label.grid(row=10, column=2, padx=5, pady=3, sticky='w')
need_frags_Label = tk.Label(win,width=8, text=allFrag ,font=('華康皮皮體W5', 12))
need_frags_Label.grid(row=11, column=2, padx=5, pady=3, sticky='w')
frags_progress_Label = tk.Label(win,width=8, text='0%' ,font=('華康皮皮體W5', 12))
frags_progress_Label.grid(row=12, column=2, padx=5, pady=3, sticky='w')
remain_days_Label = tk.Label(win, width=8, text='0', font=('華康皮皮體W5', 12))
remain_days_Label.grid(row=13, column=2, padx=5, pady=3, sticky='w')

noCommon_need_frags_Label = tk.Label(win,width=8, text=noCommonAllFrag ,font=('華康皮皮體W5', 12))
noCommon_need_frags_Label.grid(row=11, column=4, padx=5, pady=3, sticky='w')
noCommon_frags_progress_Label = tk.Label(win,width=8, text='0%' ,font=('華康皮皮體W5', 12))
noCommon_frags_progress_Label.grid(row=12, column=4, padx=5, pady=3, sticky='w')
noCommon_remain_days_Label = tk.Label(win, width=8, text='0', font=('華康皮皮體W5', 12))
noCommon_remain_days_Label.grid(row=13, column=4, padx=5, pady=3, sticky='w')

calcu = tk.Button(win,width=6, text='計算', font=('華康皮皮體W5', 12), command=cacul_level_need)
calcu.grid(row=10, column=3, padx=5, pady=3, sticky='w')

# 保存按鈕
save_button = tk.Button(win, text='保存', font=('華康皮皮體W5', 12), command=save_data)
save_button.grid(row=10, column=4, padx=5, pady=7, sticky='w')
# 在視窗關閉時保存數據
win.protocol("WM_DELETE_WINDOW", lambda: [save_data(), win.destroy()])
# 加載數據後自動計算一次
cacul_level_need()

win.mainloop()

#pyinstaller --onefile --noconsole --icon="F:\MapleStory楓谷\楓谷資料\六轉碎片進度計算\icon.ico" --add-data "F:\MapleStory楓谷\楓谷資料\六轉碎片進度計算\fonts\華康皮皮體.ttf;font" hexaCalcu2.py

