import time
import json
epoch_time = int(time.time())

from os.path import dirname, join, realpath

def main():
  ROOT_FOLDER = dirname(realpath(__file__))
  with open(join(ROOT_FOLDER, 'data', 'word_trie.json')) as f:
    word_index = json.loads(f.read())
    working_index = word_index
    working_letter = 'start'
    while working_letter != '':
      print(working_index.keys())
      working_letter = input('Enter letter: ')
      if working_letter == '':
        print('Bye!')
        break
      elif len(working_letter) > 1:
        print('Must be a single letter!')
        continue
      working_letter = working_letter.lower()
      if working_letter in working_index:
        working_index = working_index[working_letter]
        if 'word' in working_index:
          print('Word found:', working_index['word'])
          if(len(working_index.keys()) == 1):
            print('That\'s all!')
            break
      else:
        print('Not a valid word!')
        break

if __name__ == '__main__':
  main()