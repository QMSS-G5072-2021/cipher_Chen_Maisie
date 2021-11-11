from cipher_mc4938 import cipher_mc4938
import pandas as pd

def test_cipher_symbol(example):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in example[0]:
        index = alphabet.find(c)
        if index == -1:
            expected = cipher(example[0],example[1])
            assert expected == example[2], 'Result does not match the expected value'
    
test_cipher_symbol(test_word)
