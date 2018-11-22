class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs = []
        lengths = []
        prefix = ''
        if len(strs) > 0:
            len_strs = map(lambda x: len(x), strs)
            lengths = list(len_strs)
            min_string = strs[lengths.index(min(lengths))]
            min_len = min(lengths)
            for i in range(min_len):
                pick_it = True
                for word in strs:
                    if word[i] != min_string[i]:
                        pick_it = False
                if pick_it:
                    prefix += min_string[i]
                else:
                    break
        return prefix
