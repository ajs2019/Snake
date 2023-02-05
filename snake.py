import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.head = canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, fill='red')
        self.body = [self.head]
        self.direction = 'right'
        self.food = None

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.head)

        if self.direction == 'right':
            x1 += CELL_SIZE
            x2 += CELL_SIZE
        elif self.direction == 'left':
            x1 -= CELL_SIZE
            x2 -= CELL_SIZE
        elif self.direction == 'down':
            y1 += CELL_SIZE
            y2 += CELL_SIZE
        elif self.direction == 'up':
            y1 -= CELL_SIZE
            y2 -= CELL_SIZE

        if x1 <= 0 or x2 >= WIDTH or y1 <= 0 or y2 >= HEIGHT:
            return False

        new_head = self.canvas.create_rectangle(x1, y1, x2, y2, fill='red')
        self.canvas.delete(self.body[-1])
        self.body = [new_head] + self.body[:-1]

        if self.food is not None and self.head == self.food:
            self.body.append(self.canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, fill='green'))
            self.food = None

        return True

    def change_direction(self, event):
        if event.keysym == 'Up':
            self.direction = 'up'
        elif event.keysym == 'Down':
            self.direction = 'down'
        elif event.keysym == 'Left':
            self.direction = 'left'
        elif event.keysym == 'Right':
            self.direction = 'right'

    def add_food(self):
        if self.food is None:
            x1 = CELL_SIZE * random.randint(0, int(WIDTH / CELL_SIZE) - 1)
            y1 = CELL_SIZE * random.randint(0, int(HEIGHT / CELL_SIZE) - 1)
            self.food = self.canvas.create_rectangle(x1, y1, x1 + CELL_SIZE, y1 + CELL_SIZE, fill='yellow')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    snake = Snake(canvas)
    root.bind('<Key>', snake.change_direction)

    while True:
        if not snake.move():
            break

        snake.add_food()
        root.update()
        root.after()
