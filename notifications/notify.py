import os
import time
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# List of client numbers
client_numbers = ["0777322874", "0773123456", "077654327"]  # Add more client numbers here

# Your phone number (to receive notifications)
notification_number = "0721322874"

# Define the ADB command to send USSD command
def send_ussd_command(ussd_code):
    os.system(f'adb shell am start -a android.intent.action.VIEW -d "tel:{ussd_code}"')
    time.sleep(5)  # Wait for USSD response to load

# Fetch balance and expiry data (simplified response parsing)
def fetch_data_balance():
    send_ussd_command("*131#")  # USSD code to check balance
    time.sleep(3)  # Allow time for USSD response to load
    # The command below is used to capture the output of the USSD response from the phone
    result = os.popen("adb logcat -d | grep USSD").read()
    return result

# Check the data balance and expiry date for each client
def check_and_notify():
    for client_number in client_numbers:
        # Simulate fetching balance and expiry
        data_response = fetch_data_balance()
        
        # Example parsed response: Balance 50MB, Expiry Date 30/01/2025
        remaining_data = 50  # Example value, parse the actual response
        expiry_date = datetime(2025, 1, 30)  # Example expiry date, parse the actual date

        # Check if data is below 20%
        if remaining_data < 20:
            notify_client(client_number, "Your data balance is below 20%.")

        # Check if the expiry is within 4 days
        if expiry_date <= datetime.now() + timedelta(days=4):
            notify_client(client_number, f"Your data expires on {expiry_date.strftime('%d-%m-%Y')}.")

        # Notify you (admin) about the client
        notify_admin(client_number)

# Function to send SMS/Email notification to the client (to the specified number)
def notify_client(phone_number, message):
    # Implement your notification mechanism (e.g., send an SMS or email to the client)
    print(f"Notifying client {phone_number}: {message}")

# Function to send email notification to you (admin)
def notify_admin(client_number):
    admin_message = f"Client {client_number} has a low balance or their data is near expiry."
    print(admin_message)

    # Send an email to admin (you)
    send_email("your_email@example.com", "Client Data Alert", admin_message)

# Function to send email (using Gmail as an example)
def send_email(to_email, subject, body):
    from_email = "your_email@gmail.com"
    password = "your_email_password"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# Run the check daily
if __name__ == "__main__":
    check_and_notify()
