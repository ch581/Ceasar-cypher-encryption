# Ceasar cypher encryption
#import string
#plain_text = input("Passcode :")
#shift = int(input("Enter encyrption shift by :"))
#alphabet = string.ascii_lowercase
#shifted = alphabet[shift:]+alphabet[:shift]
#table = str.maketrans(alphabet, shifted)
#encrypted = plain_text.translate(table)
#print(encrypted)

import string

def caesar(text, shift, alphabets):
   def shift_alphabet(alphabet):
       return alphabet[shift:] + alphabet[:shift]
   shifted_alphabets = tuple(map(shift_alphabet, alphabets))
   results_output = "".join(alphabets)
   encrypted_output = "".join(shifted_alphabets) 
   table = str.maketrans(results_output, encrypted_output)
   return text.translate(table)

plain_text = input("Enter message :")
print(caesar(plain_text, 7, [string.ascii_lowercase, string.ascii_letters, string.ascii_uppercase,string.punctuation]))
