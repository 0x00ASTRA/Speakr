import openai
import os
import time

try:
    src_dir = os.path.dirname(os.path.realpath(__file__))
    print(src_dir)
    with open(f'{src_dir}/openai_api_key.txt', 'r') as f:
        openai.api_key = f.read()
except FileNotFoundError:
    print('Please create a file called openai_api_key.txt with your OpenAI API key in it.')
    exit(1)

class Chat:
    def __init__(self, prompt, context):
        self.fullprompt = f'{prompt}: {context}\n'
        self.prompt = f'{prompt}: '
        self.context = f'{context}\n'
        self.response = None

    # needs fixing(!)

    def segment_text(self, text, segment_size=4096):
        segments = []
        while len(text) > segment_size:
            segment = text[:segment_size]
            segments.append(segment)
            text = text[segment_size:]
        segments.append(text)
        return segments

    def get_response(self):
        segments = self.segment_text(self.context)
        responses = []

        for segment in segments:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': 'You are a Helpful assistant named Ada.'},
                    {'role': 'user', 'content': self.prompt + segment}
                ]
            )
            responses.append(response)
            time.sleep(2)
        self.response = ''.join(responses)
        return self.response