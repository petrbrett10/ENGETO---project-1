# hlavička

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Brettschneider
email: petrbrettschneider@gmail.com
"""
# user database
databaze_uzivatelu = {
    "bob":"123" , 
    "ann":"pass123" , 
    "mike":"password123" , 
    "liz":"pass123"
    }

# graphic separator
separator = "-" * 34

# username and password input
username_in = input("username: ")
password_in = input("password: ")
print (separator)

# user and password control
if username_in in databaze_uzivatelu:
    if password_in == (databaze_uzivatelu.get (username_in)):
        print("Welcome to the app,", username_in, ".")
    else: 
        print("Wrong password. Terminating the program.")
        exit()
else:
    print("Unregistred user. Terminating the program.")
    exit()

# input texts for analysis
texts = [
    '''Situated about 10 miles west of Kemmerer,     
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# determining the number of texts to analyze
print(f"We have {len(texts)} texts to be analyzed.\n{separator}")

# selection of text for analysis
text_choice = input(f"Enter a number btw. 1 and {len(texts)} to select: ")
print(separator)

# ValueError check
try:
    int(text_choice)
except ValueError:
    print("Wrong choice. Program terminated.")
    exit()
text_choice = int(text_choice)

# correctness check selection of text for analysis (selection within a range)'
if not text_choice in range(1,len(texts)):
    print("Wrong choice. Program terminated.")
    exit()

# selected text
text_choice -= 1
choosen_text = texts[text_choice]

# deleting unwanted characters from text (prepared for next texts, 
# the list of unwanted characters should be continuously expanded 
# according to the input texts)
unwanted_char = [".",",",":","?","(",")","!","%","+","/"]
for char in unwanted_char:
    choosen_text = choosen_text.replace(char,"")

# dividing selected text into words
text_to_analyze = choosen_text.split()

# dividing words by type into separate lists
titlecase_words = [word for word in text_to_analyze if word.istitle()]
numeric_strings = [word for word in text_to_analyze if word.isdigit()]
lowercase_words = [word for word in text_to_analyze if word.islower()]
uppercase_words = [word for word in text_to_analyze if word.isupper()]

# the sum of words that are numeric
numb_sum = 0
for num in numeric_strings:
    num_int = int(num)
    numb_sum += num_int

# finding the longest word (for later statistical graphic output)
max_word_length=0
for word in text_to_analyze:
    word_length = len(word)
    if word_length > max_word_length:
        max_word_length = word_length # nr of characters in longest word

# number of occurrences according to the length of individual words
occu  = {}
for i in range (1,max_word_length+1):
    length_rate = 0
    for word in text_to_analyze:
        word_length = len(word)
        if word_length == i:
           length_rate += 1
    occu[i] = length_rate

# statistical graphic output 
print(f"There are {len(text_to_analyze)} words in the selected text.")
print(f"There are {len(titlecase_words)} titlecase words.")
print(f"There are {len(uppercase_words)} uppercase words.")
print(f"There are {len(lowercase_words)} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all numbers is: {numb_sum}\n{separator}")
print(f"LEN | {"OCCURENCES":<22} | NR.\n{separator}")
# Items (word lengths) with zero occurrences are intentionally listed
# in the graphic output so that the user can see that this was also taken
# into account during the analysis. If we wanted to shorten the notation, 
# we would add a condition to the loop to print the occurrence if it
# is greater than 0.("if int(occu.get (i)) > 0")
for i in range (1, max_word_length+1):
    print(f"{i:>3} | {"*" * int(occu.get (i)):<22} | {int(occu.get (i)):<3}")
