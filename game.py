import tkinter as tk

class game:
    def handle_click_tile(self, event): 0
    def handle_click_reset(self, event): self.__init__(self.dimensions)
    def click_toggle_flag(self, event): self.flag = not self.flag

    def __init__(self, dimensions, root = tk.Tk()):
        self.flag = False
        self.dimensions = dimensions
        #self.root.withdraw()
        self.window = tk.Toplevel(root)
        self.frames = []
        self.buttons2d = []
        for x in range(dimensions[0]):
            self.frames.append(tk.Frame(master = self.window))
            self.buttons2d.append([])
        for x in range(len(self.frames)):
            for y in range(dimensions[1]):
                self.buttons2d[x].append(tk.Button(master=self.frames[x], height=2, width=4))
        self.frames.insert(0,tk.Frame(master = self.window))
        button_flag = tk.Button(master=self.frames[0], height=2, width=4,text="|>\n|", anchor="w"); button_flag.pack(side=tk.LEFT); button_flag.bind('<Button-1>', self.click_toggle_flag)
        button_reset = tk.Button(master=self.frames[0], height=2, width=4,text="Reset"); button_reset.pack(side=tk.LEFT); button_reset.bind('<Button-1>', self.handle_click_reset)
        for button_list in self.buttons2d:
            for button in button_list:
                button.pack(side=tk.LEFT)
                button.bind('<Button-1>', self.handle_click_tile)
                button['bg'] = "black"
                button['fg'] = "white"
        for frame in self.frames:
            frame.pack()
        root.mainloop()
    
    def update(self, minefield):
        for x in range(len(minefield)):
            for y in range(len(minefield[x])):
                0

_game = game([10, 20])
