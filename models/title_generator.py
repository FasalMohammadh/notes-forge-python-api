from transformers import pipeline


def generateTitle(text):
    summarizer = pipeline("summarization", model="TusharJoshi89/title-generator")
    summary = summarizer(text)[0]["summary_text"]

    return summary
