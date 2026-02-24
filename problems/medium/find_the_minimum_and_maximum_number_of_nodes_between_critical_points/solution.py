# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        ind = []
        i=2
        m = float('inf')
        if head.next.next == None:
            return [-1,-1]
        while head.next.next != None:
            prev = head.val
            head = head.next
            if (prev < head.val > head.next.val) or (prev > head.val < head.next.val):
                ind.append(i)
            i+=1
        if len(ind) < 2:
            return [-1,-1]
        else:
            for i in range(len(ind)-1):
                m = min(m,abs(ind[i]-ind[i+1]))
            return [m,ind[-1]-ind[0]]