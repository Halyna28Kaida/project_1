"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Halyna Kaida

email: lina.g@ukr.net
"""

TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
"jdfhsdfg kjgfdahgj jhdgfda kdj kj"
]

USERS = {"bob": "123", 
         "ann": "pass123", "mike": 
         "password123", "liz": "pass123"}
SEPARATOR = "-" * 40

user = input("Please, enter your username: ")
password = input("Please, enter your password: ")


if USERS.get(user) == password:
    print(
        f"\nusername: {user}\n" + \
        f"password: {password}\n" + \
        f"\n{SEPARATOR}\n" + \
        f"\nWelcome to the app, {user.title()}.\n" + \
        f"We have 3 texts to be analyzed.\n" + \
        f"\n{SEPARATOR}\n"
    )
    

    numbers = list(range(1, len(TEXTS) + 1))
    choice_numbers = [str(num) for num in numbers]
    print(choice_numbers)

    choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: " )
    if (choice in choice_numbers) and (choice.isnumeric):
        words_list = TEXTS[int(choice)-1].split()
        word_is_title = 0
        word_is_uppercase = 0
        word_is_lowercase = 0
        word_is_num = 0
        summ = 0

        # creating a set with unique word lengths
        length_set = set()

        for word in words_list:
            word = word.strip(".,/\"!_=*+/")
            # adding word length from selected text to length set 
            length_set.add(len(word)) 
            if word.istitle(): 
                word_is_title += 1
            if word.isupper() and word[0].isalpha():
                word_is_uppercase += 1
            if word.islower() and word[0].isalpha(): 
                word_is_lowercase += 1
            if word.isnumeric():          
                word_is_num += 1
                summ += int(word)

        # creating dictionary from length set with value 0
        length = dict.fromkeys(length_set, 0)

        # increasing the number of word lengths in the dictionary values 
        for word in words_list:
            length_key = len(word.strip(".,"))
            length[length_key] += 1

        print(
            f"\n{SEPARATOR}\n" + \
            f"\nThere are {len(words_list)} words in the selected text.\n" + \
            f"There are {word_is_title} titlecase words.\n" + \
            f"There are {word_is_uppercase} uppercase words.\n" + \
            f"There are {word_is_lowercase} lowercase words.\n" + \
            f"There are {word_is_num} numeric strings.\n" + \
            f"The sum of all the numbers {summ}\n" 
        ) 
        
        # printing the table of word lengths 
        if max(length.values()) < 11:
            table_sep = "*" * 24
        else:
            table_sep = "-" * (max(length.values()) * 2)
        print(table_sep)
        print("LEN".center(5), " OCCURANCES ".center(max(length.values()) + 2), "NR", sep= "|")
        print(table_sep)

        for key, value in length.items():
            if max(length.values()) < 11:
                occurances_val = ("*" * value).ljust(12)
            else:
                occurances_val = ("*" * value).ljust(max(length.values()) + 2)
            print(str(key).rjust(5), occurances_val, value, sep= "|")
        print()
    else:
        print("\nIncorrect number.\n")
else:
    print(
        f"\nusername: {user}\n" + \
        f"password: {password}\n" + \
        "\nUnregistered user, terminating the program..\n"
    )
