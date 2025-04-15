# hlavička

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Brettschneider
email: petrbrettschneider@gmail.com
"""
# users database
databaze_uzivatelu ={
    "bob":"123" , 
    "ann":"pass123" , 
    "mike":"password123" , 
    "liz":"pass123"
    }

# username and password input
username_in = input ("username: ")
password_in = input ("password: ")
print ("-" * 34)

# users nad passwords control
if username_in in databaze_uzivatelu:
    if password_in == (databaze_uzivatelu.get (username_in)):
        print ("Welcome to the app,", username_in, ".")
    else: 
        print ("Wrong password. Terminating the program.")
        exit()
else:
    print ("Unregistred user. Terminating the program.")
    exit()

# texts for analyze
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

# checking amount of texts
print (f"We have  {len(texts)}  texts to be analyzed.")
print ("-" * 34)

# text choice
text_choice = input(f"Enter a number btw. 1 and {len(texts)} to select: ")
print ("-" * 34)

# ValueError check
try:
    int (text_choice)
except ValueError:
    print ("Wrong choice. Program terminated.")
    exit()
text_choice = int(text_choice)

# text select check
if text_choice < 1 or text_choice > len(texts):
    print ("Wrong choice. Program terminated.")
    exit()

# selected text
text_choice -= 1
choosen_text = texts[text_choice]

# ".", "," deleting from selected text
choosen_text = choosen_text.replace(".","")
choosen_text = choosen_text.replace(",","")

# selected text split
text_to_analyze = choosen_text.split()

# words counting
titlecase_words = [word for word in text_to_analyze if word.istitle()]
numeric_strings = [word for word in text_to_analyze if word.isdigit()]
lowercase_words = [word for word in text_to_analyze if word.islower()]
uppercase_words = [word for word in text_to_analyze if word.isupper()]

# Titlecase words counting
only_title = len(titlecase_words)

# sum of numeric strings
numb_sum = 0
for num in numeric_strings:
    num_int = int(num)
    numb_sum += num_int

# longest word search
max_word_length=0
for word in text_to_analyze:
    word_length = len(word)
    if word_length > max_word_length:
        max_word_length = word_length # nr of letters in longest word

# sum of rate by word length
rate_by_length  = {}
for i in range (0,max_word_length+1):
    length_rate = 0
    for word in text_to_analyze:
        word_length = len(word)
        if word_length == i:
           length_rate += 1
    rate_by_length[i]=length_rate

# statistic output by type of word
print (f"There are {len(text_to_analyze)} words in the selected text.")
print (f"There are {len(titlecase_words)} titlecase words.")
print (f"There are {len(uppercase_words)} uppercase words.")
print (f"There are {len(lowercase_words)} lowercase words.")
print (f"There are {len(numeric_strings)} numeric strings.")
print (f"The sum of all numbers is: {numb_sum}")

# graphic output
print ("-" * 34)
print ("LEN ","|", "OCCURENCES", " " * 10, "|", "NR.")
print ("-" * 34)
for i in range (1, max_word_length+1):
    star_amount = int(rate_by_length.get (i))
    stars = "*" * int(star_amount)
    print (f"{i:>3}  | {stars:<22}| {star_amount:<3}")  
