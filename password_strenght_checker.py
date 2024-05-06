import random

class Start:
    def __init__(self):
        self.WhattoChoose = '' 
        self.initProgamCreate= Create()
        self.initProgamChecker= checker()

    def checkWhatTochoose(self):
        self.WhattoChoose = input(''' 

           welcome my friend this a program to check if your password has the correct strenght and also it's to create 
                                      
            to create your password put the letter "cr"
                                      
            and if you want to check your password that you created or your personl password put 'ch'
                                      
            =>
''').lower()
        while True:
            if self.WhattoChoose == "cr":
                self.initProgamCreate.main()
                break
            elif self.WhattoChoose == "ch":
                self.initProgamChecker.main()
                break
            else:
                break
       
            

class Create:
    def __init__(self):
        self.password_User = ''
        self.password_list_user = []
        self.nr_letters = ''
        self.nr_symbols = ''
        self.nr_numbers = ''
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',"@"]
        self.password_list = []
        self.password = ""

    def createPassword(self):
        print("Welcome to the PyPassword Generator!")
        self.nr_letters = int(input("How many lowercases would you like in your password?\n")) 
        self.nr_letterUpper = int(input("How many uppercases would you like in your password"))
        self.nr_symbols = int(input(f"How many symbols would you like?\n"))
        self.nr_numbers = int(input(f"How many numbers would you like?\n"))

        for _ in range(1,self.nr_letters + 1):
            self.password_list.append(random.choice(self.letters))
        
        for _ in range(1,self.nr_letterUpper + 1):
            self.password_list += random.choice(self.letters_Uppercase)
            

        for _ in range(1, self.nr_symbols + 1):
            self.password_list += random.choice(self.symbols)

        for _ in range(1, self.nr_numbers + 1):
            self.password_list += random.choice(self.numbers)

        random.shuffle(self.password_list)
        self.password = ""
        for char in self.password_list:
            self.password += char

        print(f"your password {self.password}" )


    def get_password(self):
        self.password_User = (input("right here your password => "))
        self.password_list_user = self.password_User.replace("",", ").split(", ")

    def main(self):
        self.createPassword()

class checker(Create):
    def __init__(self):
        super().__init__()
        self.has_uppercase = False
        self.has_lowercase = False
        self.has_number = False
        self.has_symbol = False
        self.isGoodps = False

    def checkTheuppercase(self):
        for item in self.password_list_user:
            for char in item:
                if char.isupper():
                    self.has_uppercase = True        
                    break
        if self.has_uppercase:
            print(f"your password '{self.password_User}' has an uppercase")        
        else:
            print(f"your password '{self.password_User}' doesn't have an uppercase")

    def checkThelowecase(self):
        for item in self.password_list_user:
            for char in item:
                if char.islower():
                    self.has_lowercase = True
                    break
        if self.has_lowercase:
            return (f"your password '{self.password_User}' has a lowercase")
        else:
            print(f"your password '{self.password_User}' doesn't have a lowercase")

    def checkTheNumber(self):
        for item in self.password_list_user:
            for char in item:
                if char.isnumeric():
                    self.has_number = True
                    break
        if self.has_number:
            print(f"your password '{self.password_User}' has a number")
        else:
            print(f"your password '{self.password_User}' doesn't have a number")

    def checkThesymbol(self):
        for item in self.password_list_user:
            for char in item:
                if char in self.symbols:
                    self.has_symbol = True
                    break
        if self.has_symbol:
            print(f"your password '{self.password_User}' has a symbol")
        else:
            print(f"your password '{self.password_User}' doesn´t have a symbol")
                
    def checktheStrenght(self):
        if len(self.password_User) >=  12:
            print(f"the lenght of your password is ok")
        else:
            print("the lenght of your password isn´t ok must be with 12 caracters")

    def main(self):
            while True:
                self.get_password()
                self.checkTheuppercase()
                self.checkThelowecase()
                self.checkTheNumber()
                self.checkThesymbol()
                self.checktheStrenght()
            
        
        

if __name__ == "__main__":
       program = Start()
       program.checkWhatTochoose()