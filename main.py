import tkinter as tk
import random
import numpy as np

shape = (10, 4)
snake_array = np.zeros(shape, dtype=np.int8)
#print(snake_array)

w = 600
h = 400
x = w//2
y = h//2

direct = [0, 0]

def random_x(w):
    return random.randint(1, (w - 1))

def random_y(h):
    return random.randint(1, (h - 1))
    
def init_chr():
    x = random_x(w)
    y = random_y(h)

    chr = canvas.create_oval(x, y, x + 10, y + 10)
    return chr

def move_chr(event):
    chr.itemconfig()

def up(event):
    global direct
    x = 0
    y = -10
    direct = x, y
    canvas.move(chr, x, y)
    
def down(event):
    global direct
    x = 0
    y = 10
    direct = x, y
    canvas.move(chr, x, y)

def right(event):
    global direct
    x = 10
    y = 0
    direct = x, y
    canvas.move(chr, x, y)

def left(event):
    global direct
    x = -10
    y = 0
    direct = x, y
    canvas.move(chr, x, y)

def food_gen():
    global food
    x = random_x(w)
    y = random_y(h)

    food = canvas.create_oval(x, y, x + 15, y + 15, fill="red")
    

def collison():
    chr_cord = canvas.coords(chr)
    item_cord = canvas.coords(food)

    coll = list(canvas.find_overlapping(chr_cord[0], chr_cord[1], chr_cord[2], chr_cord[3]))
    coll.remove(chr)
    if len(coll) != 0:
        print('hit')
        return True

def collision_event(val:bool):
    global food
    if val:
        canvas.delete(food)
        food_gen()
        
def outbound_event():
    global chr
    chr_cord = canvas.coords(chr)
    trigger = False

    if chr_cord[0] <= 0:
        trigger = True
    if chr_cord[1] <= 0 :
        trigger = True   
    if chr_cord[0] >= w:
        trigger = True
    if chr_cord[1] >= h :
        trigger = True

    
    if trigger:
        canvas.delete(chr)
        chr = init_chr()

def main_loop():
    is_collision = collison()
    collision_event(is_collision)
    outbound_event()
    canvas.move(chr, direct[0], direct[1])
    canvas.after(60, main_loop)

win = tk.Tk ()
win.geometry('800x600')
main_frame = tk.Frame(win, width= w, height= h)

canvas = tk.Canvas(win, width= w, height= h, background= "white")
canvas.pack()
chr = init_chr()
food_gen()
main_loop()

win.bind('<w>', up)
win.bind('<s>', down)
win.bind('<d>', right)
win.bind('<a>', left)


win.mainloop()