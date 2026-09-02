class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            
            if tuple(count) not in result:
                result[tuple(count)] = []
                
            result[tuple(count)].append(word)
        return list(result.values())
        