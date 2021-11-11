def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

### describe the function: The function is to encrypt text by a set-up number of alphabetical changes
### explain its inputs and its output: input is a string of text, output is a new string of ciphered text
### Provide a short use case example of encrypting and decrypting:
### cipher("test", 1) should give result "uftu"
