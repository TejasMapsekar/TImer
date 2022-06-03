import tkinter as tk
import time
import threading

reset = False

sec = 0
min = 0
hour = 0
sec_p = 0
min_p = 0
hour_p = 0

r = 0

def start_timer():
    global threads_for_clock
    global reset
    global sec 
    global min 
    global hour 
    sec = 0
    min = 0
    hour = 0
    while(True):
        time.sleep(1)
        sec += 1
        if(reset):
            break
        if(sec == 60):
            sec = 0
            min += 1
        if(min == 60):
            min = 0
            hour += 1
        if(hour == 24):
            hour = 0
        t.set(str(hour)+":"+str(min)+":"+str(sec))

threads_for_clock = [threading.Thread(target = start_timer) for q in range (0,100)]

def start_timer_thread():
    global reset
    global threads_for_clock
    global r
    reset = True
    if(threads_for_clock[r].is_alive()):
        threads_for_clock[r].join()
    if(threads_for_resume[r].is_alive()):
        threads_for_resume[r].join()
    reset = False
    r=r+1
    threads_for_clock[r].start()

def pause_timer():
    global reset
    reset = True
    global sec_p
    global min_p
    global hour_p
    global sec 
    global min 
    global hour 
    sec_p = sec
    min_p = min
    hour_p = hour

def resume_timer():
    global threads_for_clock
    global reset
    global sec_p
    global min_p
    global hour_p
    global sec 
    global min 
    global hour
    sec = sec_p
    min = min_p
    hour = hour_p
    while(True):
        time.sleep(1)
        sec += 1
        if(reset):
            break
        if(sec == 60):
            sec = 0
            min += 1
        if(min == 60):
            min = 0
            hour += 1
        if(hour == 24):
            hour = 0
        t.set(str(hour)+":"+str(min)+":"+str(sec))



threads_for_resume = [threading.Thread(target = resume_timer) for q in range (0,100)]

def resume_timer_thread():
    global reset
    global r
    if(threads_for_clock[r].is_alive()):
        threads_for_clock[r].join()
    if(threads_for_resume[r].is_alive()):
        threads_for_resume[r].join()
    reset = False
    r=r+1
    threads_for_resume[r].start()



def reset_timer():
    global reset
    reset = True
    t.set("00:00:00")


root = tk.Tk()
root.title("Timer")
root.geometry("500x500")
root.resizable(False, False)
root.attributes('-topmost', 'true')
l = tk.Label(root, text="Timer", font=("Arial", 30))
l.pack()
t = tk.StringVar()
clock = tk.Label(root,text="00:00:00", font=("Arial", 30),textvariable=t)
clock.pack(pady=5)
start_button = tk.Button(root, text="Start", font=("Arial", 30), command=start_timer_thread)
start_button.pack(pady=5)
reset_button = tk.Button(root, text="Reset", font=("Arial", 30), command=reset_timer)
reset_button.pack(pady=5)
pause_button = tk.Button(root, text="Pause", font=("Arial", 30), command=pause_timer)
pause_button.pack(pady=5)
resume_button = tk.Button(root, text="Resume", font=("Arial", 30), command=resume_timer_thread)
resume_button.pack(pady=5)

root.mainloop()