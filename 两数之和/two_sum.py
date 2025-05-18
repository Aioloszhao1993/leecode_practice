class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return ""


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    res = s.two_sum(nums, target)
    print(f"res:{res}")
    nums = [3,2,4]
    target = 6
    res = s.two_sum(nums, target)
    print(f"res:{res}")
    nums = [3, 3]
    target = 7
    res = s.two_sum(nums, target)
    print(f"res:{res}")
