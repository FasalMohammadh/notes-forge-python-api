from transformers import pipeline


def para_summarizer(text):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    summarized = summarizer(text, max_length=200, min_length=30, do_sample=False)[0][
        "summary_text"
    ]

    return summarized
