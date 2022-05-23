
from os.path import dirname, join, realpath
import json

class WordIndexer:
  def __init__(self):
    word_index = dict()
    pass

  def _indexTool(self, working_dict: dict, word: str, on_char: int):
    if on_char < len(word):
      # print(word, on_char)
      # print(working_dict)
      working_char = word[on_char]
      if working_char not in working_dict.keys():
        working_dict[working_char] = dict()
      working_dict[working_char] = self._indexTool(working_dict[working_char], word, on_char + 1)
    else:
      working_dict['word'] = word
    return working_dict

  def indexer(self, word_list: list[str]):
    working_dict = dict()
    for word in word_list:
      working_dict = self._indexTool(working_dict, word, 0)
    return working_dict

def main():
  with open(join(dirname(realpath(__file__)), 'data', 'word_list.txt')) as f:
    word_data = f.read()
  words = word_data.split(',')
  word_indexer = WordIndexer()
  indexed_words = word_indexer.indexer(words)
  with open(join(dirname(realpath(__file__)), 'data', 'word_index.json'), 'w+') as f:
    json.dump(indexed_words, f)


if __name__ == '__main__':
  main()