from client import GmailApi
from model import AI

def main():
    print("Welcome to the Gmail AI Cleaner!")
    print("This tool will help you clean up your Gmail inbox using AI.")
    print("Press Enter to continue...")
    input()

    client = GmailApi()
    emails = client.get_emails()
    print(f"Found {len(emails)} emails in your inbox.")
    print("Analyzing emails with AI...")
    emails = emails[:10]  # Limit to first 10 emails for analysis
    ai = AI()
    for email in emails:
        print (f"Subject: {email['subject']}")
        response = ai.analyze_email(email)
        print(f"AI Analysis: {response}")
        client.delete_email(email['id'])
        print("Email deleted.\n")
        
if __name__ == "__main__":
    main()