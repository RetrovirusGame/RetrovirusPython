from tkinter import *
import time, random

WIDTH = 800
HEIGHT = 600

root = Tk()
root.wm_resizable(0, 0)
root.title("Retrovirus")

canvas = Canvas(root, width=WIDTH, height=HEIGHT)

class Game:
    def __init__(self, root, canvas, virus, antibodies):
        self.root = root
        self.canvas = canvas
        self.virus = virus
        self.antibodies = antibodies
    
    def mainloop(self)
        self.canvas.create_rectangle(0, 0, self.canvas.width, self.canvas.height, color="black")
        self.root.update()
        self.root.update_idletasks()
        time.sleep(0.0001)

class Entity:
    def __init__(self, x, y, img)
        self.x = x
        self.y = y
        self.img = img

class Virus(Entity):
    def __init__(self, x, y, img, health):
        Entity.__init__(self, x, y, img)
        self.health = health

class Antibody(Entity):
    def __init__(self, x, y, img):
        Entity.__init__(self, x, y, img)

antibodies = list(Antibody(0, 0, "antibody.png") for _ in range(5))
virus = Virus(0, 0, "retrovirus.png")
g = Game(root, canvas, virus, antibodies)

while 1:
    g.mainloop()
        
