import json

from os.path import dirname, join, realpath

def main():
  data_folder = join(dirname(realpath(__file__)), 'data')
  with open(join(data_folder, 'word_trie.json')) as f:
    original_data = json.loads(f.read())
  for letter in original_data:
    with open(join(data_folder, 'word_trie_' + letter + '.json'), 'w+') as f:
      json.dump(original_data[letter], f)

if __name__ == '__main__':
  main()