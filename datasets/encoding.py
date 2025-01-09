from typing import List, Dict
from .tokens import PADDING_TOKEN, BEGINNING_OF_SEQUENCE_TOKEN, END_OF_SEQUENCE_TOKEN

def get_char_to_idx(chars: List[str]) -> Dict[str, int]:
  """Return character to index mapping.
  Args:
    chars (List[str]): Unique characters.

  Returns:
    Character to index mapping.
  """
  char_to_idx = {char: idx + 1 for idx, char in enumerate(chars)}
  char_to_idx[PADDING_TOKEN] = 0
  char_to_idx[BEGINNING_OF_SEQUENCE_TOKEN] = len(char_to_idx)
  char_to_idx[END_OF_SEQUENCE_TOKEN] = len(char_to_idx)
  return char_to_idx

def get_word_to_idx(words: List[str]) -> Dict[str, int]:
  """Return word to index mapping.
  Args:
    words (List[str]): Unique words.
  
  Returns:
    Word to index mapping.
  """
  word_to_idx = {word: idx + 1 for idx, word in enumerate(words)}
  word_to_idx[PADDING_TOKEN] = 0
  word_to_idx[BEGINNING_OF_SEQUENCE_TOKEN] = len(word_to_idx)
  word_to_idx[END_OF_SEQUENCE_TOKEN] = len(word_to_idx)
  return word_to_idx
