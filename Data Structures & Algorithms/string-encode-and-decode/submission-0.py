class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in strs:
            s_length = len(s)

            encoded += str(s_length) + "#" + s

        return encoded


    def decode(self, s: str) -> List[str]:

        encoded = []
        index = 0

        while index < len(s):
            j = index

            while s[j] != '#':
                j += 1

            w_length = int(s[index : j])
            word = s[j + 1 : j + 1 + w_length]

            encoded.append(word)

            index = j + 1 + w_length

        return encoded
            