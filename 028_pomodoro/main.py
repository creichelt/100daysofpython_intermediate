from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    title.config(text='Timer', fg=GREEN)
    check_mark.config()
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0

# def timer_pause():
#     window.after(timer, callback=None)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    s_break_sec = SHORT_BREAK_MIN * 60
    l_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(l_break_sec)
        title.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(s_break_sec)
        title.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        title.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        timer_start()
        marks = ''
        work_sesh = math.floor(reps/2)
        for i in range(work_sesh):
            marks += CHECK
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title = Label()
title.config(text='Timer', font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0) # removing border
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35))
canvas.grid(column=1, row=1)

button_start = Button(text='Start', command=timer_start, highlightbackground=YELLOW)
button_start.config(padx=0,pady=0)
button_start.grid(column=0, row=2)

button_reset = Button(text='Reset', command=timer_reset, highlightbackground=YELLOW)
button_reset.grid(column=2, row=2)

check_mark = Label()
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

# button_pause = Button(text='Pause', command=timer_pause, highlightbackground=YELLOW)
# button_pause.grid(column=0, row=3)

window.mainloop()