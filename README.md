# Word indexer

This tool indexes words into a trie data structure. It is used for the [Boggle server](https://github.com/TheOmnimax/boggle-server).

# Running

To run it, go to `/source/main.py`, and run that Python script.

# Word list

A word list is provided for you (I'm sorry, I can't remember where I found it), but you can also provide your own. Just make sure:

 * The file is called `word_list.txt`,
 * The file is in the folder `/source/data/`, and
 * Words are comma-separated.

# Data structure

The word trie will be created at `/source/data/word_trie.json`. As the name implies, it is a JSON file.

Each key is a single letter. The value of each key is a dictionary of every letter of every possible word that is possible with that sequence of letters. When there is a complete word, then the dictionary will contain the key "word" instead of a letter, with the value being the created word instead of another dictionary.

For example, let's traverse the word "hello". We would find the key "h", and that value is another dictionary. In that new dictionary, we find the key "e", which has a value with a new dictionary. We keep going until the key "o"; again, that value is a dictionary, and that dictionary contains the key "word", meaning "hello" is a word.

# Testing

The file "test.py" can be used to do spot-checks to find words. When prompted, enter a letter, then press "Enter" on your keyboard. Keep going like this. It will let you know when it finds a word. Leave the entry blank then press "Enter" to exit.