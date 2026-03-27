class Solution:
    def findKth(self, head, k):
        k -= 1
        while head and k > 0:
            head = head.next
            k -= 1
        return head

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head, k):
        temp = head
        prevLast = None

        while temp:
            kth = self.findKth(temp, k)
            if not kth:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = kth.next
            kth.next = None

            newHead = self.reverseList(temp)

            if temp == head:
                head = newHead
            else:
                prevLast.next = newHead

            temp.next = nextNode
            prevLast = temp
            temp = nextNode

        return head