class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        '''
            UMPIRE method
            Understand:
                Input:
                    Array with cards values
                    groupSize integer that determines the group size. Each value in group size should be increasing order
                Output:
                    Boolean if it's possible

            Match:
                Algorithms:
                    Bucket sort or sort and start building the groups and updating the bucket or mark them in the array as unusable
                    Linear in bucket sort
                    Log-linear if sort
            Plan:
                edge case if the length of the input is not divisible by 4 return false
                create a bucket of size 1001 since 1000 is the max possible nunmber and initiate everything to 0
                iterate over the array hand and make sure to increment the index that matches the value
                iterate over the bucket and use a greedy algorithm to reduce 4 consecutive numbers at a time
                    if you're not able to decrease the value of 4 consecutive numbers then return false
                at the end return true
        '''
        # Implement:
        card_count = len(hand)
        if card_count % groupSize != 0:
            return False
        
        bucket = [0 for i in range(max(hand)+1)]

        for i in range(card_count):
            bucket[hand[i]] += 1
        
        i = 0
        while i < len(bucket) and i + groupSize - 1 < len(bucket):
            if bucket[i] > 0:
                # decrease the next four cards return true if success or false if not possible and then return false
                j = i
                while j - i < groupSize and bucket[j] > 0:
                    bucket[j] -= 1
                    j += 1
                if j - i < groupSize:
                    return False
            if bucket[i] == 0:
                i += 1

        return all(count == 0 for count in bucket)
        '''
            
            Review:
            Evalue:
        '''


