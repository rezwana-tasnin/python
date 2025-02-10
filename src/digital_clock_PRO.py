import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x300")
root.configure(bg="black")

# Create a frame for the day names
day_frame = tk.Frame(root, bg="black")
day_frame.pack(pady=5)

# Weekday labels
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_labels = {}

for day in weekdays:
    label = tk.Label(day_frame, text=day, font=("Digital-7", 18, "bold"), bg="black", fg="#444")  # Default color: dim gray
    label.pack(side="left", padx=10)
    day_labels[day] = label  # Store in dictionary for easy update

# Create a frame for the clock and AM/PM
clock_frame = tk.Frame(root, bg="black")
clock_frame.pack()

# Create a label for the time (big and bold)
clock_label = tk.Label(clock_frame, font=("Digital-7", 120, "bold"), bg="black", fg="red")
clock_label.pack(side="left")

# Create a smaller label for AM/PM
ampm_label = tk.Label(clock_frame, font=("Digital-7", 30, "bold"), bg="black", fg="red")
ampm_label.pack(side="left", padx=10)

# Create a label for the date (DD/MM/YYYY)
date_label = tk.Label(root, font=("Digital-7", 24, "bold"), bg="black", fg="red")
date_label.pack(pady=5)

# Update the clock, date, and highlight the current day
def update_clock():
    # current_time = time.strftime("%H:%M:%S")  # Get current time
    current_time = time.strftime("%I:%M:%S")  # 12-hour format
    am_pm = time.strftime("%p")  # AM or PM
    current_day = time.strftime("%a")  # Current day (Mon, Tue, etc.)
    current_date = time.strftime("%d/%m/%Y")  # Date in DD/MM/YYYY format

    # Update time and AM/PM labels
    clock_label.config(text=current_time)
    ampm_label.config(text=am_pm)
    date_label.config(text=current_date)

    # Highlight the current day in red, others in dim gray
    for day, label in day_labels.items():
        label.config(fg="red" if day == current_day else "#444")

    clock_label.after(1000, update_clock)  # Refresh every second

# Start the clock
update_clock()

root.mainloop()
