from collections import Counter
import re
import unicodedata
from typing import List

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_data(text: str) -> str:
  """
  Args:
    text (list): Sentence.
  
  Returns:
    Post-processed text.
  """
  text = unicodedata.normalize("NFD", text.lower().strip())
  text = re.sub(r"([.!?])", r" \1", text)
  text = re.sub(r"[^a-zA-Z.!?]+", r" ", text)
  text = text.strip()
  return text

def tokenize_data(data: List[str], top_k: int) -> List[str]:
  """
  Args:
    data (list): List of sentences. 
    top_k (int): Number of tokens.

  Returns:
    Top k number of tokens.
  """
  lemmatizer = WordNetLemmatizer()
  tokens = Counter()
  for text in data:
    tokens.update([lemmatizer.lemmatize(token) for token in word_tokenize(text)])
  top_k_tokens = [token for token, _ in tokens.most_common(top_k)]
  return top_k_tokens
