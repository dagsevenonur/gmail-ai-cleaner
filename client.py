from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from auth import authenticate

class GmailApi:
    def __init__(self):
        creds = authenticate()
        self.service = build("gmail", "v1", credentials=creds)
    
    def get_emails(self):
        request = (
            self.service.users().messages().list(userId="me")
        )
        result = self._execute_request(request)
        try:
            messages = result["messages"]
        except KeyError:
            print(f"No messages found for the sender '{sender}'")
            messages = []
        return messages

    @staticmethod
    def _execute_request(request):
        try:
            return request.execute()
        except HttpError as e:
            print(f"An error occurred: {e}")
            raise RuntimeError(e)