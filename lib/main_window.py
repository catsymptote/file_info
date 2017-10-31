from tkinter import *
from tkinter import filedialog

from lib import file_info

class c_root_window:
    fileObj = file_info.c_file_info()


    def __init__(self, master_window):
        frame = Frame(master_window)
        frame.pack()

        self.print_button = Button(frame, text="Print message", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.print_button = Button(frame, text="Choose file", command=self.set_file)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Count characters", command=self.get_chars)
        self.quit_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Count lines", command=self.get_lines)
        self.quit_button.pack(side=LEFT)
    
    def print_message(self):
        print("Here is the printed message.")
        sys.stdout.flush()

    def print_test_message(self):
        print("Here is another printed message.")
        sys.stdout.flush()
    
    def get_chars(self):
        self.fileObj.counter()
        print("Chars:\t" + str(self.fileObj.get_chars()))
        sys.stdout.flush()

    def get_lines(self):
        self.fileObj.counter()
        print("Lines:\t" + str(self.fileObj.get_lines()))
        sys.stdout.flush()

    def set_file(self):
        filename = filedialog.askopenfilename()    # Set the file directory
        if (filename != ""):
            print("First input directory:\t" + str(filename))
            sys.stdout.flush()
            self.fileObj.set_filename(filename)
