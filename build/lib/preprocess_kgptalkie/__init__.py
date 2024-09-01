# entry level code and import text preprocess

from .text_preprocess import *


# General Feature Extraction
def extract_features(x):
    return {
        'word_count': word_count(x),
        'char_count': char_count(x),
        'avg_word_len': avg_word_len(x),
        'stop_words_count': stop_words_count(x),
        'hashtags_count': hashtags_count(x),
        'mentions_count': mentions_count(x),
        'numerics_count': numerics_count(x),
        'upper_case_count': upper_case_count(x),
    }

# Cleaning Text
def clean_text(text):
    text = to_lower_case(text)
    text = contraction_to_expansion(text)
    text = remove_emails(text)
    text = remove_urls(text)
    text = remove_html_tags(text)
    text = remove_special_chars(text)
    text = lemmatize(text)
    return text