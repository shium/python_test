class Roman2Int:
    def __init__(self, n):
        self.n = n
        self.roman = 'IXCMVLD'
        self.num = [1,10,100,1000,5,50,500]
        self.roman_num = dict(zip(self.roman, self.num))

    def JudgeRoman(self):
        for i in self.n:
            if i not in self.roman:
                print 'input error'
                return
    
    def RomanToInt(self):
        self.JudgeRoman()
        index = 0
        Int = 0
        time = True
        if len(self.n) == 1:
            return self.roman_num[self.n[0]]
        elif len(self.n) == 2 and self.roman_num[self.n[0]] > self.roman_num[self.n[-1]]:
            return self.roman_num[self.n[0]] + self.roman_num[self.n[-1]]
        for i in self.n[:-1]:
            index += 1
            for j in self.n[index]:
                if self.roman_num[i] == self.roman_num[j]:
                    if time and index == 1:
                        Int += self.roman_num[i]
                        time = False
                    for k in self.n[index - 1]:
                        if k == i:
                            Int += self.roman_num[k]
                        else:
                            break
                elif self.roman_num[i] < self.roman_num[j]:
                    Int += self.roman_num[j] - self.roman_num[i]
                elif self.roman_num[i] > self.roman_num[j] and index == 1:
                    Int += self.roman_num[i]
                elif self.roman_num[i] > self.roman_num[j]:
                    Int += self.roman_num[j]
                else:
                    Int += self.roman_num[j]
        return Int
                

if __name__ == '__main__':
    n = raw_input('>>')
    change = Roman2Int(n)
    ans = change.RomanToInt()
    print ans