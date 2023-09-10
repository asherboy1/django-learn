from copy import deepcopy
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []
        elif len(nums) < 3:
            return []

        len_ = len(nums)
        dict_ = {}
        for i in range(len_):
            str1 = str(i+1) + "_" + str(nums[i])
            dict_[str1] = nums[i]

        ans = []

        # print(dict_)
        for i in range(len_):
            str1 = str(i+1) + "_" + str(nums[i])
            for k in range(i, len_):
                if i == k:
                    continue
                str2 = str(k+1) + "_" + str(nums[k])
                print(str2)
                sum_ = nums[i] + nums[k]
                target = 0 - sum_

                tmp_dict = deepcopy(dict_)
                tmp_dict.pop(str1, 0)
                tmp_dict.pop(str2, 0)
                target_value = tmp_dict.values()
                # print(target_value)
                if target in target_value:
                    list1 = [nums[i], target, nums[k]]
                    print(list1)
                    list1.sort()
                    if list1 not in ans:
                        ans.append(list1)
                    
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.threeSum([3,0,-2,-1,1,2]))
    num1 = -2
    print(0 - num1)
