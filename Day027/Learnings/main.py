import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Introduction to GUI")

my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack()  # Without pack method the label will not be displayed in GUI. Try for yourselves

'''We can change already defined argument values in tkinter like this. There are so many methods
like these you can refer to tkinter documentation online'''
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    new_text = input_tk.get()
    my_label.config(text=new_text)


my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.pack()

input_tk = tkinter.Entry(width=20)
input_tk.pack()

# Entries
entry = tkinter.Entry(width=30)
# Add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()

# Spinbox


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton


def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

window.mainloop()
