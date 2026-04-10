from client import GmailApi

def main():
    client = GmailApi()
    emails = client.get_emails()

if __name__ == "__main__":
    main()