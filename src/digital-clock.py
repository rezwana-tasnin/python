import tkinter as tk
import time

# Create the main theme
root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x250")
root.configure(bg="black")

# Create a label for the time (big and bold)
clock_label = tk.Label(root, font=("Digital-7", 120, "bold"), bg="black", fg="#6f0202", bd=10, relief="ridge")
clock_label.pack(pady=10)

# Update time 
def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Get current time
    # current_time = time.strftime("%I:%M:%S %p")  # Get current time in 12-hour format with AM/PM
    clock_label.config(text=current_time)  # Update time label
    clock_label.after(1000, update_clock)  # Refresh every second

# Start the clock
update_clock()

root.mainloop()
