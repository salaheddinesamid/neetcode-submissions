class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for s in strs:
            key = str(sorted(s))
            if key not in map:
                map[key] = []

            map[key].append(s)

        return (list(map.values()))