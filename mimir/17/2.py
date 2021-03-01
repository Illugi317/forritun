'''
2. Sentence
5 points possible

Implement a class called Sentence that has a constructor that takes a string, representing the sentence, as input.  The class should have the following methods:

    get_first_word(): returns the first word as a string
    get_all_words(): returns all words in a list.
    replace(index, new_word): Changes a word at a particular index to new_word.  For example, if the sentence is "I'm going back", then replace(2, "home") results in "I'm going home".  If the index is not valid, the method does not do anything.

Example use of class:

sent = Sentence('This is a test')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())

Output:

This
['This', 'is', 'a', 'test']
['This', 'is', 'a', 'must']
'''


class Sentence:
    def __init__(self,words)-> None:
        self.words = words.split()

    def get_first_word(self):
        return str(self.words[0])
        
    def get_all_words(self):
        return self.words
    
    def replace(self,index,word_to_replace_with):
        try:
            self.words[index] = word_to_replace_with
        except IndexError:
            pass

    def __str__(self) -> str:
        return str(self.my_value)


if __name__ == '__main__':
    sent = Sentence('This is a test')
    print(sent.get_first_word())
    print(sent.get_all_words())
    sent.replace(3, "must")
    #print(sent.get_all_words())