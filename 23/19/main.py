import time

class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.right = None
        self.left = None
        
        
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if test else "kuler.txt"
        self.data = open(self.filename).read().rstrip().split("\n")
        self.nodes = {}
        self.fav1 = "7D99B6" if test else "811A89"
        self.fav2 = "E06162" if test else "8EAA54"
        
        
    def solve(self):
        root = self.buildTree()
        
        fav1 = self.nodes[int(self.fav1, 16)]
        fav2 = self.nodes[int(self.fav2, 16)]
        
        parents1 = self.getParents(fav1)
        parents2 = self.getParents(fav2)
        
        common : Node = None
        for i in range(len(parents1)):
            if parents1[i] in parents2:
                common = parents1[i]
                break
        
        return hex(common.key)
        
    def getParents(self, node):
        parents = []
        while node.parent != None:
            parents.append(node.parent)
            node = node.parent
            
        return parents
        
        
    def buildTree(self):
        root = Node(int(self.data[0][1:], 16), None)
        for i in range(1, len(self.data)):
            key = int(self.data[i][1:], 16)
            currentNode = root
            while True:
                if key <= currentNode.key:
                    if currentNode.left == None:
                        n = Node(key, currentNode)
                        self.nodes[key] = n
                        currentNode.left = n
                        break
                    currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        n = Node(key, currentNode)
                        self.nodes[key] = n
                        currentNode.right = n
                        break
                    currentNode = currentNode.right
        return root
            
            
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("--TEST--")
    print(f"Result: {s.solve()}")
    
    s = Solution()
    print("--MAIN--")
    print(f"Result: {s.solve()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()