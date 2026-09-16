class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
    #    for i in range(len(strs)):
    #        for j in range(i + 1, len(strs)):
    #            if self.isAnagram(strs[i], strs[j]):
    #                print(strs[i] + " " + strs[j])

