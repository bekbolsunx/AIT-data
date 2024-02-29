class SubstituteCipher():
     def __init__(self, s):
          self.s = s 
          self.new_str =''
          self.start = ord('a')
          self.end = ord('z')
          
          
     def cipher(self):
          for i in self.s:
               if ord(i) + 13 <= self.end:
                    self.new_str += chr(ord(i)+13)
               if ord(i) + 13 >self.end:
                    self.new_str += chr(ord(i)+ 13 - 26)
                    
     def show(self):
          return self.new_str
                    
hello = SubstituteCipher('beksteel')
hello.cipher()
print(hello.show())

    #  Cipher by cesar method 
def cassar(s):
    rear = ""
    letters = {"A": 1, "B": 2, "C" :3, "D": 4, "E" : 5, "F" : 6, "G" : 7}
    for i in s:
        for key, val in letters.items():
            if letter[i] + 3 == None:
                rear += key
            if letters[i] + 3 - 25 == val:
                rear += key


def caesar_cipher(s):
    result = ""
    letters = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}

    for char in s:
        for key, val in letters.items():
            if char.upper() == key:
                result += list(letters.keys())[(val + 3 - 1) % len(letters)]
                break
        else:
            result += char

    return result

# Example usage
plaintext = "HELLO"
ciphertext = caesar_cipher(plaintext)

print(f'Plaintext:  {plaintext}')
print(f'Ciphertext: {ciphertext}')


def withOrd():
    s = "Hello"
    res = ""
    for i in s:
        x = ord(i) + 3
        res += chr(x)
    return res