import tkinter


class Field:
    def __int__(self, root, label_text):
        self.label = tkinter.label()
        self.label.pack()

        self.entry = tkinter.Entry(root)


