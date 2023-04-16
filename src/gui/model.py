from src.extractors.pdf_extractor import PDFExtractor
from src.extractors.word_extractor import WordExtractor
from src.extractors.web_extractor import WebExtractor
from src.chat.chat import Chat

class Model:
    def __init__(self):
        self.text = ''

    def extract_text_from_pdf(self, file_path):
        pdf_extractor = PDFExtractor(file_path)
        return pdf_extractor.extract_all_text()

    def extract_text_from_web(self, url):
        web_extractor = WebExtractor(url)
        return web_extractor.extract_text()

    def extract_text_from_word(self, file_path):
        text_extractor = WordExtractor(file_path)
        return text_extractor.extract_text()
    
    def get_chat_response(self, question, text):
        chat = Chat(prompt=question, context=text)
        return chat.get_response()