class Solution:
    def reverse(self, x: int) -> int:
        use_str = str(x)
        new_str = ""
        # x>0,直接反转字符串
        if x > 0:
            new_str = use_str[::-1]
        # x<0,反转字符串后，第一位加-号，并去掉最后一位
        elif x < 0:
            new_str = "-" + use_str[::-1][:len(use_str) - 1]
        else:
            new_str = x
        # 反转后的值超出此范围，返回0
        if int(new_str) < -2**31 or int(new_str) > 2**31 - 1:
            return 0
        return int(new_str)


if __name__ == "__main__":
    s = Solution()
    num = 123
    res = s.reverse(num)
    print(f"res:{res}")
    num = -123
    res = s.reverse(num)
    print(f"res:{res}")
    num = 120
    res = s.reverse(num)
    print(f"res:{res}")
    num = 0
    res = s.reverse(num)
    print(f"res:{res}")
    num = 1534236469
    res = s.reverse(num)
    print(f"res:{res}")
