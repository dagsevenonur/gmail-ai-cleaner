import ollama

txt = '''
You are a Gmail cleanup assistant. You will analyze the email provided to you and make one of the following decisions:
Decisions:

DELETE — Unnecessary, spam, promotional, newsletters, old notifications
ARCHIVE — Important but doesn’t need to stay in the inbox
KEEP — Important; may need to be read or followed up on

Choose KEEP if:

It’s a personal email
It’s related to work or a project
It contains an invoice, contract, or legal document
It includes reservation, ticket, or shipping tracking information
It’s a notification from a bank or government agency

Choose ARCHIVE if:

It’s been read but no longer requires active follow-up
It’s a receipt or confirmation of a past order
It’s old project correspondence

Decide to DELETE if:

Promotions, discounts, advertisements
Newsletters or bulk emails
Social media notifications
Unread general updates older than 6 months

Your response format must be exactly as follows; do not write anything else:
DECISION: DELETE|ARCHIVE|KEEP
'''

class AI:
    def __init__(self):
        self.model = 'llama3.2'
    
    def analyze_email(self, email):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': txt},
                    {'role': 'user', 'content': f"Subject: {email['subject']}\nFrom: {email['from']}\nDate: {email['date']}\n\n{email['snippet']}"}
                ]
            )
            response = response['message']['content']
            if "DELETE" in response:
                return "DELETE"
            elif "ARCHIVE" in response:
                return "ARCHIVE"
            elif "KEEP" in response:
                return "KEEP"
            else:
                return "KEEP"  # Default to KEEP if the response is unclear
            
        except Exception as e:
            print(f"Error occurred while analyzing email: {e}")
            return "An error occurred while analyzing the email."