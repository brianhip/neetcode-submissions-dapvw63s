class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # convert order into a dictionary witht eh asssociated rank to each letter
        # if len(words) == 1:
        #     return True
        # if len(order) != len(set(order)):
        #     return False
        # letter_rank = {}
        # for index, char in enumerate(order):
        #     letter_rank[char] = index
        # for i in range(1, len(words)):
        #     word_one = words[i - 1]
        #     word_two = words[i]
        #     min_len = min(len(word_one), len(word_two))
        #     same = 0
        #     while same < min_len:
        #         char_one = word_one[same]
        #         char_two = word_two[same]
        #         if letter_rank[char_one] > letter_rank[char_two]:
        #             return False
        #         elif letter_rank[char_one] < letter_rank[char_two]:
        #             break
        #         same += 1
        #     if same == len(word_two) and len(word_one) > len(word_two):
        #         return False
            
        # return True


        if len(words) == 1:
            return True
        if len(order) != len(set(order)):
            return False
        priority = {char: index for index, char in enumerate(order)}
        sorted_words = sorted(words, key= lambda word: [priority.get(char, 999) for char in word])
        return words == sorted_words