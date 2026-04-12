from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from base64 import urlsafe_b64decode

from auth import authenticate

class GmailApi:
    def __init__(self):
        creds = authenticate()
        self.service = build("gmail", "v1", credentials=creds)
    
    def get_emails(self):
        request = self.service.users().messages().list(userId="me")
        result = self._execute_request(request)
        
        try:
            messages = result["messages"]
        except KeyError:
            print("No messages found.")
            return []
        
        emails = []
        for msg in messages:
            detail = self.service.users().messages().get(
                userId="me", 
                id=msg["id"],
                format="full",
                metadataHeaders=["Subject", "From", "Date"]
            ).execute()
            
            headers = detail["payload"]["headers"]
            snippet = detail["snippet"] 
            payload = detail["payload"]
            decoded_payload = self.decode_payload(payload)
            email = {"id": msg["id"], "snippet": snippet, "payload": decoded_payload}
            for header in headers:
                email[header["name"].lower()] = header["value"]
            
            emails.append(email)
        return emails
    
    def delete_email(self, email_id):
        try:
            request = self.service.users().messages().trash(userId="me", id=email_id)
            self._execute_request(request)
            print(f"Email with ID {email_id} has been trashed.")
        except HttpError as e:            
            print(f"An error occurred while trashing email with ID {email_id}: {e}")
        
    def decode_payload(self, payload):
        if "data" in payload:
            return urlsafe_b64decode(payload["data"]).decode("utf-8")
        elif "parts" in payload:
            for part in payload["parts"]:
                decoded = self.decode_payload(part)
                if decoded:
                    return decoded
        return None

    @staticmethod
    def _execute_request(request):
        try:
            return request.execute()
        except HttpError as e:
            print(f"An error occurred: {e}")
            raise RuntimeError(e)