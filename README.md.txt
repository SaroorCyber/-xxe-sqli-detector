# 🛡️ XXE and SQL Injection Detector

This is a beginner-friendly Python GUI tool to **detect XXE (XML External Entity) and SQL Injection** patterns from a given website URL. The tool is designed for cybersecurity students and aspiring SOC Analysts to practice static detection logic and pattern matching.

## 📌 Features

- ✅ Detects common **XXE injection** payload patterns
- ✅ Scans for **SQL Injection** keywords in website response
- ✅ GUI interface using **Tkinter**
- ✅ Easy to use: just paste a URL and click “Start Testing”

---

## 🚀 How It Works

- Takes user input (URL)
- Uses `requests` to fetch the HTML content
- Applies regular expressions and keyword checks
- Displays alerts if known malicious patterns are found

---

## 📷 GUI Preview

*(Add screenshot if you want)*

---

## 🧪 Sample Vulnerabilities Detected

- `<!DOCTYPE ... <!ENTITY ... SYSTEM "file://...">`  → XXE Pattern  
- `SELECT * FROM users WHERE ...` → SQL Injection Pattern

---

## 🔧 Requirements

Make sure you have Python 3 installed.

Install the required libraries:
```bash
pip install requests
