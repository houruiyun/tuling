# coding=utf-8
#/usr/bin/python
#author:houry
#date: 2018\11\5 0005 0:15
import random


def save():
    #定义一个空字符串用于拼接
    str_num = ''
    for i in range(4):
        num= random.randrange(97,123)
        str_s = chr(num)
        str_num = str_num+str_s
        print(str_num)

num = input('请输入一个三位数:')
random_num = random.randrange(100,1000)

if  num.isdigit() and 100<=int(num) <= 999:
    num = int(num)
    random_num = int(random_num)
    if num >random_num:
        bai = num//100
        shi = num%100//10
        ge = num%10
        print('这个三位数的个位是{}十位是{}百位是{}'.format(ge,shi,bai))
        print('这个三位数的个位是%s十位是%s百位是%s' % ge,shi,bai)
    if num == random_num:
        print('你中奖了',random_num)
    if num < (random_num):
        save()
else:
    print('请按规定输出')
