import Tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        button = tk.Button(text="Save", command=self.save)
        button.pack(side="top")
        self.widgets = []
        for line in ["one","two","three","four"]:
            widget = tk.Entry(self)
            widget.insert(0, line)
            widget.pack(side="top", fill="x")
            self.widgets.append(widget)

    def save(self):
        for widget in self.widgets:
            print widget.get()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    
    
    