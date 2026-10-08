from email.message import EmailMessage
import smtplib
import os

########################################
# 1. Fill in placeholders
########################################

TO_EMAIL_1 = "rick@example.com"
TO_EMAIL_2 = "batman@example.com"
FROM_EMAIL = "morty@example.com"
APP_PASSWORD = "YOUR_APP_PASSWORD_FROM_GOOGLE"

# Or, store the sensitive data in your .bashrc
# APP_PASSWORD = os.getenv("APP_PASSWORD")
# FROM_EMAIL = os.getenv("FROM_EMAIL")

########################################
# 2. List business contacts and their data
########################################

business_contacts = [
    {
    "name": "Rick",
    "email": TO_EMAIL_1,
    "project": "AI World Domination System",
    "report": "rick_report.pdf",
    "known_issue": "the agents forming a union and asking for dental"
    },
    {
    "name": "Batman",
    "email": TO_EMAIL_2,
    "project": "GPU-Powered Bat-Signal",
    "report": "batman_report.pdf",
    "known_issue": "an alarming increase in the local bat population"
    }
]

########################################
# Connect to your Gmail account
########################################

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
	email_server.login(
		FROM_EMAIL,
		APP_PASSWORD
		)

	########################################
	# Customize email message for each contact
	########################################

	for contact in business_contacts:
		message = EmailMessage()

		message["Subject"] = contact["project"] + " Status Update"
		message["From"] = FROM_EMAIL
		message["To"] = contact["email"]

		message.set_content(
			f"""
Hi {contact['name']},

I have an update on the {contact['project']}.

Everything is running according to plan. 
However, we're currently dealing with {contact['known_issue']}.

I'd appreciate your input on the matter.

PS. Full report is attached.
Morty
"""
			)

		########################################
		# Add attachments
		########################################
		
		report_pdf = open(contact["report"], "rb").read()
		message.add_attachment(
			report_pdf,
			maintype="application",
			subtype="pdf",
			filename=contact["report"]
			)

		########################################
		# Send the customized email
		########################################

		email_server.send_message(message)

		print("email was sent to", contact["name"])