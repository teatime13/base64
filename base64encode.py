class Base64:
    def __init__(self, a_str="sample"):
        self.debug = True
        
        self.a_str = a_str
        self.wordlist = {}
        self.make_wordlist()
        self.change_bite()


    def make_wordlist(self):
        a_bit = 0b0
        
        for i in range(65, 65+26):
            self.wordlist[chr(i)] = a_bit
            a_bit += 0b1

        for i in range(97, 97+26):
            self.wordlist[chr(i)] = a_bit
            a_bit += 0b1

        for i in range(0, 10):
            self.wordlist[str(i)] = a_bit
            a_bit += 0b1

        self.wordlist['+'] = a_bit
        a_bit += 0b1

        self.wordlist['/'] = a_bit

        if self.debug:
            print(self.wordlist)


    def change_bite(self):
        bits = ''
        for s in self.a_str:
            bits += str(format(self.wordlist[s], '06b'))

        if self.debug:
            print(bits)

    def encode(self):
        pass


if __name__ == "__main__":
    base64 = Base64('sample')
    base64 = Base64('A')
    base64 = Base64('B')
