# Medium 1: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# TC: O(N) where N is the tree traversal 
# SC: O(H) where H is the height of the Tree.

class Node:
    # defining constructor to create a node
    def __init__(self, key) -> None:
        # setting left and right child equals to NULL
        self.right = None
        self.left = None

        # inserting data into the node
        self.key = key

# This function return pointer to LCA of two given values p and q
def findLCA(root, p, q, v):
 
    # Base Case
    if root is None:
        return None

    if root.key == p:
        v[0] = True
        return root
 
    if root.key == q:
        v[1] = True
        return root
 
    # Look for keys in left and right subtree
    left_lca = findLCA(root.left, p, q, v)
    right_lca = findLCA(root.right, p, q, v)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

def find(root, k):
 
    # Base Case
    if root is None:
        return False
 
    # If key is present at root, or if left subtree or right
    # subtree , return true
    if (root.key == k or find(root.left, k) or
            find(root.right, k)):
        return True
 
    # Else return false
    return False
 
# This function returns LCA of n1 and n2 on value if both
# n1 and n2 are present in tree, otherwise returns None
 
def LCA(root, n1, n2):
 
    # Initialize n1 and n2 as not visited
    v = [False, False]
 
    # Find lca of n1 and n2 using the technique discussed above
    lca = findLCA(root, n1, n2, v)
 
    # Returns LCA only if both n1 and n2 are present in tree
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
            find(lca, n1)):
        return lca
 
    # Else return None
    return None

# Driver program to test above function

root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)

lca = LCA(root, 2, 4)
 
if lca is not None:
    print("LCA(4, 5) = ", lca.key)
else:
    print("Keys not present")
 
