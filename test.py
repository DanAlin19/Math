import tkinter as tk
import random

easyNumbers_array = [
    ["23", "+", "45", "+", "12", "+", "67", "+", "89", "+", "34", "+", "56"],
    ["13", "+", "48", "+", "22", "+", "73", "+", "82", "+", "39", "+", "50"],
    ["31", "+", "59", "+", "14", "+", "78", "+", "97", "+", "41", "+", "63"],
    ["42", "+", "67", "+", "25", "+", "83", "+", "91", "+", "53", "+", "74"],
    ["55", "+", "38", "+", "19", "+", "64", "+", "72", "+", "29", "+", "86"],
    ["17", "+", "64", "+", "33", "+", "79", "+", "88", "+", "47", "+", "65"],
    ["29", "+", "76", "+", "43", "+", "82", "+", "94", "+", "56", "+", "78"],
    ["39", "+", "85", "+", "52", "+", "97", "+", "83", "+", "61", "+", "44"],
    ["48", "+", "57", "+", "63", "+", "91", "+", "76", "+", "38", "+", "52"],
    ["26", "+", "93", "+", "59", "+", "87", "+", "74", "+", "31", "+", "69"]
]

mediumNumbers_array = [
    ["10", "+", "25", "+", "30", "-", "15", "-", "3"],
    ["15", "+", "20", "-", "5", "-", "6", "-", "8"],
    ["40", "-", "10", "-", "2", "+", "7", "+", "13"],
    ["100", "-", "5", "-", "10", "-", "4", "+", "20"],
    ["50", "+", "3", "-", "25", "+", "10", "-", "6"],
    ["18", "+", "27", "-", "12", "-", "8", "-", "5"],
    ["35", "-", "17", "+", "21", "+", "9", "-", "2"],
    ["60", "-", "30", "-", "10", "+", "5", "-", "3"],
    ["25", "+", "35", "-", "15", "-", "9", "+", "12"],
    ["48", "-", "24", "+", "30", "-", "18", "+", "6"]
]

hardNumbers_array = [
    ["34", "+", "72", "-", "17", "*", "3", "+", "12", "/", "31", "*", "9"],
    ["27", "-", "33", "*", "17", "+", "56", "/", "-23", "+", "98", "*", "3"],
    ["15", "*", "7", "-", "68", "+", "7", "/", "11", "*" "-13", "+", "24"],
    ["100", "*", "5", "+", "20", "-", "10", "/", "34", "*", "20", "-", "5"],
    ["50", "+", "3", "-", "25", "+", "10", "-", "6", "*", "2", "/", "13"],
    ["20", "+", "5", "*", "3", "-", "8", "+", "14", "/", "9", "*", "5"],
    ["87", "/", "29", "+", "12", "*", "3", "-", "15", "/", "3", "*", "4"],
    ["30", "+", "18", "*", "2", "/", "16", "-", "10", "*", "3", "/", "2"],
    ["40", "-", "23", "*", "2", "+", "16", "+", "7", "/", "19", "-", "3"],
    ["25", "*", "7", "+", "8", "/", "61", "*", "37", "+", "47", "/", "79"]
    
]

res_easy = [326, 327, 383, 435, 363, 393, 458, 461, 425, 439]
res_medium = [47, 16, 48, 101, 32, 20, 76, 22, 48, 42]
res_hard = [ 81, 300, -28, 295, 2, 45, 40, -6, 0, 2]

visited_easy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
visited_medium = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
visited_hard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

reveal_button = None
answer_label = None
try_again_button = None

def choose_difficulty(difficulty, window):
    global reveal_button, easy_button, medium_button, hard_button

    if difficulty == "Easy":
        index = random.randint(0, len(easyNumbers_array) - 1)
        while visited_easy[index] == 1:
            index = random.randint(0, len(easyNumbers_array) - 1)
        visited_easy[index] = 1
        selected_numbers = easyNumbers_array[index]
        selected_result = res_easy[index]
        
    elif difficulty == "Medium":
        index = random.randint(0, len(mediumNumbers_array) - 1)
        while visited_medium[index] == 1:
            index = random.randint(0, len(mediumNumbers_array) - 1)
        visited_medium[index] = 1
        selected_numbers = mediumNumbers_array[index]
        selected_result = res_medium[index]

    elif difficulty == "Hard":
        index = random.randint(0, len(hardNumbers_array) - 1)
        while visited_hard[index] == 1:
            index = random.randint(0, len(hardNumbers_array) - 1)
        visited_hard[index] = 1
        selected_numbers = hardNumbers_array[index]
        selected_result = res_hard[index]

    hide_buttons()
    countdown(window)
    generate_numbers(window, selected_numbers)
    reveal_button = check_answer(window, selected_result)

def hide_buttons():
    easy_button.pack_forget()
    medium_button.pack_forget()
    hard_button.pack_forget()

def check_answer(window, answer):
    reveal_button = tk.Button(window, text="Reveal Answer", bg="light blue", fg="black", font=("Arial", 60, "bold"), command=lambda: show_answer(window, answer))
    reveal_button.place(relx=0.5, rely=0.5, anchor="center")
    return reveal_button

def show_answer(window, answer):
    global reveal_button, answer_label, try_again_button
    reveal_button.config(state=tk.DISABLED)
    reveal_button.place_forget()
    answer_label = tk.Label(window, text=f"The answer is {answer}", bg="light blue", fg="black", font=("Arial", 80, "bold"))
    answer_label.place(relx=0.5, rely=0.4, anchor="center")
    try_again_button = tk.Button(window, text="Try Again", bg="light blue", fg="black", font=("Arial", 40, "bold"), command=lambda: reset_game(window))
    try_again_button.place(relx=0.5, rely=0.6, anchor="center")

def reset_game(window):
    global reveal_button, answer_label, try_again_button, easy_button, medium_button, hard_button
    if reveal_button:
        reveal_button.config(state=tk.NORMAL)
    if answer_label:
        answer_label.destroy()
    if try_again_button:
        try_again_button.destroy()
    easy_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)
    medium_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)
    hard_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

def countdown(window):
    countdown_label = tk.Label(window, bg="light blue", fg="green", font=("Arial", 500, "bold"))
    countdown_label.place(relx=0.5, rely=0.5, anchor="center")
    for i in range(3, 0, -1):
        countdown_label.config(text=str(i))
        window.update()
        window.after(1000)
    countdown_label.destroy()

def generate_numbers(window, numbers_array):
    for num in numbers_array:
        numbers_label = tk.Label(window, bg="light blue", fg="black", font=("Arial", 500, "bold"))
        numbers_label.place(relx=0.5, rely=0.5, anchor="center")
        numbers_label.config(text=num)
        window.update()
        window.after(2000)
        numbers_label.destroy()

def create_window():
    global easy_button, medium_button, hard_button
    window = tk.Tk()
    window.title("IT BUZZ MATH")
    window.geometry("400x300")
    window.configure(bg="light blue")

    title_label = tk.Label(window, text="IT BUZZ MATH", bg="light blue", fg="black", font=("Arial", 24, "bold"))
    title_label.pack(pady=20)

    button_font = ("Arial", 16, "bold")
    button_width = 10
    button_height = 2

    easy_button = tk.Button(window, text="Easy", bg="light green", fg="black", font=button_font, width=button_width, height=button_height, command=lambda: choose_difficulty("Easy", window), highlightbackground="light green")
    easy_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

    medium_button = tk.Button(window, text="Medium", bg="orange", fg="black", font=button_font, width=button_width, height=button_height, command=lambda: choose_difficulty("Medium", window), highlightbackground="orange")
    medium_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

    hard_button = tk.Button(window, text="Hard", bg="red", fg="black", font=button_font, width=button_width, height=button_height, command=lambda: choose_difficulty("Hard", window), highlightbackground="red")
    hard_button.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

    window.mainloop()

if __name__ == "__main__":
    create_window()
