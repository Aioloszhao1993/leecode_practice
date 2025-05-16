from attr.validators import min_len


class Solution:
    def longest_common_prefix(self, strs):
        if not strs:
            return ""
        # 获取一个最短的字符串，最长公共前缀也不会比这个长
        min_len = min(len(s) for s in strs)
        # 遍历最短长度
        for i in range(min_len):
            # 获取第一个字符串i位置的字符
            current_str = strs[0][i]
            for s in strs[1:]:
                # 和剩下字符串i位置的字符做对比，不同则返回i之前的字符串
                if s[i] != current_str:
                    return strs[0][:i]
        # 全部一致，则返回整个最短字符串作为公共前缀
        return strs[0][:min_len]


if __name__ == "__main__":
    s = Solution()
    tmp1 = ["flower", "flow", "flight"]
    res = s.longest_common_prefix(tmp1)
    print(f"res:{res}")
    tmp2 = ["dog","dofsgcar","car"]
    res = s.longest_common_prefix(tmp2)
    print(f"res:{res}")
