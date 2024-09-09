# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def delOneNode(tn, trgt):
            if tn == None:
                pass
            elif tn.val == trgt:
                return tn.left, tn.right
            elif tn.left != None and tn.left.val == trgt:
                llt = tn.left.left
                lrt = tn.left.right
                tn.left = None
                if llt == None and lrt == None:
                    pass
                else:
                    return llt, lrt
            elif tn.left != None and tn.left.val != trgt and tn.right == None:
                return delOneNode(tn.left, trgt)
            elif tn.left != None and tn.left.val != trgt and tn.right != None and tn.right.val == trgt:
                rlt = tn.right.left
                rrt = tn.right.right
                tn.right = None
                return rlt, rrt
            elif tn.left != None and tn.left.val != trgt and tn.right != None and tn.right.val != trgt:
                left_testing = delOneNode(tn.left, trgt)
                if left_testing != None:
                    return left_testing
                else:
                    return delOneNode(tn.right, trgt)
            elif tn.left == None and tn.right != None and tn.right.val == trgt:
                rlt = tn.right.left
                rrt = tn.right.right
                tn.right = None
                return rlt, rrt
            elif tn.left == None and tn.right != None and tn.right.val != trgt:
                return delOneNode(tn.right, trgt)
            else:
                pass


        forest = [root]
        for val in to_delete:
            new_items = []
            for item in forest:
                if item == None:
                    continue
                items = delOneNode(item, val)
                if items != None:
                    new_items += list(items)
                new_items += [item]
            forest = new_items

        while None in forest:
            forest.remove(None)

        forest = list(set(forest))
        final = []
        for item in forest:
            if item.val in to_delete:
                continue
            else:
                final.append(item)
        return final


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delOneNode(tn, td):
            if tn.val == td:
                l = tn.left
                r = tn.right
                #tn = None   #no difference code
                return l, r
            elif tn.left != None and tn.left.val == td:
                rl = tn.left.left
                rr = tn.left.right
                tn.left = None
                return rl, rr
            elif tn.right != None and tn.right.val == td:
                rl = tn.right.left
                rr = tn.right.right
                tn.right = None
                return rl, rr
            elif tn.left != None and tn.left.val !=td:
                return delOneNode(tn.left, td)
            elif tn.right != None and tn.right.val != td:
                return delOneNode(tn.right, td)
            else:
                pass
    
        def if_monoNode_toDel(tn, td):
            if tn != None and tn.left == None and tn.right == None and tn.val == td:
                return True
            else:
                return False
        
        forest = [root]
        for val in to_delete:
            new_item = []
            for item in forest:
                if item == None:
                    continue
                items = delOneNode(item, val)
                print("root: ", item)
                print("results: ", items)
                new_item += [item]
                if items != None:
                    new_item += list(items)
            forest = new_item

        
        while None in forest:
            forest.remove(None)
        
        # ***clean up treenode in to_delete
        for item in forest:
            if item.val in to_delete:
                if item.right in forest or item.left in forest:
                    forest.remove(item)

        # ***clean up mononode in to_delete
        for item in forest:
            for val in to_delete:
                if if_monoNode_toDel(item, val):
                    forest.remove(item)
    
        return list(set(forest))

