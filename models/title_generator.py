from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import nltk

cache_dir = "/title-generator"

tokenizer = AutoTokenizer.from_pretrained(
    "fabiochiu/t5-small-medium-title-generation", cache_dir=cache_dir
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    "fabiochiu/t5-small-medium-title-generation", cache_dir=cache_dir
)


def generateTitle(text):
    summarizer = pipeline("summarization", model="TusharJoshi89/title-generator")
    summary = summarizer(text)[0]["summary_text"]

    return summary


def generate_title_v2(text):

    inputs = [f"summarize: {text}"]

    inputs = tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(
        **inputs, num_beams=8, do_sample=True, min_length=10, max_length=64
    )
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    return nltk.sent_tokenize(decoded_output.strip())[0]
