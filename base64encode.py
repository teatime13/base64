class Base64:
    def __init__(self):
        #self.debug = True
        self.debug =False
        self.a_str = ''
        self.wordlist = {}
        self.bits = ''
        self.string_after_conversion = ''
        self.six_bit_list = []
        self.encoded_data = ''

        self.make_wordlist()

    def __str__(self):
        return self.encoded_data


    def make_wordlist(self):
        a_bit = 0b0
        
        for i in range(65, 65+26):
            self.wordlist[format(a_bit, '06b')] = chr(i)
            a_bit += 0b1

        for i in range(97, 97+26):
            self.wordlist[format(a_bit, '06b')] = chr(i)
            a_bit += 0b1

        for i in range(0, 10):
            self.wordlist[format(a_bit, '06b')] = str(i)
            a_bit += 0b1

        self.wordlist[format(a_bit, '06b')] = '+'
        a_bit += 0b1

        self.wordlist[format(a_bit, '06b')] = '/'

        if self.debug:
            print(self.wordlist)

    def character_to_bit(self):
        self.bits = ''
        for s in self.a_str:
            self.bits += format(ord(s), '08b')

        if self.debug:
            print(self.bits)

    def splitting_to_6_bit(self):
        self.six_bit_list = [self.bits[i: i+6] for i in range(0,len(self.bits),6)]

        if len(self.six_bit_list[-1]) < 6:
            self.six_bit_list[-1] += '0' * (6 - len(self.six_bit_list[-1]))

        if self.debug:
            print(self.six_bit_list)

    def converting_from_table(self):
        self.string_after_conversion = ''
        for s in self.six_bit_list:
            self.string_after_conversion += self.wordlist[s]

        if self.debug:
            print(self.string_after_conversion)

    def replenishment_equal(self):
        if len(self.string_after_conversion) % 4 != 0:
            self.string_after_conversion += '=' * (4 - len(self.string_after_conversion) % 4)

        self.encoded_data = self.string_after_conversion

        if self.debug:
            print(self.string_after_conversion)

    def encode(self, a_str="sample"):
        self.a_str = a_str
        self.character_to_bit()
        self.splitting_to_6_bit()
        self.converting_from_table()
        self.replenishment_equal()

        print(self.a_str + ' : ' + self.encoded_data)

if __name__ == "__main__":
    base64 = Base64()
    base64.encode('sample')
    print(base64)
    base64.encode('A')
    print(base64)
    base64.encode('ABCDEFG')
    print(base64)
