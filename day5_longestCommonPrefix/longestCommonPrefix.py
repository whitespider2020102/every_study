'''
!/usr/bin/env python38
@time    :  2020/01/08
@Author  :  WhiteSpider
@File    :  longestCommonPrefix.py
@Version : 3.8
@Software: PyCharm
@Blog    : https://github.com/whitespider2020102
说明：具体参考leetcode，最长公共前缀
题目：编写一个函数来查找字符串数组中的最长公共前缀,如果不存在公共前缀，返回空字符串 ""。。
具体思路:Python 特性，取每一个单词的同一位置的字母，看是否相同。
zip(*strs) 可理解为解压，返回二维矩阵式
set() 函数创建一个无序不重复元素集
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


if __name__ == '__main__':
    strs = ['flower', 'flow', 'flight']
    result = Solution()
    results = result.longestCommonPrefix(strs)
    print(results)
