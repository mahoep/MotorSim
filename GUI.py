# Place holder GUI for now, doesn't do anything
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #self.pack()
        self.build_labels()
        #self.buttons()


    def build_labels(self):
        titleRow = ["Grain Type", "Grain Length", "Grain Diameter", "Core Diameter"]
        i = 0
        self.rowOne = tk.Label(root, text="Grain 1").grid(row=1,column=0) # .grid(row=i+1, column=0)
        for titles in titleRow:
            self.titleRow = tk.Label(root, text=titleRow[i]).grid(row=0,column=i+1)
            i += 1

    def new_line(self):
        ent = tk.Entry(root, width=15)
        ent.pack()


    def buttons(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(row=10, column=0, columnspan=10, sticky="new")

        self.add_grain = tk.Button(self, text="Add Grain")
        self.add_grain["command"] = self.new_line
        self.add_grain.grid(row=11, column=1, columnspan=10, sticky="new")

root = tk.Tk()
app = Application(master=root)
app.mainloop()





