# Send Emails with Python 📧🐍
Send personalized emails automatically with Python SMTP & Gmail

## Video Tutorial 🎥
This code is written step by step in my **Python Simplified** tutorial: 
<br>
**Send Emails with Python 📧 SMTP, Attachments & Personalization**.

<a href="https://youtu.be/WA7GC9DP8tw" target="_blank"><img width="600" alt="Send Emails with Python SMTP Thumbnails" src="https://github.com/user-attachments/assets/49691bd6-5fcd-4ffc-98a2-ff873a39d34d" /></a>

## 🚀 What does this code do?
- Create emails with `email.message.EmailMessage`
- Connect to Gmail securely with `smtplib` and SMTP
- Send personalized messages to multiple contacts using a loop and f-strings
- Attach PDF reports to emails
- Keep your email address and app password outside your Python code using environment variables

## 📁 Project Files

```text
send_emails/
├── app.py              # Main email automation script
├── rick_report.pdf     # Example attachment for Rick
├── batman_report.pdf   # Example attachment for Batman
├── pickle.png          # Example image file
└── README.md
```

The current `app.py` uses the two PDF files. `pickle.png` is included in the repository but isn't attached by the final script.

## 🛠️ Requirements

- Python 3
- A Gmail account with **2-Step Verification** enabled and an **App Password** (where supported by your Google account)

No third-party Python packages are required! The project uses `email`, `smtplib`, and `os` from the Python standard library.

## ⚙️ Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/MariyaSha/send_emails.git
cd send_emails
```

**2. Set up your Gmail App Password**

Enable 2-Step Verification on your Google account, then create an App Password if that option is available to your account. Use that App Password for SMTP authentication — **not your regular Google password**.

Google's instructions: https://support.google.com/accounts/answer/185833

**3. Configure your sender and recipients**

Open `app.py` and replace the example addresses:

```python
TO_EMAIL_1 = "rick@example.com"
TO_EMAIL_2 = "batman@example.com"
FROM_EMAIL = "morty@example.com"
```

The script includes a placeholder for `APP_PASSWORD`. For a quick local experiment, you can replace it, but **don't commit real passwords to GitHub**. The safer approach is to use environment variables as shown below.

**4. Recommended: Store credentials outside your code**

On Linux, WSL, or a Bash terminal, add these lines to your `~/.bashrc` file (using your own details):

```bash
export FROM_EMAIL="your_email@gmail.com"
export APP_PASSWORD="your_google_app_password"
```

Load the changes into your current shell:

```bash
source ~/.bashrc
```

Then, in `app.py`, comment out the hard-coded `FROM_EMAIL` and `APP_PASSWORD` assignments and uncomment the existing environment-variable lines:

```python
APP_PASSWORD = os.getenv("APP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")
```

> **Security note:** Never commit actual credentials, share screenshots containing them, or upload your personal `.bashrc` file. Environment variables keep secrets out of the script, but a local shell configuration file still needs appropriate access protection.

**5. Run the script**

From the repository folder (so Python can find the PDF attachments):

```bash
python app.py
```

The script connects to Gmail with `smtplib.SMTP_SSL("smtp.gmail.com", 465)`, logs in, loops through `business_contacts`, creates a customized `EmailMessage` for each contact, attaches the corresponding PDF, and sends it.

Before running, make sure you've replaced the example recipient addresses with addresses you control or have permission to email.

## ✏️ Make It Your Own

Edit the `business_contacts` list in `app.py` to change the recipients, names, projects, known issues, and PDF filenames. Each contact can have a different subject, email body, and attachment.

If you add new PDF files, keep them in the repository folder or update their paths in the script.

## 😀 Thanks for reading!
