# importing only those functions
# which are needed
from tkinter import *
# import filedialog module
from tkinter import filedialog
import tkinter.scrolledtext as st
# creating tkinter window

root = Tk()
root.title('Menu Demonstration')

# Creating Menubar
menubar = Menu(root)
content = Frame(root)
content.pack(side=BOTTOM)

# Set window size
root.geometry("500x500")

# Set window background color
root.config(background="white")

# Create a File Explorer label
label_file_explorer = Label(root,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")
label_file_explorer.pack()

listbox = Listbox(root,width=100)

listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(root,orient="vertical")

scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)

def browseFiles():
    filename = filedialog.askopenfilenames(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("Excell files",
                                                      "*.xlsx*"),
                                                     ("PDF files",
                                                      "*.pdf*"),
                                                     ("CSV files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    lst = list(filename)

    print(lst)
    myfiles=""
    for file in lst:
        print(file)
        myfiles=myfiles+"\n"+file
        listbox.insert(END, file)

    label_file_explorer.configure(text="File Opened: " + str(myfiles))


#filez = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
#lst = list(filez)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = browseFiles)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
root.config(menu = menubar)
mainloop()


