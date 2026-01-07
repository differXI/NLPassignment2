# ===============================
# Programming Assignment 2
# NLP Data Cleaning & Evaluation
# ===============================

import pandas as pd
import re
import time
import nltk
import textstat
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# -------------------------------
# Configuration
# -------------------------------
CSV_PATH = "Sentiment Analysis Dataset.csv"
TEXT_COL = "SentimentText"

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

# Regex patterns
EMOTICON_RE = re.compile(r"(:\)|:\(|:D|;\)|<3)")
SPECIAL_CHAR_RE = re.compile(r"[^a-zA-Z\s]")
PHONE_RE = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
ACCOUNT_RE = re.compile(r"\b\d{10,16}\b")
ADDRESS_RE = re.compile(r"\b(street|road|rd|ave|avenue|lane|ln)\b", re.I)


def basic_stats(texts):
    sentences = []
    words = []

    for t in texts:
        sents = sent_tokenize(str(t))
        sentences.extend(sents)
        for s in sents:
            words.extend(word_tokenize(s))

    vocab = set(words)

    sent_lengths = [len(word_tokenize(s)) for s in sentences if len(word_tokenize(s)) > 0]

    return {
        "sentence_count": len(sentences),
        "word_count": len(words),
        "vocab_size": len(vocab),
        "avg_sentence_length": sum(sent_lengths) / len(sent_lengths),
        "max_sentence_length": max(sent_lengths),
        "min_sentence_length": min(sent_lengths),
        "max_word_length": max(len(w) for w in words)
    }


def clean_text(text, counters):
    text = str(text)

    counters["emoticon_removed"] += len(EMOTICON_RE.findall(text))
    counters["phone_removed"] += len(PHONE_RE.findall(text))
    counters["account_removed"] += len(ACCOUNT_RE.findall(text))
    counters["address_removed"] += len(ADDRESS_RE.findall(text))

    text = EMOTICON_RE.sub(" ", text)
    text = PHONE_RE.sub(" ", text)
    text = ACCOUNT_RE.sub(" ", text)
    text = ADDRESS_RE.sub(" ", text)

    text = text.lower()
    counters["lowercase"] += 1

    text = SPECIAL_CHAR_RE.sub(" ", text)
    counters["special_char_removed"] += 1

    tokens = word_tokenize(text)
    cleaned_tokens = []

    for t in tokens:
        if t not in STOP_WORDS:
            cleaned_tokens.append(LEMMATIZER.lemmatize(t))
        else:
            counters["stopword_removed"] += 1

    counters["token_count"] += len(cleaned_tokens)

    return " ".join(cleaned_tokens)


def readability_per_sentence(texts):
    scores = []
    for t in texts:
        for s in sent_tokenize(str(t)):
            if len(s.split()) > 2:
                scores.append(textstat.flesch_kincaid_grade(s))
    return sum(scores) / len(scores)


def lexical_diversity(texts):
    words = []
    for t in texts:
        words.extend(word_tokenize(str(t)))
    return len(set(words)) / len(words)


start_time = time.time()

# Load dataset (fix encoding)
df = pd.read_csv(CSV_PATH, encoding="latin1")

original_texts = df[TEXT_COL].dropna().tolist()

# Stats BEFORE cleaning
before_stats = basic_stats(original_texts)
before_readability = readability_per_sentence(original_texts)
before_lexical = lexical_diversity(original_texts)

# Cleaning
counters = {
    "emoticon_removed": 0,
    "stopword_removed": 0,
    "token_count": 0,
    "lowercase": 0,
    "special_char_removed": 0,
    "phone_removed": 0,
    "account_removed": 0,
    "address_removed": 0
}

df["clean_text"] = df[TEXT_COL].apply(lambda x: clean_text(x, counters))

clean_texts = df["clean_text"].dropna().tolist()

# Stats AFTER cleaning
after_stats = basic_stats(clean_texts)
after_readability = readability_per_sentence(clean_texts)
after_lexical = lexical_diversity(clean_texts)

runtime = time.time() - start_time

# -------------------------------
# REPORT
# -------------------------------
print("\n===== BASIC STATISTICS =====")
print("Before Cleaning:", before_stats)
print("After Cleaning :", after_stats)

print("\n===== QUALITY METRICS =====")
print(f"Readability (FK Grade) Before: {before_readability:.2f}")
print(f"Readability (FK Grade) After : {after_readability:.2f}")
print(f"Lexical Diversity Before    : {before_lexical:.3f}")
print(f"Lexical Diversity After     : {after_lexical:.3f}")

print("\n===== CLEANING COUNTS =====")
for k, v in counters.items():
    print(f"{k}: {v}")

print(f"\nTotal Runtime: {runtime:.2f} seconds")
