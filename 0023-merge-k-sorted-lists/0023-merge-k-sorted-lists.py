class Solution(object):
    def mergeKLists(self, lists):
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        arr.sort()

        dummy = ListNode(0)
        current = dummy

        for num in arr:
            current.next = ListNode(num)
            current = current.next

        return dummy.next