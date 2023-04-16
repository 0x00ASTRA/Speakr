import tkinter as tk

class View:
    def __init__(self):
        self.controller = None
        self.extract_button = None
        self.chat_button = None

        # create main window
        self.root = tk.Tk()
        self.root.title("Text Extractor and Chatbot")

        # create frame for file input and extraction
        self.file_frame = tk.Frame(self.root)
        self.file_frame.pack(pady=10)

        # create label and entry for file input
        self.file_label = tk.Label(self.file_frame, text="Enter file path or URL:")
        self.file_label.pack(side=tk.LEFT, padx=5)
        self.file_entry = tk.Entry(self.file_frame, width=50)
        self.file_entry.pack(side=tk.LEFT, padx=5)

        # create frame for chat input and output
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(pady=10)

        # create chat output area
        self.chat_output = tk.Text(self.chat_frame, height=20, width=70)
        self.chat_output.pack(pady=10)

        # create label and entry for chat input
        self.chat_label = tk.Label(self.chat_frame, text="Ask me anything:")
        self.chat_label.pack(side=tk.LEFT, padx=5)
        self.chat_entry = tk.Entry(self.chat_frame, width=50)
        self.chat_entry.pack(side=tk.LEFT, padx=5)
    
    def create_buttons(self):
        if self.controller is not None:
            # create extract button
            self.extract_button = tk.Button(self.file_frame, text="Extract Text", command=self.controller.extract_text)
            self.extract_button.pack(side=tk.LEFT, padx=5)

            # create chat button
            self.chat_button = tk.Button(self.chat_frame, text="Send", command=self.controller.send_chat)
            self.chat_button.pack(side=tk.LEFT, padx=5)

    def register_extract_event_listener(self, listener):
        if self.extract_button is not None:
            self.extract_button.bind("<Button-1>", listener)
    
    def register_ask_event_listener(self, listener):
        if self.chat_button is not None:
            self.chat_button.bind("<Button-1>", listener)

    def get_input_type(self):
        return self.file_entry.get().split(".")[-1]
    
    def get_input_value(self):
        return self.file_entry.get()
    
    def set_extracted_text(self, text):
        self.chat_output.insert(tk.END, text)
    
    def get_extracted_text(self):
        return self.chat_output.get("1.0", tk.END)
    
    def get_question(self):
        return self.chat_entry.get()

    def update_ui(self):
        self.create_buttons()

    def run(self):
        self.root.mainloop()