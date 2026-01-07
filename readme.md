# Programming Assignment 2 – NLP Data Preparation

## Course
Natural Language Processing (NLP) Workshop

## Assignment
Programming Assignment 2

## Student Information
- **Name:** Thanachai Naksomboon  
- **Student ID:** 662115020  

## System Specification
- **CPU:** Intel® Core™ i3-7100 CPU @ 3.90GHz  
- **RAM:** 24 GB  
- **Operating System:** Windows  
- **Python Version:** 3.x (Virtual Environment)

---

## 1. Dataset Description

This assignment uses the provided sentiment analysis dataset from the Programming 2 course (approximately **1 million text records**).  
The dataset contains the following columns:

- **ItemID** – Unique identifier  
- **Sentiment** – Sentiment label  
- **SentimentText** – Raw text content  

The dataset is suitable for large-scale Natural Language Processing (NLP) tasks such as text cleaning, tokenization, and readability analysis.

---

## 2. Objectives

The objectives of this assignment are:

1. Perform text preprocessing following the workshop steps (Step 1–4)
2. Compare **basic statistics before and after cleaning**
3. Evaluate the quality of cleaned text using **automated metrics**
4. Measure the **runtime performance** of the preprocessing pipeline

---

## 3. Data Preparation Pipeline

The preprocessing pipeline strictly follows the workshop requirements.

### Step 1: Text Cleaning
The raw text was cleaned using regular expressions and emoji handling.

Actions performed:
- Removed special characters and punctuation
- Removed numbers
- Removed extra whitespace
- Removed emoticons / emojis
- Detected and removed:
  - Phone numbers
  - Addresses
  - Account numbers

This step ensures that the text contains only meaningful alphabetic content suitable for NLP analysis.

---

### Step 2: Tokenization

Two levels of tokenization were applied:

- **Sentence tokenization:** Splitting text into individual sentences  
- **Word tokenization:** Splitting sentences into individual tokens (words)

This step enables accurate linguistic analysis and readability computation.

---

### Step 3: Lowercasing and Stopword Removal

- All tokens were converted to lowercase
- Common English stopwords (e.g., *the, is, and, of*) were removed

This reduces noise and improves the quality of statistical and lexical analysis.

---

### Step 4: Stemming and Lemmatization

- **Stemming:** Applied using Porter Stemmer to reduce words to their root form  
- **Lemmatization:** Applied using WordNet Lemmatizer to convert words into their dictionary base form  

These techniques normalize the vocabulary and reduce redundancy.

---

## 4. Statistical Comparison (Before vs After Cleaning)

The following statistics were computed **before and after cleaning**:

- Average sentence length
- Total word count
- Total sentence count
- Vocabulary size (number of unique words)
- Maximum word length
- Minimum, maximum, and average sentence length
- Number of:
  - Emojis removed
  - Stopwords removed
  - Tokens processed
  - Lowercased words
  - Special characters removed
  - Phone numbers removed
  - Addresses removed
  - Account numbers removed

These statistics demonstrate the structural changes introduced by the cleaning process.

---

## 5. Automated Quality Evaluation

### 5.1 Readability Scores (Flesch–Kincaid)

Readability was evaluated using:
- **Flesch-Kincaid Grade Level**
- **Flesch Reading Ease**

The scores were computed at the **sentence level** to avoid distortion caused by extremely long texts.

> Note: Readability formulas were originally designed for grammatically complete, punctuated text. Aggressive preprocessing may increase the calculated difficulty score, which is an expected and documented behavior.

---

### 5.2 Lexical Diversity

Lexical diversity was calculated using the formula:

# Programming Assignment 2 – NLP Data Preparation

## Course
Natural Language Processing (NLP) Workshop

## Assignment
Programming Assignment 2

## Student Information
- **Name:** Thanachai Naksomboon  
- **Student ID:** 662115020  

## System Specification
- **CPU:** Intel® Core™ i3-7100 CPU @ 3.90GHz  
- **RAM:** 24 GB  
- **Operating System:** Windows  

---

## 1. Dataset Description

This assignment uses the provided sentiment analysis dataset from the Programming 2 course (approximately **1 million text records**).  
The dataset contains the following columns:

- **ItemID** – Unique identifier  
- **Sentiment** – Sentiment label  
- **SentimentText** – Raw text content  

The dataset is suitable for large-scale Natural Language Processing (NLP) tasks such as text cleaning, tokenization, and readability analysis.

---

## 2. Objectives

The objectives of this assignment are:

1. Perform text preprocessing following the workshop steps (Step 1–4)
2. Compare **basic statistics before and after cleaning**
3. Evaluate the quality of cleaned text using **automated metrics**
4. Measure the **runtime performance** of the preprocessing pipeline

---

## 3. Data Preparation Pipeline

The preprocessing pipeline strictly follows the workshop requirements.

### Step 1: Text Cleaning
The raw text was cleaned using regular expressions and emoji handling.

Actions performed:
- Removed special characters and punctuation
- Removed numbers
- Removed extra whitespace
- Removed emoticons / emojis
- Detected and removed:
  - Phone numbers
  - Addresses
  - Account numbers

This step ensures that the text contains only meaningful alphabetic content suitable for NLP analysis.

---

### Step 2: Tokenization

Two levels of tokenization were applied:

- **Sentence tokenization:** Splitting text into individual sentences  
- **Word tokenization:** Splitting sentences into individual tokens (words)

This step enables accurate linguistic analysis and readability computation.

---

### Step 3: Lowercasing and Stopword Removal

- All tokens were converted to lowercase
- Common English stopwords (e.g., *the, is, and, of*) were removed

This reduces noise and improves the quality of statistical and lexical analysis.

---

### Step 4: Stemming and Lemmatization

- **Stemming:** Applied using Porter Stemmer to reduce words to their root form  
- **Lemmatization:** Applied using WordNet Lemmatizer to convert words into their dictionary base form  

These techniques normalize the vocabulary and reduce redundancy.

---

## 4. Statistical Comparison (Before vs After Cleaning)

The following statistics were computed **before and after cleaning**:

- Average sentence length
- Total word count
- Total sentence count
- Vocabulary size (number of unique words)
- Maximum word length
- Minimum, maximum, and average sentence length
- Number of:
  - Emojis removed
  - Stopwords removed
  - Tokens processed
  - Lowercased words
  - Special characters removed
  - Phone numbers removed
  - Addresses removed
  - Account numbers removed

These statistics demonstrate the structural changes introduced by the cleaning process.

---

## 5. Automated Quality Evaluation

### 5.1 Readability Scores (Flesch–Kincaid)

Readability was evaluated using:
- **Flesch-Kincaid Grade Level**
- **Flesch Reading Ease**

The scores were computed at the **sentence level** to avoid distortion caused by extremely long texts.

> Note: Readability formulas were originally designed for grammatically complete, punctuated text. Aggressive preprocessing may increase the calculated difficulty score, which is an expected and documented behavior.

---

### 5.2 Lexical Diversity

Lexical diversity was calculated using the formula:

