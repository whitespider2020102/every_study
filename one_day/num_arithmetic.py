'''
日期：2020-01-04
项目组成员：吴金翰
说明：具体参考leetcode，两数之和
题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
具体思路:1.使用enumerate方法遍历索引和数字，如果目标值减去数字的值在字典内，则返回要被减数的索引和结果的索引
git渠道：GitHub个人库
'''



def twoSum(nums, target):
    hashmap={}
    for i,num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i,hashmap.get(target - num)]
        hashmap[num] = i #这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == '__main__':
    nums = [4,9,12,16,17,18,0,3,1]
    target = 1
    print(twoSum(nums , target))
