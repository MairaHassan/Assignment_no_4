import tkinter as tk

# Configuration
CELL_SIZE = 40
ROWS = 10
COLS = 10
DEFAULT_ERASER_SIZE = 60

class CanvasEraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser with Features")

        # Canvas
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        # Controls
        self.controls = tk.Frame(root)
        self.controls.pack(pady=5)

        self.reset_btn = tk.Button(self.controls, text="Reset", command=self.reset_grid)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        self.undo_btn = tk.Button(self.controls, text="Undo", command=self.undo)
        self.undo_btn.pack(side=tk.LEFT, padx=5)

        self.slider_label = tk.Label(self.controls, text="Eraser Size:")
        self.slider_label.pack(side=tk.LEFT)

        self.eraser_size_var = tk.IntVar(value=DEFAULT_ERASER_SIZE)
        self.slider = tk.Scale(self.controls, from_=20, to=100, orient=tk.HORIZONTAL, variable=self.eraser_size_var, command=self.update_eraser_size)
        self.slider.pack(side=tk.LEFT)

        self.cells = []
        self.previous_states = []  # Stack for undo
        self.create_grid()

        # Create eraser
        self.eraser_size = DEFAULT_ERASER_SIZE
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, fill="white", outline="black", width=2)

        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        for i in range(ROWS):
            row = []
            for j in range(COLS):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row.append(rect)
            self.cells.append(row)

    def move_eraser(self, event):
        self.save_state()  # Save current state for undo
        size = self.eraser_size
        x1 = event.x - size // 2
        y1 = event.y - size // 2
        x2 = x1 + size
        y2 = y1 + size
        self.canvas.coords(self.eraser, x1, y1, x2, y2)
        self.erase_overlapping_cells(x1, y1, x2, y2)

    def erase_overlapping_cells(self, ex1, ey1, ex2, ey2):
        for row in self.cells:
            for cell in row:
                x1, y1, x2, y2 = self.canvas.coords(cell)
                if self.rects_overlap(ex1, ey1, ex2, ey2, x1, y1, x2, y2):
                    self.canvas.itemconfig(cell, fill="white")

    def reset_grid(self):
        for row in self.cells:
            for cell in row:
                self.canvas.itemconfig(cell, fill="blue")

    def save_state(self):
        state = []
        for row in self.cells:
            state.append([self.canvas.itemcget(cell, 'fill') for cell in row])
        self.previous_states.append(state)

    def undo(self):
        if self.previous_states:
            last_state = self.previous_states.pop()
            for i, row in enumerate(self.cells):
                for j, cell in enumerate(row):
                    self.canvas.itemconfig(cell, fill=last_state[i][j])

    def update_eraser_size(self, value):
        self.eraser_size = int(value)

    @staticmethod
    def rects_overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return not (ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2)

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasEraserApp(root)
    root.mainloop()
