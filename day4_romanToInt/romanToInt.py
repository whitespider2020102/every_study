'''
!/usr/bin/env python38
@time    :  2020/01/07
@Author  :  WhiteSpider
@File    :  romanToint.py
@Version : 3.8
@Software: PyCharm
@Blog    : https://github.com/whitespider2020102
说明：具体参考leetcode，罗马数变整数
题目：给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
具体思路:构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
这样一来，遍历整个 romana的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内
如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
举个例子:遍历经过 I的时候先记录 I的对应值 1再往前移动一步记录 IV的值 3，加起来正好是 IV的真实值 4。
max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0]的情况
'''


def romanToint(romana):
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}
    return sum(d.get(romana[max(i-1, 0):i+1], d[n]) for i, n in enumerate(romana))

if __name__== '__main__':
    romana ='MCMXC'
    target = romanToint(romana)
    print(target)















