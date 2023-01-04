from tkinter import *
from tkinter import messagebox, colorchooser, font

loop = True
cookies = 0
cps = 0
base_price = 10
price_1 = 10



def update_cookie_ammount():
    cookie_ammount.config(text=f"cookies: {cookies}")

def get_cps():
    global cookies
    cookies += cps
    update_cookie_ammount()
    window.after(1000, get_cps)

def get_cookie():
    global cookies
    cookies += 1
    update_cookie_ammount()

def upgrade_cps_1():
    global cps
    global cookies
    global price_1
    if cookies < price_1:
        price_1_text.config(fg="#FF0000")
    else:
        cps+=1
        cookies-=price_1
        update_cookie_ammount()
        cps_ammount.config(text=f"cps: {cps}")
        price_1 = int(price_1*1.2)
        price_1_text.config(fg="#000000", text=f"${price_1}")

def change_colors():
    color = (colorchooser.askcolor())[1]
    window.config(bg=color)
    empty_space.config(bg=color)

def exit():
    global loop
    if messagebox.askyesno(title="oh", message="Do you really want to quit? :("):
        loop = False

window = Tk()
window.geometry("430x300")
sans = font.Font(window, family="Comic Sans MS")

cps_ammount = Label(window, text=f"cps: {cps}", font=sans)
cps_ammount.grid(column=2, row=1)

cookie_ammount = Label(window, text=f"cookies: {cookies}", font=sans)
cookie_ammount.grid(column=1, row=1)

empty_space = Label(window, padx=100)
empty_space.grid(column=3, row=1)

color_button = Button(window, text="color", command=change_colors, padx=16, font=sans)
color_button.grid(column=4, row=1)

exit_button = Button(window, text="exit", bg="#FF0000", command=exit, padx=20, font=sans)
exit_button.grid(column=4, row=2)

cookie_button = Button(window, text="get cookie", command=get_cookie, font=sans)
cookie_button.grid(column=1, row=2)

price_1_text = Label(window, text=f"${price_1}", font=sans)
price_1_text.grid(column=2, row=3)

upgrade_button_1 = Button(window, text="+1 cps", command=upgrade_cps_1, font=sans)
upgrade_button_1.grid(column=1, row=3)


window.after(0, get_cps())
while loop is True:
    window.update_idletasks()
    window.update()