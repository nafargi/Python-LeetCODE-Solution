# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:


        remove = 0
        sum = 0
        letter = list(''.join(words))
        j = 0
        for i in range(len(words)):
            chars_list = list(chars)
            for _ in range(len(words[i])):
                if letter[j] in chars_list:
                    print(letter[j])
                    chars_list.remove(letter[j])
                    remove += 1
                j += 1
            if remove == len(words[i]):
                sum += remove
            remove = 0
        return sum

        
        # remove = 0
        # sum = 0
        # letter =list(words[i])
        # for i in range(len(words)):
           
        #     chars_list = list(chars)
        #     for j in range(len(letter)):
        #         if letter[j] in chars_list:
        #             chars_list.remove(letter[j])
        #             remove += 1
        #     if remove == len(letter):
        #         sum += remove
        #     remove = 0
        # return sum
                    