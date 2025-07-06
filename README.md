# 📧 Mail ID Validator

A Python + Streamlit based web application that validates email addresses across multiple layers — ensuring real, usable, and quality email data.

---

## 🚀 Project Overview

**Mail ID Validator** is a lightweight, user-friendly tool that performs comprehensive email validation through:

- Format checking
- Domain verification
- Disposable email detection
- Optional SMTP mailbox validation

It helps developers, marketers, and businesses prevent fake or incorrect email entries, making it ideal for signup forms, lead capture tools, and B2B platforms.

---

## ✅ Features

- 🔍 **Format Validation**: Ensures the email syntax is valid using regex.
- 🌐 **Domain Verification**: Checks if the domain (like gmail.com) exists using DNS lookup.
- 🚫 **Disposable Email Detection**: Flags temporary email providers (e.g., mailinator.com, 10minutemail).
- 📡 **SMTP Mailbox Validation**: Verifies if the email inbox actually exists.
- 🖥️ **Streamlit Interface**: Clean and intuitive UI for instant use.

---

## 💡 Problem It Solves

Poor quality email addresses hurt deliverability, conversions, and user trust.

This tool helps:
- Prevent fake signups
- Maintain clean mailing lists
- Improve onboarding and lead capture accuracy

---

## 🛠️ Tech Stack

- **Python 3.12.7**
- **Streamlit** – For frontend & UI
- **dnspython** – For domain MX record lookup
- **validate_email_address** – For SMTP-based mailbox verification
- **re (Regex)** – For syntax validation

---

## 📦 Installation

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run mailid_validator.py
```



### 🔄 Example Use

1. Launch the app  
2. Enter any email ID in the input field  
3. Click **Validate**  
4. Get a complete validation report in real-time  

📁 Sample Output

```bash

Email: user@gmail.com  
Valid Format: ✅  
Domain Exists: ✅  
Disposable: ❌  
SMTP Check: ✅  
```
---

## 📡 Live Demo

Check out the live application here:  
👉 [Mail ID Validator on Streamlit](https://mailidvalidator.streamlit.app/)

---

### 📄 License
This project is open-source and available under the MIT License.

---
### 📬 Feedback & Contribution
Your feedback is highly appreciated 🙌
Feel free to open an issue, suggest improvements, or contribute via pull requests.

Made with ❤️ using Python & Streamlit




