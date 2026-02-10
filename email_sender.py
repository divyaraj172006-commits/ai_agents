import smtplib
from email.mime.text import MIMEText
from secrets import sender_email, receiver_email, app_password
# Email details

subject = "Hello from Python"
body = "Hi 👋\n\nThis email was sent using Python.\n\nThanks!"

# Create email
msg = MIMEText(body)
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("✅ Email sent successfully!")