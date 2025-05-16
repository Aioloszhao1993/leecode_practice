class Solution:
    def longest_common_prefix(self, strs):
        # 取列表中的第一个字符串
        s0 = strs[0]
        # 获取第一个字符串中所有字符和下标
        for j, c in enumerate(s0):
            # 从第二个元素开始，循环获取字符串列表中的字符串
            for s in strs[1:]:
                # 如果当前元素使用第一个元素下标获取到的值，和第一个元素下标对应的值不同，则返回当前下标之前的字符串
                if s[j] != c:
                    return s0[:j]
        # 全部一致，则返回第一个字符串
        return s0

if __name__ == "__main__":
    s = Solution()
    tmp1 = ["flower", "flow", "flight"]
    res = s.longest_common_prefix(tmp1)
    print(f"res:{res}")
    tmp2 = ["dog","dofsgcar","car"]
    res = s.longest_common_prefix(tmp2)
    print(f"res:{res}")
