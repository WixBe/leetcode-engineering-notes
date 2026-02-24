from collections import Counter

class Solution:
    def succ(self, hand, groupSize, i, n):
        nxtval = hand[i]+1
        hand[i]=-1
        count = 1
        i+=1
        while i<n and count<groupSize:
            if hand[i] == nxtval:
                nxtval = hand[i]+1
                hand[i]=-1
                count+=1
            i+=1
        return count == groupSize

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize!=0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i]>=0:
                if not self.succ(hand, groupSize, i, n):
                    return False
        return True