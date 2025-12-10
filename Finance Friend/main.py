from tkinter import *
import datetime
from tkinter import messagebox, ttk
import json
import os
from pandas import *


def add_exp():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showinfo(title="Invalid amount entry", message="The amount should be in numbers.")
        return

    date = date_entry.get()
    category = search.get()
    description = description_entry.get("1.0", "end-1c")

    if not date or not category or not description:
        messagebox.showinfo(title="Error", message="Fill all the information to add.")
        return

    new_data = {
        "date": date_entry.get(),
        "category": search.get(),
        "description": description_entry.get("1.0", "end-1c"),
        "amount": amount
    }

    if not os.path.exists("Summary.json"):
        data = {"expenses": []}

    else:
        try:
            with open("Summary.json", "r") as summary:
                data = json.load(summary)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {"expenses": []}

    data["expenses"].append(new_data)

    with open("Summary.json", "w") as summary:
        json.dump(data, summary, indent=4)

    messagebox.showinfo(title="Successful", message="Expense added successfully")
    search.set("")
    description_entry.delete("1.0", "end")
    amount_entry.delete(0, "end")
    search.focus()


def summary():
    try:
        if not os.path.exists("Summary.json") or os.path.getsize("Summary.json") == 0:
            data = {"expenses": []}
        else:
            with open("Summary.json", "r") as file:
                data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"expenses": []}

    if not data["expenses"]:
        messagebox.showinfo(
            title="All Records",
            message="No records found. Add some expenses first."
        )
        return

    all_expenses = ""
    for details in data["expenses"]:
        all_expenses += (
            f"Date: {details['date']}\n"
            f"Category: {details['category']}\n"
            f"Description: {details['description']}\n"
            f"Amount: ₹{details['amount']}\n"
            f"{'-' * 35}\n"
        )
    messagebox.showinfo(
        title=f"Summary",
        message=all_expenses
    )


def export_report():
    try:
        if not os.path.exists("Summary.json") or os.path.getsize("Summary.json") == 0:
            data = {"expenses": []}
        else:
            with open("Summary.json", "r") as file:
                data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"expenses": []}

    if not data["expenses"]:
        messagebox.showinfo(
            title="No Data",
            message="No expenses found! Add some data first."
        )
        return

    expenses = data["expenses"]

    df = DataFrame(expenses)
    df.to_csv("All_expenses.csv", index=False)
    messagebox.showinfo(title="Successful", message="Report exported successfully!")


def search_exp():
    category = search_combobox.get()
    try:
        if not os.path.exists("Summary.json") or os.path.getsize("Summary.json") == 0:
            data = {"expenses": []}
        else:
            with open("Summary.json", "r") as file:
                data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"expenses": []}

    if not data["expenses"]:
        messagebox.showinfo(
            title="No Data",
            message="No expenses found! Add some data first."
        )
        return

    filtered = [rec for rec in data["expenses"] if rec["category"] == category]
    total = sum(rec["amount"] for rec in filtered)
    if not filtered:
        messagebox.showinfo(
            title="No Records Found",
            message=f"No records found for category: {category}"
        )
        return
    choice = messagebox.askyesno(
        title=category,
        message=f"Total spent on {category}: ₹{total}\n\nDo you want to view all records?"
    )

    all_expenses = ""
    for details in data["expenses"]:
        if details["category"] == category:
            all_expenses += (
                f"Date: {details['date']}\n"
                f"Category: {details['category']}\n"
                f"Description: {details['description']}\n"
                f"Amount: ₹{details['amount']}\n"
                f"{'-' * 35}\n"
            )
    messagebox.showinfo(
        title=f"Summary of {category}",
        message=all_expenses
    )


def get_today_report():
    try:
        if not os.path.exists("Summary.json") or os.path.getsize("Summary.json") == 0:
            data = {"expenses": []}
        else:
            with open("Summary.json", "r") as file:
                data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        data = {"expenses": []}

    if not data["expenses"]:
        messagebox.showinfo(
            title=f"Today's report ({datetime.date.today()})",
            message="No data in file. Try adding data."
        )
        return

    all_expenses = ""
    data_frame = []

    for details in data["expenses"]:
        if details["date"] == str(datetime.date.today()):
            clean_desc = details["description"].replace("\n", " ").strip()

            all_expenses += (
                f"Date: {details['date']}\n"
                f"Category: {details['category']}\n"
                f"Description: {clean_desc}\n"
                f"Amount: ₹{details['amount']}\n"
                f"{'-' * 35}\n"
            )
            data_frame.append({
                "Date": details["date"],
                "Category": details["category"],
                "Description": clean_desc,
                "Amount": details["amount"]
            })

    if not data_frame:
        messagebox.showinfo(
            title=f"Today's report ({datetime.date.today()})",
            message="No data to show for today."
        )
        return

    choice = messagebox.askyesno(
        title=f"Today's report ({datetime.date.today()})",
        message=f"{all_expenses}\n\nDo you want to save today's report as CSV?"
    )
    if choice:
        df = DataFrame(data_frame)
        df.to_csv(f"{datetime.date.today()}_report.csv", index=False)
        messagebox.showinfo(
            title="Saved",
            message=f"Successfully Saved as {datetime.date.today()}_report.csv"
        )


def monthly_report():
    pass


def mode_selector():
    mode = radio_state.get()
    bg = "white"
    fg = "black"
    sc = "white"
    if mode == 1:
        bg = "black"
        fg = "white"
        sc = "white"
    elif mode == 2:
        bg = "white"
        fg = "black"
        sc = "black"

    window.config(bg=bg)
    canvas.config(bg=bg)
    title_label.config(bg=bg, fg=fg)
    date_label.config(bg=bg, fg=fg)
    date_entry.config(bg=bg, fg=fg, insertbackground=sc)
    search_label.config(bg=bg, fg=fg)
    description_label.config(bg=bg, fg=fg)
    description_entry.config(bg=bg, fg=fg, insertbackground=sc)
    amount_label.config(bg=bg, fg=fg)
    amount_entry.config(bg=bg, fg=fg, insertbackground=sc)
    radio_button1.config(bg=bg, fg=fg, selectcolor="red")
    radio_button2.config(bg=bg, fg=fg, selectcolor="red")
    search_for.config(bg=bg, fg=fg)


window = Tk()
window.title("Financial Data")
window.geometry("1000x600")


canvas = Canvas(height=200, width=200, highlightthickness=0)
image = PhotoImage(file="BudgetBuddy.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=0, row=0)

title_label = Label(text="Hi! I am your Budget Buddy.", font=("Courier", 18, "bold"))
title_label.grid(column=1, row=0, columnspan=2)

date_label = Label(text="Date:", font=("Courier", 10, "bold"))
date_label.grid(column=0, row=1, sticky="e", pady=5)
date_entry = Entry(width=40)
date_entry.insert(0, str(datetime.date.today()))
date_entry.grid(column=1, row=1, pady=5)

search_label = Label(text="Category:", font=("Courier", 10, "bold"))
search_label.grid(column=0, row=2, sticky="e", pady=5)
search = ttk.Combobox(state="readonly",
                      values=["Housing / Rent", "Food & Groceries", "Transportation", "Bills & Utilities",
                              "Healthcare & Medical", "Shopping & Personal Care", "Entertainment & Leisure",
                              "Savings & Investments", "Loans & EMIs", "Miscellaneous", "Others"],
                      width=37
                      )
search.focus()
search.grid(column=1, row=2, pady=5)

description_label = Label(text="Description:", font=("Courier", 10, "bold"))
description_label.grid(column=0, row=3, pady=5, sticky="e")
description_entry = Text(window, width=30, height=8)
description_entry.grid(column=1, row=3, pady=5)

amount_label = Label(text="Amount:", font=("Courier", 10, "bold"))
amount_label.grid(column=0, row=4, pady=5, sticky="e")
amount_entry = Entry(width=40)
amount_entry.grid(column=1, row=4, pady=5)

add_button = Button(text="Add Expense", font=("Courier", 10, "bold"), width=29,
                    command=lambda: add_exp())
add_button.grid(column=1, row=5, pady=5)

show_summary = Button(text="Show Summary", font=("Courier", 10, "bold"), width=29, command=summary)
show_summary.grid(column=1, row=6, pady=5)

export_report = Button(text="Export Report", font=("Courier", 10, "bold"), width=29, command=export_report)
export_report.grid(column=1, row=7, pady=5)

search_for = Label(text="Search For:", font=("Courier", 10, "bold"))
search_for.grid(column=3, row=1, sticky="e", pady=5)
search_combobox = ttk.Combobox(state="readonly",
                               values=["Housing / Rent", "Food & Groceries", "Transportation", "Bills & Utilities",
                                       "Healthcare & Medical", "Shopping & Personal Care", "Entertainment & Leisure",
                                       "Savings & Investments", "Loans & EMIs", "Miscellaneous", "Others"],
                               width=37
                               )
search_combobox.grid(column=4, row=1, pady=5)

search_button = Button(text="Search", font=("Courier", 10, "bold"), width=10, command=search_exp)
search_button.grid(column=4, row=2, pady=5)

today_report_button = Button(text="Show Today's report", font=("Courier", 10, "bold"), width=22, command=get_today_report)
today_report_button.grid(column=4, row=6, pady=5)

monthly_report_button = Button(text="Show this month report", font=("Courier", 10, "bold"), command=monthly_report)
monthly_report_button.grid(column=4, row=7, pady=5)

radio_state = IntVar()
radio_button1 = Radiobutton(text="Dark", value=1, variable=radio_state, font=("Courier", 10, "bold"), command=mode_selector)
radio_button2 = Radiobutton(text="Light", value=2, variable=radio_state, font=("Courier", 10, "bold"), command=mode_selector)
radio_button1.grid(column=4, row=0, pady=5, sticky="e")
radio_button2.grid(column=5, row=0, pady=5, sticky="w")
radio_button2.select()

window.mainloop()
