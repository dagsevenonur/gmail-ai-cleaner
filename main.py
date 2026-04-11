from client import GmailApi

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
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()