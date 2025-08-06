import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]

def gen_password(nbre_lettres,nbre_symboles,nbre_nombres):
    mot_passe_liste = (
        random.choices(letters, k=nbre_lettres) +
        random.choices(symbols, k=nbre_symboles) +
        random.choices(numbers, k=nbre_nombres)
    )
    random.shuffle(mot_passe_liste)
    mot_passe = ''.join(mot_passe_liste)
    return mot_passe
   