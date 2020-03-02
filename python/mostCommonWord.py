class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_word_set = set(banned)
        result, dic, count = '', {}, 0
        words = re.findall('\w+', paragraph.lower())
        for word in words:
            if word in banned_word_set:
                continue
            elif word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
            if dic[word] > count:
                count = dic[word]
                result = word
        return result
