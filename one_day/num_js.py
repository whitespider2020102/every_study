'''
日期：2020-01-04
项目组成员：吴金翰
说明：具体参考leetcode，两数之和
题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
具体思路:1.使用一层循环，每遍历到一个元素就计算该元素与 target之间的差值 dif，然后以 dif为下标到数组temp中寻找，
如果 temp[dif] 有值(即不是 undefine)，则返回两个元素在数组 nums 的下标
如果没有找到，则将当前元素存入数组 temp 中(下标: nums[i],Value:i)
git渠道：GitHub个人库
'''

import execjs

def get_spt(nums,target):
    # start = 10
    ctx = execjs.compile(
    '''
  var twoSum = function(nums, target) {
    var temp = [];
    for(var i=0;i<nums.length;i++){
        var dif = target - nums[i]; //得到差值dif
        if(temp[dif] != undefined){ 
            return [temp[dif],i]; //返回两个元素在数组 nums 的下标
        }
        temp[nums[i]] = i; //当前元素存入数组 temp 中(下标: nums[i],Value:i)
    }
};
    ''')
    spt = ctx.call('twoSum',nums, target)
    return spt


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    target = 4
    spt = get_spt(nums,target)
    print (spt)

