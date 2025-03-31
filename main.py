

# hlavička

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Brettschneider
email: petrbrettschneiderr@gmail.com
"""
# databáze uživatelů

databaze_uzivatelu ={
    "bob":"123" , 
    "ann":"pass123" , 
    "mike":"password123" , 
    "liz":"pass123"
    }

# object - počítání velkých
# object - počítání malých
# object - počítání čísel (int)
# zadání jména
jmeno_vstup = input ("username:")

# zadání hesla
heslo_vstup = input ("password:")
print ("-----------------------------")
# ověření uživatele a hesla
if jmeno_vstup in databaze_uzivatelu:
    if heslo_vstup == (databaze_uzivatelu.get (jmeno_vstup)):
        print ("Welcome to the app,", jmeno_vstup)
    else: 
        print ("Wrong password. Program terminated.")
        exit()
else:
    print ("Unregistred user. Terminating the program")
    exit()

#print ("pokračuji")
     

# vstupní texty

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
pocet_textu = int(len(texts))

print ("We have ", pocet_textu , " texts to be analyzed.")
print ("-----------------------------")
# výběr textu
volba_textu = int(input("Enter a number btw. 1 and 3 to select:"))
print ("-----------------------------")

# vyhodnocení vložení výběru textu
if volba_textu<1 or volba_textu>pocet_textu:
    print ("Špatná volba. Ukončuji program.")
    exit()

volba_textu = volba_textu - 1
vybrany_text = texts[volba_textu]
#print (vybrany_text)
#print (type (vybrany_text))

# definice setu - jednotlivá slova z řetězce
text_k_analyze = list()
# procházení textu - projde text písmeno po písmenu a najde konce slov - když narazí na mezeru, čárku nebo tečku, uloží slovo do listu "text_k_analyze"
slovo=""
for pismeno in vybrany_text:
    if pismeno == " ":
        #print ("mezera")
        text_k_analyze.append (slovo)
        slovo=""
    elif pismeno == ".":
        #print ("tečka")
        text_k_analyze.append (slovo)
        slovo=""
    elif pismeno == ",":
        #print ("čárka")
        text_k_analyze.append (slovo)
        slovo=""
    elif pismeno == '\n':
        #print ("Enter")
        text_k_analyze.append (slovo)
        slovo=""
    else:
        slovo=slovo+pismeno
        #print (slovo)
if len(slovo)>0:
    text_k_analyze.append(slovo)    
#print (type(text_k_analyze))
#print (text_k_analyze)
#print (len(text_k_analyze[9]))
# odmazání prázdných řetězců z listu
# posouzení slov v textu - pozice s prázdným textem
pocet_slov_v_textu = 0
prazdne_pozice = []
for i in text_k_analyze:
    if len(i)>0:
        pocet_slov_v_textu = pocet_slov_v_textu + 1
pozice_slova=1
for word in text_k_analyze:
    if len(word)<1:
        #print ("nalezeno", pozice_slova)
        prazdne_pozice.append (pozice_slova)
        pozice_slova +=1
    else:  
        #print (word, len(word), pozice_slova)
        pozice_slova +=1
#for word in text_k_analyze:
    #print (word,len(word))
# vymazání prázdných pozic
#print (prazdne_pozice)
prazdne_pozice.sort (reverse=True)
#print (prazdne_pozice)
#print (text_k_analyze)
for pozice in prazdne_pozice:
    del text_k_analyze[pozice-1]
    
# kontrola listu bez "prázdných" slov    
#print (text_k_analyze)

print ("There are ",pocet_slov_v_textu, "words in the selected text.")

# počet slov začínajích velkým, malým písmenem a číslem
zac_velkym = []
zac_malym = []
zac_cislem = []
cele_velke =[]
cele_male = []
cele_cislo = []
for word in text_k_analyze:
    prvni_pismeno=str(word[0])
    #print (word,prvni_pismeno)
    if ord(prvni_pismeno) in range (65,90):
        zac_velkym.append (word)
    elif ord(prvni_pismeno) in range (97,122):
        zac_malym.append (word)
    elif ord(prvni_pismeno) in range (48,57):
        zac_cislem.append (word)

#print (zac_velkym)
#print ("Slov začínajích velkým písmenem je:", len (zac_velkym))

#print (zac_malym)
#print ("Slov začínajích malým písmenem je:", len (zac_malym))

#print (zac_cislem)        
#print ("Čísel je:", len (zac_cislem))

# kontrola slov psaných jen velkými písmeny
for word in text_k_analyze:
    cele_velke_status = 0
    cislo_status = 0
    cele_male_status = 0
    for letter in word:
        #print (word, letter, ord(letter))
        if ord(letter) in range (65,90):
            cele_velke_status = 1
        if ord(letter) in range (97,122):
            cele_male_status = 1
        if ord(letter) in range (48,57):
            cislo_status = 1      
        
    if cele_velke_status == 1 and cele_male_status == 0 and cislo_status ==0:
        #print (cele_velke_status, word)
        cele_velke.append(word)
        #print (cele_velke_status)
    if cele_velke_status == 0 and cele_male_status == 1 and cislo_status ==0:
        #print (cele_male_status, word)
        cele_male.append(word)
        #print (cele_male_status)
    if cele_velke_status == 0 and cele_male_status == 0 and cislo_status ==1:
        #print (cislo_status, word)
        cele_cislo.append(word)
        #print (cislo_status)
set_PV = set(zac_velkym)
#print ("PV:",set_PV)
set_CV = set(cele_velke)
print (set_CV)

#rozdil_PV_CV = set_PV - set_CV
#print ("Rozdil: ",rozdil_PV_CV)
zac_velkym_rozdil = len(zac_velkym) - len(cele_velke)     
print ("There are ",zac_velkym_rozdil, "titlecase words.")
#print (zac_velkym)
print ("There are ",len(cele_velke), "uppercase words.")
#print (cele_velke)
print ("There are ",len(cele_male), "lowercase words.")
#print (cele_male)
print ("There are ",len(cele_cislo), "numeric strings.")
#print (cele_cislo)
# součet čísel
soucet_cisel = 0
for cislo in cele_cislo:
    cislo_int = int(cislo)
    soucet_cisel+=cislo_int
print ("The sum of all numbers is: ",soucet_cisel)
#pocet_vyskytu_delek_slov
max_delka=0
for polozka in text_k_analyze:
    delka_slova=len(polozka)
    if delka_slova>max_delka:
        max_delka = delka_slova #pocet znaku nejdelsiho slova
    #print (delka_slova, max_delka)
pocet_vyskytu_dle_delky = {}
for i in range (0,max_delka+1):
    pocet_vyskytu=0
    for polozka in text_k_analyze:
        delka_slova=len(polozka)
        if delka_slova==i:
           pocet_vyskytu=pocet_vyskytu+1
    pocet_vyskytu_dle_delky[i]=pocet_vyskytu

#print (type(pocet_vyskytu_dle_delky))
#print (pocet_vyskytu_dle_delky)
pocet_hvezdicek=0
print ("-----------------------------")
print ("LEN ","|", "OCCURENCES", "|", "NR.", "\n")
print ("-----------------------------")
for i in range (1, max_delka+1):
    pocet_hvezdicek = int(pocet_vyskytu_dle_delky.get (i))
    print (i,"|", "*" * int(pocet_hvezdicek), "|", pocet_hvezdicek)
           
#velka_pismena = 
#mala_pismena = 
#cisla_v_textu = 