def Goldbach(even_num):
    prime = [x for x in range(2, even_num) if x % 2 == 1]
    for i in prime:
        for j in prime:
            add = i + j
            if add == even_num:
                print i, j
                return

def check(num):
    if num % 2 == 1:
        print 'Input error, please input a even number'
    else:
        Goldbach(num)

if __name__ == '__main__':
    num = input('Please input a even number: ')
    check(num)
