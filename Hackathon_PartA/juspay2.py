# import math

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.uid = None
#         self.parent = None
#         self.children = []
#         self.isLocked = False
#         self.isDescendantLocked = 0
        
# class Tree:
#     def __init__(self, n, m, node_lst, queries):
#         self.node_lst = []
#         self.node_map = {}
#         for node in node_lst:
#             converted = Node(node)
#             self.node_lst.append(converted)
#             self.node_map[node] = converted
            
#         for i in range(int(n/m)):
#             start = i*m + 1
#             end = i*m + m
#             if end > n-1:
#                 end -= end%(n-1)
#             if end < n:
#                 self.node_lst[i].children = self.node_lst[start: end+1]
            
#         for i in range(1, n):
#             self.node_lst[i].parent = self.node_lst[math.ceil(i/m) - 1]

#         self.root = self.node_lst[0]
#         self.processed_queries = [query.split() for query in queries]
    
#     def lock(self, node, uid):
#         if node.isDescendantLocked>0 or node.isLocked or self.isAncestorLocked(node.parent):
#             return False
        
#         node.uid = uid
#         node.isLocked = True
#         parent_node = node.parent
        
#         while parent_node:
#             parent_node.isDescendantLocked += 1
#             parent_node = parent_node.parent
#         return True
        
#     def unlock(self, node, uid):
#         if uid != node.uid or not node.isLocked:
#             return False
#         node.isLocked = False
#         node.uid = None
#         parent_node = node.parent
        
#         while parent_node:
#             parent_node.isDescendantLocked -= 1
#             parent_node = parent_node.parent
#         return True
        
#     def upgrade(self, node, uid):
#         if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
#             return False
            
#         self.unlockChildren(node, uid)
#         self.lock(node, uid)
        
#         return True
        
#     def isAncestorLocked(self, node):
#         while node:
#             if node.isLocked:
#                 return True
#             node = node.parent
#         return False
        
        
#     def unlockChildren(self, node, uid):
#         for child in node.children:
#             self.unlock(child, uid)
#             self.unlockChildren(child, uid)
        
#     def __print_tree(self, node, out):
#         out += node.val + " No of Descendants Locked: " + str(node.isDescendantLocked) + " is Node Locked: " + str(node.isLocked) + ",\n"
#         for child in node.children:
#             out = self.__print_tree(child, out)
#         return out
        
#     def __str__(self):
#         return self.__print_tree(self.root, "")

# # Taking user input
# n = int(input("Enter the number of nodes: "))
# m = int(input("Enter the m-ary parameter: "))

# print("Enter the nodes:")
# nodes = [input().strip() for _ in range(n)]

# print("Enter the number of queries:")
# query_count = int(input().strip())

# print("Enter the queries:")
# queries = [input().strip() for _ in range(query_count)]

# # Creating tree and processing queries
# obj = Tree(n, m, nodes, queries)

# res = []

# for query in obj.processed_queries:
#     if query[0] == "1":
#         res.append(obj.lock(obj.node_map[query[1]], query[2]))
#     elif query[0] == "2":
#         res.append(obj.unlock(obj.node_map[query[1]], query[2]))
#     elif query[0] == "3":
#         res.append(obj.upgrade(obj.node_map[query[1]], query[2]))

# print(res)

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0
        
class MAryTree:
    def __init__(self, root_val):
        self.node_map = {}
        self.root = Node(root_val)
        self.node_map[root_val] = self.root
        
    def make_m_ary_tree(self, node_vals, m):
        nodes = [self.root] + [Node(val) for val in node_vals[1:]]
        self.node_map.update({val: node for val, node in zip(node_vals, nodes)})

        for i in range(len(nodes)):
            start = i * m + 1
            end = i * m + m
            if end >= len(nodes):
                end = len(nodes) - 1
            if start < len(nodes):
                nodes[i].children = nodes[start:end + 1]
                for child in nodes[start:end + 1]:
                    child.parent = nodes[i]

    def lock(self, node_val, uid):
        node = self.node_map[node_val]
        if node.isDescendantLocked > 0 or node.isLocked or self.isAncestorLocked(node.parent):
            return False
        
        node.uid = uid
        node.isLocked = True
        parent_node = node.parent
        
        while parent_node:
            parent_node.isDescendantLocked += 1
            parent_node = parent_node.parent
        return True
        
    def unlock(self, node_val, uid):
        node = self.node_map[node_val]
        if uid != node.uid or not node.isLocked:
            return False
        node.isLocked = False
        node.uid = None
        parent_node = node.parent
        
        while parent_node:
            parent_node.isDescendantLocked -= 1
            parent_node = parent_node.parent
        return True
        
    def upgrade_lock(self, node_val, uid):
        node = self.node_map[node_val]
        if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
            return False
            
        self.unlockChildren(node, uid)
        self.lock(node_val, uid)
        return True
        
    def isAncestorLocked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False
        
    def unlockChildren(self, node, uid):
        for child in node.children:
            self.unlock(child.val, uid)
            self.unlockChildren(child, uid)

def main():
    n, m, t = map(int, input().split())
    names = [input().strip() for _ in range(n)]
    
    tree = MAryTree(names[0])
    tree.make_m_ary_tree(names, m)
    
    for _ in range(t):
        opType, name, id = input().split()
        id = int(id)
        if opType == "1":
            print("true" if tree.lock(name, id) else "false")
        elif opType == "2":
            print("true" if tree.unlock(name, id) else "false")
        elif opType == "3":
            print("true" if tree.upgrade_lock(name, id) else "false")

if __name__ == "__main__":
    main()
