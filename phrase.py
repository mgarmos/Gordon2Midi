import word
from enum import Enum



class Meter(Enum):
    DUPLE = 2
    TRIPLE = 3    
        

class Phrase:

    meter = Meter.DUPLE
    phrase = [] # A phrase is a list of words. A word is a list of four syllables
    length = 0
    print("1")
    
    def __init__(self, length, meter=Meter.DUPLE):
        self.meter = meter
        self.length = length
        self.getPhrase()
        
    def __str__(self):
        result = ''
        for myWord in self.phrase:
            for syllable in myWord:
                result += str(syllable) + ', '
            result += '\n'
        return result
        
    
    def getPhrase(self):        
        for i in range(self.length):
            wordRequested = word.getDupleWord() if self.meter == Meter.DUPLE else word.getTripleWord()
            self.phrase.append(wordRequested)
            
    
    def printPhrase(self):
        print('printPhrase')
        for myWord in self.phrase:
            for syllable in myWord:
                print(syllable,end=', ')
            print('')
            
    def main():
        myPhrase = Phrase(3, Meter.TRIPLE)
        print(myPhrase)
      
if __name__== "__main__":
    Phrase.main()            
            

       

