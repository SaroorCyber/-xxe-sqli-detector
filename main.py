import re
import requests
import tkinter as tk
from tkinter import messagebox

def detect_xxe(input_string):
    xxe_patterns = [
        r'<!DOCTYPE\s+[\w\s"\'=-]*\[\s*<!ENTITY\s+\w+\s+SYSTEM',
        r'<!ENTITY\s+\w+\s+SYSTEM\s+["\']file://',
    ]

    for pattern in xxe_patterns:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    return False

def detect_sql_injection(input_string):
    sql_injection_keywords = [
        'SELECT', 'INSERT', 'UPDATE', 'DELETE', 'DROP', 'UNION', '--', ';'
    ]

    for keyword in sql_injection_keywords:
        if keyword in input_string.upper():
            return True
    return False

def test_vulnerabilities():
    user_url = url_entry.get()

    try:
        response = requests.get(user_url)
        if response.status_code == 200:
            content = response.text

            xxe_detected = detect_xxe(content)
            sql_injection_detected = detect_sql_injection(content)

            if xxe_detected or sql_injection_detected:
                message = "Vulnerabilities detected:\n\n"
                if xxe_detected:
                    message += "XXE Injection\n"
                if sql_injection_detected:
                    message += "SQL Injection\n"
                warning_label.config(text=message, fg="red")
            else:
                warning_label.config(text="No vulnerabilities detected.", fg="green")
        else:
            warning_label.config(text="Failed to retrieve website content.", fg="red")

    except requests.exceptions.RequestException as e:
        warning_label.config(text=f"An error occurred: {e}", fg="red")

# Create the main application window
root = tk.Tk()
root.title("XXL and SQL Detector")

# Create GUI elements
top_heading = tk.Label(root, text="XXL and SQL Detector", font=("Helvetica", 16, "bold"))
top_heading.pack(pady=10)

label = tk.Label(root, text="Enter the website URL:")
label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

test_button = tk.Button(root, text="Start Testing", command=test_vulnerabilities)
test_button.pack()

warning_label = tk.Label(root, text="", fg="black")
warning_label.pack()

root.mainloop()
