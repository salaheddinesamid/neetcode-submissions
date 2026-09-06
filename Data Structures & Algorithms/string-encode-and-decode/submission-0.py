class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0

        while index < len(s):
            j = index

            while s[j] != '#':
                j += 1

            length = int(s[index:j])

            j += 1

            decoded.append(s[j: j + length])

            index = j + length

        return decoded
