import string

print(
"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"\"\"\"\"\"\" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)
# def encrypt(plain_text, shift):
#     plain_text_lst = list(plain_text)
#     cipher_text = ''

#     global alphabet_list

#     for idx in range(len(plain_text_lst)):
#         if plain_text_lst[idx] in alphabet_list:
#             cipher_text += alphabet_list[alphabet_list.index(plain_text_lst[idx]) + shift]
#         else:
#             print("Your input cannot be recognised. It may contain a non-letter symbol.")
#             return
#     print("The encoded text is {}".format(cipher_text))
#     return cipher_text

# def decrypt(plain_text, shift):
#     global alphabet_list
    
#     plain_text_lst = list(plain_text)
#     decipher_text = ''
#     for idx in range(len(plain_text_lst)):
#         if plain_text_lst[idx] in alphabet_list:
#             decipher_text += alphabet_list[alphabet_list.index(plain_text_lst[idx]) - shift]
#         else:
#             print("Your input cannot be recognised. It may contain a non-letter symbol.")
#             return
#     print("The decoded text is {}".format(decipher_text))
#     return decipher_text

def caesar(start_text, cipher_direction, shift_amount):
    global alphabet_list
    text_lst = list(start_text)
    end_text = ''

    for idx in range(len(text_lst)):
        if text_lst[idx] in alphabet_list:
            if cipher_direction == "encode":
                end_text += alphabet_list[alphabet_list.index(text_lst[idx], 0, len(alphabet_list) - shift_amount) + shift_amount] 
            elif cipher_direction == "decode":
                end_text += alphabet_list[alphabet_list.index(text_lst[idx], shift_amount) - shift_amount]
        else:
            end_text += text_lst[idx]
    print("The {}d text is {}".format(cipher_direction, end_text))

while True:

    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type in your message:\n").lower()
    shift = int(input("Type in your shift number:\n"))
    shift = shift % 26

    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    [alphabet_list.append(x) for x in alphabet_list[:shift]]
    [alphabet_list.insert(i, value) for i, value in enumerate(alphabet_list[len(alphabet_list) - 2*shift:len(alphabet_list) - shift])]

    caesar(text, command, shift)

    if input("Do u want to restart the cipher program?\n") == 'no':
        print("Goodbye.")
        break



