from transformers import pipeline
from simplet5 import SimpleT5
import os
import pathlib

model = SimpleT5()
model.load_model("t5", "./model-t5-small", use_gpu=False)


def para_summarizer(text):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    return summarizer(text, max_length=200, min_length=30, do_sample=False)[0][
        "summary_text"
    ]


def para_summarize_v2(text):
    return model.predict(f"summarize:{text}")[0]
