'''
!/usr/bin/env python38
@time    :  2020/01/06
@Author  :  WhiteSpider
@File    :  Palindrome.py
@Version : 3.8
@Software: PyCharm
@Blog    : https://github.com/whitespider2020102
说明：具体参考leetcode，回文数
题目：判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
具体思路:回文数是正序读和倒序读都一样的整数，那我们只要根据输入的target，计算出其倒序的整数，如果x==palindrome，那么x就是回文数。
'''

def Palindrome(self, target: int) -> bool:
    if target < 0:
        return False
    palindrome, x = target, 0
    while target:
        x = x * 10 + target % 10
        target = target // 10
    if x == palindrome:
        return True
    else:
        return False


if __name__ == '__main__':
    target: int= 1221
    print(Palindrome('self', target))
