# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            
        curr1 = list1
        curr2 = list2

        if curr1 == None and curr2 == None:
            return None
        if (curr2 == None and curr1 != None):
            curr = ListNode(curr1.val)
            curr1 = curr1.next
            curr.next = self.mergeTwoLists(Solution, curr1, curr2)
            return curr
        if (curr1 == None and curr2 != None):
            curr = ListNode(curr2.val)
            curr2 = curr2.next
            curr.next = self.mergeTwoLists(Solution, curr1, curr2)
            return curr
        if curr1.val <= curr2.val:
            curr = ListNode(curr1.val)
            curr1 = curr1.next
            curr.next = self.mergeTwoLists(Solution, curr1, curr2)
            return curr
        if curr2.val < curr1.val:
            curr = ListNode(curr2.val)
            curr2 = curr2.next
            curr.next = self.mergeTwoLists(Solution, curr1, curr2)
            return curr



def lenNode(ln):
    cnt = 0
    while ln != None:
        cnt += 1
        ln = ln.next
    return cnt

def enumNode(ln):
    lnl = []
    while ln != None:
        lnl.append(ln.val)
        ln = ln.next
    return lnl

def merge_twoNodes(list1, list2):
    curr1 = list1
    curr2 = list2

    if curr1 == None and curr2 == None:
        return None
    if (curr2 == None and curr1 != None):
        curr = ListNode(curr1.val)
        curr1 = curr1.next
        curr.next = merge_twoNodes(curr1, curr2)
        return curr
    if (curr1 == None and curr2 != None):
        curr = ListNode(curr2.val)
        curr2 = curr2.next
        curr.next = merge_twoNodes(curr1, curr2)
        return curr
    if curr1.val <= curr2.val:
        curr = ListNode(curr1.val)
        curr1 = curr1.next
        curr.next = merge_twoNodes(curr1, curr2)
        return curr
    if curr2.val < curr1.val:
        curr = ListNode(curr2.val)
        curr2 = curr2.next
        curr.next = merge_twoNodes(curr1, curr2)
        return curr


def reverseNode(ln):
    lstnd = ListNode(ln.val)
    lstnd.next = None
    curr = ln.next
    while curr != None:
        cn = ListNode(curr.val)
        cn.next = lstnd
        if curr.next != None:
            head = ListNode(curr.next.val)
            head.next = cn
        else:
            head = cn
        curr = curr.next
        lstnd = cn
    return head


ln1 = ListNode(1)
ln1.next = ListNode(3)
ln1.next.next = ListNode(7)
ln1.next.next.next = ListNode(11)

ln2 = ListNode(2)
ln2.next = ListNode(4)
ln2.next.next = ListNode(6)

ln3 = ListNode(17)
ln3.next = ListNode(8)
ln3.next.next = ListNode(13)
ln3.next.next.next = ListNode(5)
test_rev = reverseNode(ln3)
print("reversed: ", enumNode(test_rev))


mn = merge_twoNodes(ln1, ln2)
cmn = Solution.mergeTwoLists(Solution, ln1, ln2)
print("merged: ", enumNode(mn))


def bubble_sort(num):
    index = 0
    minm = num[0]
    cnt = 0
    while cnt != len(num):
        for i in range(cnt, len(num)):
            if num[i] <= minm:
                minm = num[i]
                index = i
        num[cnt], num[index] = num[index], num[cnt]
        cnt += 1
    return num

def sortNode(ln):
    curr = ln
    sorted = False
    if curr.next == None:
        sorted =True
    

    while not sorted:
        print("while loop initial", curr.val)
        print("listing: ",enumNode(curr))
        operated = False
        if curr.next != None and not (curr.val <= curr.next.val):
            print(enumNode(curr))
            a, b = curr.val, curr.next.val
            curr.val = b
            curr.next.val = a
            operated = True
            print('switched', enumNode(curr))
        curr = curr.next
        if curr == None:
            curr = ln
            operated = True
            print('ended once')
        print("while loop ending: ", enumNode(curr))
        if curr.next != None and curr.next.val < curr.val: # additional checking
            operated = True     # since the curr is re-generated.
        sorted = not operated
    return ln


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None:
        return None
    last_val = head.val
    curr = ListNode(last_val)
    if head.next == None:
        curr.next == None
    elif head.next != None:
        while head.next.val == last_val:
            head = head.next
            if head.next == None:
                break
        curr.next = deleteDuplicates(head.next)
    return curr


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head == None:
        return None
    curr = head
    while curr.val == val:
        curr=curr.next
        if curr == None:
            return None
    new = ListNode(curr.val)
    if curr.next != None:
        if curr.next.val == val:
            curr = curr.next
        new.next = removeElements(curr.next, val)
    return new
        

test_bs = enumNode(sortNode(sortNode(ln3)))
print(test_bs)





################################################################################################################################

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def lenNode(ln):
            cnt = 0
            while ln != None:
                cnt += 1
                ln = ln.next
            return cnt

        if l1 == None or l1 == ListNode(0):
            return l2
        if l2 == None or l2 == ListNode(0):
            return l1

        cnt_a = lenNode(l1)
        cnt_b = lenNode(l2)
        if cnt_b > cnt_a:
            na, nb = l2, l1
            cnta, cntb = cnt_b, cnt_a
        else:
            na, nb = l1, l2
            cnta, cntb = cnt_a, cnt_b
        
        num = 0
        while cnta > cntb:
            num = 10*num + na.val
            na = na.next
            cnta -= 1
        while cnta != 0:
            num = 10*num + na.val+nb.val
            na = na.next
            nb = nb.next
            cnta -= 1
        
        snum = [int(str(num)[i]) for i in range(len(str(num)))]     # partial solution, e.g. required reading str for int as calculator

        def ltn(lst):
            if lst == []:
                return None
            n = ListNode(lst[0])
            n.next = ltn(lst[1:])
            return n

        return ltn(snum)
