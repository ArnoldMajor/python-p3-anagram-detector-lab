# your code goes here!
class Anagram:
    def __init__(self, keyword):
        self.keyword = keyword.lower()

    def match(self, wordlist):
            matchlist = []
            for word in wordlist: 
                if sorted(word.lower()) == sorted(self.keyword):
                    matchlist.append(word)
            return matchlist

        

Anagram("ByeGood").match(["Hello", "Goodbye", "Afternoon"])