import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from time import sleep
from datetime import datetime
import random
import threading


button_state = True
date = datetime.now()
health = 3
user_score = 0
button_ids = []

# -- UPDATE LABEL --

def update_label(win:ttk.Window,lbl_name:str,content:str):
    for x in win.children.values():
        if not isinstance(x,ttk.Label): continue
        if x.winfo_name() == lbl_name:
            x.config(text=content)
    
# -- HANDLE THE PLAYED TIME --

def set_timer(startTime:datetime,win:ttk.Window):
    global button_state
    while(button_state == False):
        sleep(1)
        update_label(win,"time_info", f"Elapsed Time : {str((datetime.now()-startTime)).split('.')[0]}")

# -- SELECT THE RANDOM BUTTONS FROM THE WINDOW --

def select_random_boxes(win:ttk.Window):
    global button_ids
    all_buttons = []
    for x in win.children.values():
        if not isinstance(x,ttk.Button) or x.winfo_name() == "start_button": continue
        all_buttons.append(x.winfo_id())
     
    for y in range(4):
        sleep(.1)
        id = random.choice(all_buttons)
        all_buttons.remove(id)
        button_ids.append(id)
       
    
# 46137359
# 46137368
# 46137371
# 46137376

# -- SHOW THE CORRECT BUTTONS IN START --

def show_the_buttons_shortly(win:ttk.Window):
    for x in win.children.values():
        if not isinstance(x,ttk.Button): continue
        if x.winfo_id() in button_ids:
            x.config(bootstyle="success-outline")
    
    sleep(1)
    
    for x in win.children.values():
        if not isinstance(x,ttk.Button): continue
        if x.winfo_id() in button_ids:
            x.config(bootstyle="primary")
    
# -- CREATE MAIN WINDOW

def create_window():
    root = ttk.Window(themename="darkly",resizable=(0,0))
    root.title("Find The Boxes")
    root.geometry("420x600")
  
        
    s = ttk.Style()
    s.configure("TFrame",background="#2A8C82")
    footer_frame = ttk.Frame(root,style="TFrame")
    footer_frame.place(x=0,y=500,height=100,width=420)
    
    # -START BUTTON-
    def start_button_click(btn:ttk.Button):
        global button_state,user_score,health,button_ids
        global date
        # is_button_correct(root)
        button_state = not button_state
        if button_state : 
            btn.config(text="Start")
            button_state = True
            date = datetime.now()
            reset_player_status(window=window,is_score_too=True)
            for x in root.children.values():
                if not isinstance(x,ttk.Button) or x.winfo_name() == "start_button": continue
                x.config(bootstyle="primary")
            
                        
        else: 
            button_ids = []
            select_random_boxes(win=window)
            threading.Thread(daemon=True,target=show_the_buttons_shortly,args=(window,)).start()
            # show_the_buttons_shortly(win=window)
            date = datetime.now()
            threading.Thread(daemon=True,target=set_timer,args=(date,root)).start()
            change_button_state(ACTIVE,window=window)
            reset_player_status(window=window,is_score_too=False)
            btn.config(text="Stop")
            
            
            # set_timer(date)
    
    start_button = ttk.Button(root,text="Start",name="start_button")
    start_button.config(command = lambda btn=start_button:start_button_click(btn))
    start_button.place(x=300,y=525,height=50,width=100)
    
    # -- TIME LABEL --
    time_label = ttk.Label(root,text="Elapsed Time : 0:00:00",background="#2A8C82",name="time_info")
    time_label.place(x=30,y=515)
    
    # -- SCORE LABEL --
    score_label = ttk.Label(root,text="Your score is  : 0",background="#2A8C82",name="score_info")
    score_label.place(x=30,y=540)
    
    # -- HEALTH LABEL --
    health_symbol = "♥"
    health_label = ttk.Label(root,text=f"Your health    : {' '.join([health_symbol for x in range(health)])}",background="#2A8C82",name="health_info")
    health_label.place(x=30,y=565)    
    
    return root

# -- RESET PLAYER STATS --

def reset_player_status(window:ttk.Window,is_score_too:bool):
    global user_score,health
    
    if is_score_too: user_score = 0
    health = 3
    update_label(window,"score_info",f"Your score is  : {user_score}")
    update_label(window,"health_info",f"Your health    : {' '.join(['♥' for x in range(health)])}")
    update_label(window,"time_info","Elapsed Time : 0:00:00")
    for x in window.children.values():
        if not isinstance(x,ttk.Button):continue
        if x.winfo_name() == "start_button":
            x.config(text="Start")


# -- SET BUTTON CLICK VISUAL --

def is_button_correct(win:ttk.Window):
    global button_ids
    for x in win.children.values():
        if not isinstance(x,ttk.Button): continue
        if x.winfo_id() in button_ids:
            x.config(bootstyle="danger-outline")
        else:
            x.config(bootstyle="success-link")
        
# -- SHOW POP-UP --
def show_messagebox(msg:str,ttl:str,scr:bool = True):
    global button_state,window,button_ids
    change_button_state(DISABLED,window=window)
    mb = Messagebox.yesno(message=msg,title=ttl)
    if mb == "Yes":
        reset_player_status(window=window,is_score_too=scr)
        change_button_state(ACTIVE,window=window)
        button_ids = []
        for x in window.children.values():
            if not isinstance(x,ttk.Button): continue
            x.config(bootstyle="primary")
    else:
        button_state == False
        for x in window.children.values():
            if not isinstance(x,ttk.Button) or x.winfo_name() != "start_button": continue
            x.config(state=DISABLED)
    
    
# -- CHECK THE CLICKED BUTTON --
def button_check(button:ttk.Button):
    global button_state,window,user_score,health,button_ids

    if button.winfo_id() in button_ids:
        button.config(bootstyle="success-outline",state=DISABLED)
        update_label(window,"score_info",f"Your score is  : {user_score}")
        button_ids.remove(button.winfo_id())
        if len(button_ids) == 0:
            button_state = True
            change_button_state(DISABLED,window=window)
            user_score += 1
            show_messagebox("Would you likte to play again ?","You Won !",False)
            
                    
        
    else:
        button.config(bootstyle="danger-outline")
        health -=1
        update_label(window,"health_info",f"Your health    : {' '.join(['♥' for x in range(health)])}")
        if health == 0:
            button_state = True
            show_messagebox("You don't have any more lives left, do you want to try again ?",
                            "You Lost !")
            


# -- SET BUTTONS AS GRID --
def set_buttons(event,window:ttk.Window):
    
    
    for x in range(1,5):
        for y in range(1,5):
            button = ttk.Button(window)
            button.config(command=lambda btn=button:event(btn),
                          state=DISABLED)
            
            button.grid(row=x,column=y,ipadx=20,ipady=20,
                        padx=20,pady=20)

# -- CHANGE START BUTTON STATE --
def change_button_state(state,window:ttk.Window):
    for x in window.children.values():
        if not isinstance(x,ttk.Button) or x.winfo_name()=="start_button": continue
        x.config(state=state)

window = create_window()
set_buttons(button_check,window=window)

window.mainloop()
sleep(2)
