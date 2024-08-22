class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.lockedDescendants = 0  # Track only number of locked descendants

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
            end = min(i * m + m + 1, len(nodes))
            if start < len(nodes):
                nodes[i].children = nodes[start:end]
                for child in nodes[start:end]:
                    child.parent = nodes[i]

    def lock(self, node_val, uid):
        node = self.node_map[node_val]
        if node.lockedDescendants > 0 or node.isLocked or self.isAncestorLocked(node):
            return False
        
        node.uid = uid
        node.isLocked = True
        self.updateAncestorLocks(node, 1)
        return True
        
    def unlock(self, node_val, uid):
        node = self.node_map[node_val]
        if uid != node.uid or not node.isLocked:
            return False
        node.isLocked = False
        node.uid = None
        self.updateAncestorLocks(node, -1)
        return True
        
    def upgrade_lock(self, node_val, uid):
        node = self.node_map[node_val]
        if node.lockedDescendants == 0 or node.isLocked or self.isAncestorLocked(node):
            return False
        
        if not self.unlockChildren(node, uid):
            return False
        
        return self.lock(node_val, uid)
        
    def isAncestorLocked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False
        
    def unlockChildren(self, node, uid):
        for child in node.children:
            if child.isLocked and child.uid != uid:
                return False
            self.unlock(child.val, uid)
            if not self.unlockChildren(child, uid):
                return False
        return True
        
    def updateAncestorLocks(self, node, change):
        while node.parent:
            node = node.parent
            node.lockedDescendants += change

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