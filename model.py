import ollama
import yaml

class AI:
    def __init__(self):
        self.model = 'llama3.2'

    @staticmethod
    def load_instructions(file_path):
        try:
            with open(file_path, 'r') as file:
                instructions = yaml.safe_load(file)
                ollama_config = instructions.get('ollama', {})
                model = ollama_config.get('model', 'llama3.2')
                system = ollama_config.get('system', '')
                return model, system
        except Exception as e:
            print(f"Error loading instructions: {e}")
            return ""
    
    def analyze_email(self, email):
        try:
            model, system = self.load_instructions('config.yaml')
            self.model = model
            self.system = system
            response = ollama.chat(
                model=self.model,
                messages=[
                    {'role': 'system', 'content': self.system},
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