#!/usr/bin/env python3
#! /usr/bin/python3
# -*- coding:UTF-8 -*-
#作者：王硕
#学号：320170941311
#邮箱: kyiwong97@gmail.com
#环境：python 3.7.4

m = input('请输入16进制解密密文：')
_m = []
for n in m:
    _m += list(str('{:04b}'.format(int(n,16))))#str('{:04b}'.format(int(sHe[j][hang * 16 + lie]))).replace('', ' ')[1:-1].split(' ')
m = _m


key = input('请输入16进制加密密钥：')
_key = []
for n in key:
    _key += list(str('{:04b}'.format(int(n,16))))#str('{:04b}'.format(int(sHe[j][hang * 16 + lie]))).replace('', ' ')[1:-1].split(' ')
key = _key

#置换选择1，2
z1 = "57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4".split(',')
z2 = "14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32".split(',')

#特殊的左移位数
teshuTable = ['1','2','9','16']

def zhihuanxuanze1(key,z1):
    _k = []
    for n in z1:
        n = int(n)-1
        _k.append(key[n])
    return _k

def xunhuanzuoyi(list,k):
    return list[k:]+list[:k]

def zhihuanxuanze2(c,d,z2,t):
    roundkey = []
    for n in range(1,17):
        if str(n) in t:
            c = xunhuanzuoyi(c, 1)
            d = xunhuanzuoyi(d, 1)
        else:
            c = xunhuanzuoyi(c, 2)
            d = xunhuanzuoyi(d, 2)
        k = c+d
        roundkey.append(zhihuanxuanze1(k,z2))
    return roundkey
#IP 与 IP逆

IP = "58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7".split(',')
IP_1 =  "40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25".replace(", ",', ').split(", ")

#扩展变换E
E = '32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1'.split(',')
P = '16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25'.split(',')

#s盒

s1 = '14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13'.split(',')
s2 = '15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9'.split(',')
s3 = '10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12'.split(',')
s4 = '7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14'.split(',')
s5 = "2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3".split(',')
s6 = "12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13".split(',')
s7 = '4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12'.split(',')
s8 = '13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11'.split(',')
sHe = [s1,s2,s3,s4,s5,s6,s7,s8]
#初始置换函数
def chushizhihuan(m,table):
    newM = []
    for n in table:
        n = int(n)
        newM.append(m[n - 1])
    return newM

#F轮变换
def F(r,n,roundkey,sHe): #sHe 表中表
    r = chushizhihuan(r,E)
    shuchu = []
    for j in range(0,48):
        r[j] = str(int(r[j])^int(roundkey[n-1][j]))
    for j in range(0,8):
        temp = r[j*6:(j+1)*6]
        hang = int(temp[0])*2+int(temp[5])
        lie = int(temp[1])*(2**3)+int(temp[2])*(2**2)+int(temp[3])*2+int(temp[4])
        shuchu += str('{:04b}'.format(int(sHe[j][hang * 16 + lie]))).replace('', ' ')[1:-1].split(' ') # 现在转为10进制8位2进制
    return  chushizhihuan(shuchu,P)


#加密轮
def enc(m,roundkey,sHe):
    l, r = m[:32], m[32:]
    for n in range(1,17): #多交换了一轮 给我换回去！
        temp = r
        r = F(r,17-n,roundkey,sHe)
        for j in range(0,32):
            l[j] = str(int(l[j])^int(r[j]))
        if n != 16:
            r = l
            l = temp
        else:
            r = temp
    #    print("L",n+1,' = ',l,'\nR',n+1,' = ',r)
    m = l+r
# 逆初始置换
    return chushizhihuan(m, IP_1)


#main
#生成轮密钥
key = zhihuanxuanze1(key,z1)
c,d = key[:28],key[28:]
roundkey = zhihuanxuanze2(c,d,z2,teshuTable)

#初始置换
m = chushizhihuan(m,IP)
#print('初始置换后明文为：',m)
#16轮加密来袭

m = enc(m,roundkey,sHe)
#解密完成了哦
c = ''
for n in range(0,64):
    if n %4 ==0:
        c += str(hex(int(m[n])*8+int(m[n+1])*4+int(m[n+2])*2+int(m[n+3]))).replace('0x','')
print("解密明文为：",c)