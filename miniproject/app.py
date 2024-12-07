import tkinter as tk
from tkinter import messagebox


def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
    list3 = list1 + ["*"] + list2
    return [list3, False]


def calculate_flames():
    p1 = player1_entry.get().strip().lower().replace(" ", "")
    p2 = player2_entry.get().strip().lower().replace(" ", "")

    if not p1 or not p2:
        messagebox.showerror("Input Error", "Please enter both names!")
        return

    p1_list = list(p1)
    p2_list = list(p2)

    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[: star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left
        else:
            result = result[: len(result) - 1]

    relationship = result[0]
    messagebox.showinfo("FLAMES Result", f"Relationship status: {relationship}")


# GUI Setup
root = tk.Tk()
root.title("FLAMES Relationship Game")
root.geometry("400x300")
root.config(bg="#FFB6C1")

# Header
header = tk.Label(
    root, text="FLAMES Relationship Game", font=("Helvetica", 16, "bold"), bg="#FF69B4", fg="white", pady=10
)
header.pack(fill=tk.X)

# Frame for Inputs
frame = tk.Frame(root, bg="#FFB6C1")
frame.pack(pady=20)

# Player 1 Name
tk.Label(frame, text="Player 1 Name:", font=("Arial", 12), bg="#FFB6C1").grid(row=0, column=0, padx=10, pady=10, sticky="w")
player1_entry = tk.Entry(frame, width=30, font=("Arial", 12))
player1_entry.grid(row=0, column=1, padx=10, pady=10)

# Player 2 Name
tk.Label(frame, text="Player 2 Name:", font=("Arial", 12), bg="#FFB6C1").grid(row=1, column=0, padx=10, pady=10, sticky="w")
player2_entry = tk.Entry(frame, width=30, font=("Arial", 12))
player2_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to Calculate
calculate_button = tk.Button(
    root, text="Calculate Relationship", font=("Arial", 12, "bold"), bg="#FF1493", fg="white", padx=10, pady=5, command=calculate_flames
)
calculate_button.pack(pady=20)

# Footer
footer = tk.Label(
    root, text="Find out your relationship status!", font=("Helvetica", 10, "italic"), bg="#FFB6C1", fg="#333"
)
footer.pack()

# Run the Application
root.mainloop()
