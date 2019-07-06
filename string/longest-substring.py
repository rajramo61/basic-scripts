# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         total_chars = len(s)
#         max_str_len = i = j = 0
#
#         while i < total_chars and j < total_chars:
#             if s[j] in char_set:
#                 char_set.remove(s[i])
#                 i += 1
#             else:
#                 char_set.add(s[j])
#                 j += 1
#                 max_str_len = max(max_str_len, j - i)
#         return max_str_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        total_chars = len(s)
        max_str_len = i = j = 0

        while i < total_chars and j < total_chars:
            if s[j] in char_index_map:
                i = max(char_index_map.get(s[j]), i)
            else:
                char_index_map[s[j]] = j + 1
                max_str_len = max(max_str_len, j - i + 1)
            j += 1
        return max_str_len


def stringToString(input):
    import json

    return json.loads(input)


def main():
    import sys
    import io

    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line)

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
