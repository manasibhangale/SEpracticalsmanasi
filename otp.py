import smtplib
import random
from validate_email_address import validate_email

def generate_otp(length=6):
    """
    Generate a random OTP of specified length (default is 6).
    Length must be between 4 and 8 digits.
    """
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8.")
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_email(email, otp):
    """
    Send OTP to the specified email address using SMTP.
    """
    # Validate the email address
    if not validate_email(email):
        raise ValueError("Invalid email address.")

    # Properly formatted email message with Subject
    sender_email = "manasibhangale2004@gmail.com"  # Your Gmail address
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"
    message = f"Subject: {subject}\n\n{body}"  # Include subject and body

    try:
        # Connect to Gmail's SMTP server securely using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, 'qlun mynq vzxz vheq')  # Replace with your app password
            smtp.sendmail(sender_email, email, message)
            print(f"OTP sent to {email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    """
    Main function to generate OTP and send it via email.
    """
    email = input("Enter the recipient's email address: ")
    try:
        otp = generate_otp(length=6)  # Generate a 6-digit OTP
        send_email(email, otp)  # Send the OTP to the email
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
