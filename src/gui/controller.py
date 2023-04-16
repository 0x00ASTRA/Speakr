from src.gui.view import View
from src.gui.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model
        self.view.register_extract_event_listener(self.handle_extract_button_click)
        self.view.register_ask_event_listener(self.handle_ask_button_click)

    def handle_extract_button_click(self, event):
        input_type = self.view.get_input_type()
        input_value = self.view.get_input_value()

        if input_type == 'pdf':
            text = self.model.extract_text_from_pdf(input_value)
        elif input_type == 'web':
            text = self.model.extract_text_from_web(input_value)
        elif input_type == 'text':
            text = self.model.extract_text_from_text(input_value)
        else:
            self.view.show_error_message("Invalid input type.")

        self.view.set_extracted_text(text)

    def handle_ask_button_click(self, event):
        question = self.view.get_question()
        text = self.view.get_extracted_text()

        if not text:
            self.view.show_error_message("Please extract text first.")
        elif not question:
            self.view.show_error_message("Please enter a question.")
        else:
            answer = self.model.generate_text(question, text)
            self.view.set_answer_text(answer)

    def extract_text(self):
        input_type = self.view.get_input_type()
        input_value = self.view.get_input_value()
        if input_type == 'pdf':
            text = self.model.extract_text_from_pdf(input_value)
        elif input_type == 'web':
            text = self.model.extract_text_from_web(input_value)
        elif input_type == 'text':
            text = self.model.extract_text_from_text(input_value)
        else:
            self.view.show_error_message("Invalid input type.")
        self.view.set_extracted_text(text)
        return text
    
    def send_chat(self):
        question = self.view.get_question()
        text = self.view.get_extracted_text()
        self.model.get_chat_response(question=question, text=text)

    def run(self):
        self.view.run()