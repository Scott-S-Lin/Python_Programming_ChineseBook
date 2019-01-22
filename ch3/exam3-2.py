#filename:Animalstore.py
#function: Class has Name and list

class Animal_Store:

#class has Name and list attribute
    def __init__(self, name):
        self.name = name
        self.list = []    

    def add_description(self, nick):
        self.list.append(nick)

Wu = Animal_Store('Amira')
Tsai = Animal_Store('Panda')

Wu.add_description('He can play ball')
Wu.add_description('and can smile to child')
Tsai.add_description('He can dance')

print(Wu.list)
print(Tsai.list)

