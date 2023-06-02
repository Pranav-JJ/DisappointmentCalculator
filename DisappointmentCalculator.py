import tkinter as tk
from tkinter import ttk
import webbrowser

# Mapping of grades to numerical values
mapping = {"A+": 10, "A": 9, "B+": 8, "B": 7, "C+": 6, "C": 5, "D": 4, "F": 0}

# Mapping the links based on scores - SGPA
def open_link1(event):
    webbrowser.open("https://youtu.be/G9rLVTzlGdY")
def open_link2(event):
    webbrowser.open("https://youtu.be/nouCx4tQa54")
def open_link3(event):
    webbrowser.open("https://youtu.be/7ncHu9EvQik")

# Mapping the links based on scores - CGPA
def open_link4(event):
    webbrowser.open("https://youtu.be/N9qYF9DZPdw")
def open_link5(event):
    webbrowser.open("https://youtu.be/nouCx4tQa54")
def open_link6(event):
    webbrowser.open("https://youtu.be/O8vzYPDWkDg")  


def calculate_sgpa():
    # Retrieve input values from the entry fields
    credit_values = [
        int(credit_entries[i].get()) for i in range(len(credit_entries))
    ]
    grade_values = [
        mapping[grade_entries[i].get()] for i in range(len(grade_entries))
    ]

    # Calculate weighted total and SGPA
    total = sum(credit_values[i] * grade_values[i] for i in range(len(credit_values)))
    cred_sum = sum(credit_values)
    sgpa = total / cred_sum

    # Display SGPA on the GUI
    sgpa_label["text"] = f"SGPA: {sgpa:.2f}"

    # Additional functionality for SGPA output
    if sgpa >= 9.0:
        additional_labelsgpa["text"] = "Damn homie, you smart af. You're still depressed though, I bet."
        additional_labelsgpa.configure(foreground="green", cursor="hand2")
        additional_labelsgpa.bind("<Button-1>", open_link1)
    elif 8.0 <= sgpa < 9.0:
        additional_labelsgpa["text"] = "Congrats! You live to get depressed another semester!"
        additional_labelsgpa.configure(foreground="blue", cursor="hand2")
        additional_labelsgpa.bind("<Button-1>", open_link2)
    else:
        additional_labelsgpa["text"] = "Congrats! You have reached your one-way destination to depression!"
        additional_labelsgpa.configure(foreground="red", cursor="hand2")
        additional_labelsgpa.bind("<Button-1>", open_link3)


def calculate_cgpa():
    # Retrieve input values from the entry fields
    num_semesters = int(num_semesters_entry.get())
    sgpa_list = []
    for i in range(num_semesters):
        sgpa_per_sem = float(sgpa_entries[i].get())
        sgpa_list.append(sgpa_per_sem)

    # Calculate CGPA
    cgpa = sum(sgpa_list) / num_semesters

    # Display CGPA on the GUI
    cgpa_label["text"] = f"CGPA: {cgpa:.2f}"


    # Additional functionality for CGPA output
    if cgpa >= 9.0:
        additional_labelcgpa["text"] = "Damn homie, you smart af. I have nothing more to add except.. will it last?"
        additional_labelcgpa.configure(foreground="green", cursor="hand2")
        additional_labelcgpa.bind("<Button-1>", open_link4)
    elif 8.0 <= cgpa < 9.0:
        additional_labelcgpa["text"] = "Congrats! Your struggle to reach 9 CGPA begins!"
        additional_labelcgpa.configure(foreground="blue", cursor="hand2")
        additional_labelcgpa.bind("<Button-1>", open_link5)
    else:
        additional_labelcgpa["text"] = "Congrats! You still remain in your one-way destination called depression!"
        additional_labelcgpa.configure(foreground="red", cursor="hand2")
        additional_labelcgpa.bind("<Button-1>", open_link6)

# Create the main window
root = tk.Tk()
root.title("DisappointmentCalculator")

# Create labels for "Credits" and "Grades"
credit_label = tk.Label(root, text="Credits")
credit_label.grid(row=0, column=1, padx=5, pady=5)
grade_label = tk.Label(root, text="Expected Grades")
grade_label.grid(row=0, column=2, padx=5, pady=5)

# List of subjects
subjects = ["Sub1", "Sub2", "Sub3", "Sub4", "EDI", "DT"]

# List to store the entry fields for credits and grades
credit_entries = []
grade_entries = []
sgpa_entries = []  # List to store SGPA entry fields

# Create input fields for credits and grades
for i, subject in enumerate(subjects):
    # Create labels for subjects
    subject_label = tk.Label(root, text=subject)
    subject_label.grid(row=i+1, column=0, padx=5, pady=5)

    # Create entry fields for credits
    credit_entry = tk.Entry(root, width=5)
    credit_entry.grid(row=i+1, column=1, padx=5, pady=5)
    credit_entries.append(credit_entry)

    # Create entry fields for grades
    grade_entry = tk.Entry(root, width=5)
    grade_entry.grid(row=i+1, column=2, padx=5, pady=5)
    grade_entries.append(grade_entry)

# Create a button to calculate SGPA
calculate_sgpa_button = tk.Button(root, text="Calculate SGPA", command=calculate_sgpa)
calculate_sgpa_button.grid(row=len(subjects)+2, column=0, columnspan=3, padx=5, pady=10)

# Create a label to display SGPA
sgpa_label = tk.Label(root, text="SGPA: ")
sgpa_label.grid(row=len(subjects)+3, column=0, columnspan=3, padx=5, pady=10)

# Create a label to display additional SGPA output
additional_labelsgpa = ttk.Label(root, text="")
additional_labelsgpa.grid(row=len(subjects)+4, column=0, columnspan=3, padx=5, pady=10)

# Create a label to display additional CGPA output
additional_labelcgpa = ttk.Label(root, text="")
additional_labelcgpa.grid(row=len(subjects)+13, column=0, columnspan=3, padx=5, pady=10)

# Create input fields for CGPA
num_semesters_label = tk.Label(root, text="Number of Semesters: ")
num_semesters_label.grid(row=len(subjects)+5, column=0, padx=5, pady=5)
num_semesters_entry = tk.Entry(root, width=5)
num_semesters_entry.grid(row=len(subjects)+5, column=1, padx=5, pady=5)

# Create a button to submit the number of semesters
def handle_num_semesters():
    num_semesters = int(num_semesters_entry.get())
    if num_semesters > 0:
        for i in range(num_semesters):
            sgpa_label = tk.Label(root, text=f"Semester {i+1} SGPA: ")
            sgpa_label.grid(row=len(subjects)+7+i, column=0, padx=5, pady=5)
            sgpa_entry = tk.Entry(root, width=5)
            sgpa_entry.grid(row=len(subjects)+7+i, column=1, padx=5, pady=5)
            sgpa_entries.append(sgpa_entry)

        # Enable the "Calculate CGPA" button and CGPA label
        calculate_cgpa_button.grid(row=len(subjects)+7+num_semesters, column=0, columnspan=3, padx=5, pady=10)
        cgpa_label.grid(row=len(subjects)+8+num_semesters, column=0, columnspan=3, padx=5, pady=10)
    else:
        # Disable the "Calculate CGPA" button and CGPA label
        calculate_cgpa_button.grid_forget()
        cgpa_label.grid_forget()

def reset_fields():
    # Clear all input fields
    for entry in credit_entries + grade_entries + sgpa_entries:
        entry.delete(0, tk.END)
    num_semesters_entry.delete(0, tk.END)
    sgpa_label["text"] = "SGPA: "
    cgpa_label["text"] = "CGPA: "
    additional_labelsgpa["text"] = ""
    additional_labelcgpa["text"] = ""

submit_semesters_button = tk.Button(root, text="Submit", command=handle_num_semesters)
submit_semesters_button.grid(row=len(subjects)+5, column=2, padx=5, pady=5)


# Create a label to display CGPA
cgpa_label = tk.Label(root, text="CGPA: ")
cgpa_label.grid(row=len(subjects)+6, column=0, columnspan=3, padx=5, pady=10)

# Create a button to calculate CGPA
calculate_cgpa_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)

# Create a button to reset all fields
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.grid(row=len(subjects)+14, column=0, columnspan=3, padx=5, pady=10)

# Start the GUI main loop
root.mainloop()
