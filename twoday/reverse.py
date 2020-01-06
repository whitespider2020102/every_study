'''
日期：2020-01-04
项目组成员：吴金翰
说明：具体参考leetcode，整数反转
题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转
具体思路:1. 为对当前数取对 10的余数，再一项项填入res尾部，即可完成 int 翻转。
        2.int 取值范围为 [-2^{31}, 2^{31} - 1]，如果翻转数字溢出，则立即返回 0。
git渠道：GitHub个人库
'''


def reverse(self, x: int) -> int:
    y, res = abs(x), 0
    of = (1 << 31) - 1 if x > 0 else 1 << 31 #[-2^{31}, 2^{31} - 1]
    while y != 0:
        res = res * 10 + y % 10 #取余数进入res反转
        if res > of: return 0
        y //= 10   #取y的整数并将y重新进入循环
    return res if x > 0 else -res


if __name__ == '__main__':
    x = 123
    print(reverse('self',x))
