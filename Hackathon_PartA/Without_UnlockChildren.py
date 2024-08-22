class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0
        self.lockedDescendants = set()  # Track locked descendants

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
            parent_node.lockedDescendants.add(node)
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
            parent_node.lockedDescendants.remove(node)
            parent_node = parent_node.parent
        return True
        
    def upgrade_lock(self, node_val, uid):
        node = self.node_map[node_val]
        if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
            return False
        
        # Unlock all locked descendants efficiently
        for locked_descendant in list(node.lockedDescendants):
            self.unlock(locked_descendant.val, locked_descendant.uid)
        
        # Lock the current node
        return self.lock(node_val, uid)
        
    def isAncestorLocked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False

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
