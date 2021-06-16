class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        word = ""
        paragraph_list=list(paragraph)
        for i in range(len(paragraph_list)):
            char = paragraph_list[i]
            if char.isalpha():
                word+=char.lower()
            if not char.isalpha() or i == len(paragraph_list)-1:
                if word not in banned and len(word)>=1:
                    words.append(word)
                word=""
        counts = collections.Counter(words)
        return counts.most_common()[0][0]
