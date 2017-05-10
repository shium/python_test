# -*- coding: utf-8 -*-


#读取文本，将文本切成list，并返回
def chippings():
    f = open('1.txt', 'r+')
    str_book = f.read()
    f.close()
    list_book = []
    head = 0
    str_book = str_book.lower()
    for i in range(len(str_book)):
        if str_book[i] == ' ' or str_book[i] =='\n':
            rear = i
            list_book.append(str_book[head:rear])
            head = i + 1
    #print list_book
    return list_book

#统计list中相同字符
def sort(list_book):
    set_list = set(list_book)
    for item in set_list:
        if len(item) >= 7:
            print item, '\t', list_book.count(item)
        else:
            print item, '\t\t', list_book.count(item)
    
list_book = chippings()
sort(list_book)