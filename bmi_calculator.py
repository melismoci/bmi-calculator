import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get input values from the entry fields
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            result = f"Your BMI is {bmi:.2f}. You are underweight."
        elif 18.5 <= bmi < 24.9:
            result = f"Your BMI is {bmi:.2f}. You are normal weight."
        elif 25 <= bmi < 29.9:
            result = f"Your BMI is {bmi:.2f}. You are overweight."
        else:
            result = f"Your BMI is {bmi:.2f}. You are obese."
        
        # Display the result in a message box
        messagebox.showinfo("BMI Result", result)
    
    except ValueError:
        # Handle errors if inputs are invalid
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height!")

# Create the main application window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")  # Increased window size for better visibility
root.config(bg="green")  # Set the background color to yellow

# Add labels and entry fields for weight and height
tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="green").grid(row=0, column=0, padx=10, pady=10, sticky="e")
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height (m):", font=("Arial", 12), bg="green").grid(row=1, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Add a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
