class flashcard:
        def __init__(self, word, meaning):
            self.word = word
            self.meaning = meaning
        def str_(self):
            return self.word+' '+self.meaning+' )'
flash = []

print("welcome to flashcard application")
while(True):
        word = input("enter the name you want to add to flashcard : ") 
        meaning = input("enter the meaning of the word : ")
        flash.append(flashcard (word, meaning))
        option = int(input("enter, if you want to add another flashcard enter 0, otherwise enter 1: "))
        if (option):
            break

print("\nYour flashcards")
for i in flash:
      print(">",i)