import docx2txt

class WordExtractor:
    # extract data from word files
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = docx2txt.process(self.file_path)
        self.title = ''
        self.description = ''
        self.keywords = ''
        self.all = {}
    
    def get_text(self):
        return self.text
    
    def get_title(self):
        # extract title from the first line of text
        self.title = self.text.split('\n')[0]
        return self.title
    
    def get_description(self):
        # extract description from the second line of text
        self.description = self.text.split('\n')[1]
        return self.description
    
    def get_keywords(self):
        # extract keywords from the third line of text
        self.keywords = self.text.split('\n')[2]
        return self.keywords
    
    def get_all(self):
        self.all = {
            'title': self.get_title(),
            'description': self.get_description(),
            'keywords': self.get_keywords(),
            'text': self.get_text()
        }
        return self.all
    
    def save(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.text)