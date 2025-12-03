import tkinter

'''pack(): This manager arranges widgets in a horizontal or vertical stack within their parent. 
Widgets are placed sequentially, and their positions can be influenced by options like side 
(left, right, top, bottom), fill (expand to fill available space), and expand 
(expand to fill extra space).

grid(): This manager organizes widgets in a two-dimensional grid, similar to rows and columns in a 
table. Widgets are placed at specific row and column coordinates, and their size and position can
be further controlled using options like rowspan, columnspan, sticky (align within cell), and 
padx/pady (padding).

place(): This manager offers the most precise control over widget placement by allowing you to 
specify the exact x and y coordinates, as well as the width and height, of each widget within 
its parent. This method can be useful for highly customized layouts but requires more manual 
calculation.'''

'''If you are using any layout manager like pack, grid, place you have to use one LM throughout the project'''

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("Introduction to GUI")
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.grid(column=0, row=0)  # Without pack method the label will not be displayed in GUI. Try for yourselves

my_label["text"] = "New Text"
my_label.config(text="New Text", padx=20, pady=20)


def button_clicked():
    new_text = input_tk.get()
    my_label.config(text=new_text, padx=20, pady=20)


my_button = tkinter.Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button = tkinter.Button(text="Don't Click me", command=button_clicked)
new_button.grid(column=2, row=0)

input_tk = tkinter.Entry(width=20)
input_tk.grid(column=3, row=3)

window.mainloop()
