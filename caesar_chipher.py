class Cipher:
    alphabet= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_alphabet = ''
    crypto_encode = {}
    crypto_decode = {}

    def __init__(self, keyword) -> None:
        self.keyword = keyword.upper()
        Cipher.shift_alphabet(self.keyword,self.alphabet)

    @classmethod
    def shift_alphabet(cls, keyword, alphabet):
        key_list, value_list, new_str, new_alphabet = [], [], '', keyword+alphabet
        
        for char in new_alphabet:
            if new_str.find(char) == -1:
                new_str += char
        cls.new_alphabet = new_str
        
        key_list.extend(cls.new_alphabet)
        value_list.extend(alphabet)

        cls.crypto_encode = {value: key for value, key in zip(value_list, key_list)}
        cls.crypto_decode = {key: value for key, value in zip(key_list, value_list)}


    def encode(self, data):
        new_string = ""
        
        for char in data:
            if char in self.crypto_encode.keys():
                new_string += self.crypto_encode[char]
            elif char.upper() in self.crypto_encode.keys():
                value = self.crypto_encode[char.upper()]
                new_string += value.lower()
            if char.find(' ') != -1:
                new_string += ' '
        
        return new_string
    
    def decode(self, data):
        new_string = ""
        
        for char in data:
            if char in self.crypto_decode.keys():
                new_string += self.crypto_decode[char]
            elif char.upper() in self.crypto_decode.keys():
                value = self.crypto_decode[char.upper()]
                new_string += value.lower()
            if char.find(' ') != -1:
                new_string += ' '

        return new_string

cipher = Cipher("crypto")
cipher.encode('Hello World')

cipher.decode("Fjedhc dn atidsn")
