class Base64:
    def __init__(self, a_str="sample"):
        self.a_str = a_str
        self.wordlist = {}
        self.make_wordlist()
        print(self.wordlist)


    def make_wordlist(self):
        a_bit = 0b0
        
        for i in range(65, 65+26):
            self.wordlist[a_bit] = chr(i)
            a_bit += 0b1

        for i in range(97, 97+26):
            self.wordlist[a_bit] = chr(i)
            a_bit += 0b1

        for i in range(0, 10):
            self.wordlist[a_bit] = str(i)
            a_bit += 0b1

        self.wordlist[a_bit] = '+'
        a_bit += 0b1

        self.wordlist[a_bit] = '/'


    def change_bite(self):
        pass

if __name__ == "__main__":
    bas64 = Base64()
