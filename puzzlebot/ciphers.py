import random 
import string 

class Ciphers:

    @staticmethod
    def __all__():
        return [i for i in dir(Ciphers) if not i.startswith('_') ]

    class Substitution:
        """
        A substitution cipher.

        """

        def __init__(self):
            self.name = 'Substitution'
            self.key = [*string.ascii_lowercase]
            random.shuffle(self.key)
            self.difficulty = 'EASY'
        
        def encrypt(self, text):
            result = ""
            for i in range(len(text)):
                char = text[i]
                if char.isupper():
                    c = char.lower() 
                    idx = [*string.ascii_lowercase].index(c)
                    e = self.key[idx]
                    enc = e.upper() 
                    result += enc
                elif char.islower():
                    idx = [*string.ascii_lowercase].index(char)
                    enc = self.key[idx]
                    result += enc
                else:
                    result += char
            return result


    class Caesar:
        """
        A Caesar cipher.
        
        Per Wikipedia (https://en.wikipedia.org/wiki/Caesar_cipher): 
        In cryptography, a Caesar cipher is one of the simplest and most widely 
        known encryption techniques. It is a type of substitution cipher in 
        which each letter in the plaintext is replaced by a letter some fixed 
        number of positions down the alphabet.

        """

        def __init__(self):
            self.name = 'Caesar'
            self.key = random.randint(1, 25)
            self.difficulty = 'EASY'
        
        def encrypt(self, text):
            result = ""
            ascii_A = 65
            ascii_a = 97
            for i in range(len(text)):
                char = text[i]
                if (char.isupper()):
                    result += chr((ord(char) + self.key - ascii_A) % 26 + ascii_A)
                elif (char.islower()):
                    result += chr((ord(char) + self.key - ascii_a) % 26 + ascii_a)
                else:
                    result += char
            return result
    

    class _Xor:
        """
        An XOR cipher.

        This cipher does a byte-by-byte XOR of each character against the key.
        """
        def __init__(self, key=128):
            self.name = 'XOR'
            self.key = key
            self.difficulty = 'MEDIUM'
            
        def encrypt(self, text):
            result = ""
            # transverse the plain text
            for i in range(len(text)):
                c = text[i]
                e = chr(ord(c) ^ self.key)
                result += e
            return result


#if __name__ == '__main__':
#    print('All ciphers: ', Ciphers.__all__())
#    print('-'*40)
#    print('Caesar         (13)                           ', Ciphers.Caesar().encrypt('Foo bar baz'))
#    print('Caesar         (1)                            ',  Ciphers.Caesar(key=1).encrypt('Foo bar baz'))
#    print('XOR            (0)                            ',  Ciphers.Xor(key=0).encrypt('Foo bar baz'))
#    print('XOR            (1)                            ',  Ciphers.Xor(key=65).encrypt('Foo bar baz'))
#
#    cipher = Ciphers.Substitution()
#    print(f'Substitution   ({"".join(cipher.key)})   ',  cipher.encrypt('Foo bar baz'))