# summarizer.py
from transformers import BartTokenizer, BartForConditionalGeneration

class TextSummarizer:
    def __init__(self):
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    def summarize_text(self, text):
        inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

if __name__ == "__main__":
    text = """ Pakistan partied late into the night after javelin thrower Arshad Nadeem won the country’s first ever Olympic track and field medal with a Games record throw of 92.97 meters to take gold in Paris.

The normally cricket-mad nation stayed up late Thursday night to watch Nadeem clinch Pakistan’s first Olympic medal since the men’s field hockey team won bronze in Barcelona 32 years ago.

“Our brother has won the gold medal and I’ve lost my voice because I’ve been celebrating all night,” his brother Shahid Nadeem told CNN on Friday from the family’s home in Mian Channu, in Pakistan’s Punjab state.

“When he gets home we will celebrate him in such a way that the world will never forget! We are simple people and will celebrate with kheer (local rice pudding) and whatever Allah gives us, we are happy!” he said.

"""
    summarizer = TextSummarizer()
    print(summarizer.summarize_text(text))