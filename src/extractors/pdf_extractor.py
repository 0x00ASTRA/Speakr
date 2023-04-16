import PyPDF2 as pdf2

class PDFExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_file = open(self.file_path, 'rb')
        self.pdf_reader = pdf2.PdfReader(self.pdf_file)
        self.pdf_writer = pdf2.PdfWriter()
        self.num_pages = len(self.pdf_reader.pages)

    def extract(self, page_num):
        page = self.pdf_reader.getPage(page_num)
        self.pdf_writer.addPage(page)
        return self.pdf_writer

    def extract_all(self):
        for page_num in range(self.num_pages):
            self.extract(page_num)
    
    def extract_text(self, page_num):
        page = self.pdf_reader.pages[page_num]
        return page.extract_text()
    
    def extract_all_text(self):
        text = ''
        for page_num in range(self.num_pages):
            text += self.extract_text(page_num)
        return text

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            self.pdf_writer.write(f)