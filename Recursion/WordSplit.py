# Create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

def word_split(phrase, words, res = None):
    if res is None:
        res = []

    for word in words:
        if phrase.startswith(word):
            res.append(word)
            return word_split(phrase[len(word):], words, res)
    return res

def word_split(phrase, words, res = None):
    if res is None:
        res = []

    for word in words:
        val = phrase[0: len(word)]        
        if val == word:
            res.append(word)
            return word_split(phrase[len(word):], words, res)
    return res

word_split('themanran',['the','ran','man'])
word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
word_split('themanran',['clown','ran','man'])
