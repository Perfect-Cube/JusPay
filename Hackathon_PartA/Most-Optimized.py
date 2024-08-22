class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.lockedDescendants = set()  # Track locked descendants as a set

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
        if node.lockedDescendants or node.isLocked or self.isAncestorLocked(node):
            return False
        
        node.uid = uid
        node.isLocked = True
        self.updateAncestorLocks(node, node)
        return True
        
    def unlock(self, node_val, uid):
        node = self.node_map[node_val]
        if uid != node.uid or not node.isLocked:
            return False
        
        node.isLocked = False
        node.uid = None
        self.updateAncestorLocks(node, node, remove=True)
        return True
        
    def upgrade_lock(self, node_val, uid):
        node = self.node_map[node_val]
        if not node.lockedDescendants or node.isLocked or self.isAncestorLocked(node):
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
        locked_descendants = list(node.lockedDescendants)  # Work on a copy to avoid modification issues
        for child in locked_descendants:
            if child.uid != uid:
                return False
            self.unlock(child.val, uid)
        return True
        
    def updateAncestorLocks(self, node, locked_node, remove=False):
        change_fn = set.remove if remove else set.add
        while node.parent:
            node = node.parent
            if remove:
                node.lockedDescendants.remove(locked_node)
            else:
                node.lockedDescendants.add(locked_node)

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
