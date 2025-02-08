# class to implement node of RB Tree
class RBNode:
        # constructor
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    # function to get the grandparent of node
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    # function to get the sibling of node
    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left

    # function to get the uncle of node
    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()
    

    

# function to implement Red Black Tree


class RedBlackTree:
        # constructor to initialize the RB tree
    def __init__(self):
        self.root = None       
    

    # Questão: 1) Implementar uma  ́arvore rubro-negra na linguagem de sua escolha com as operações básicas de Inserção (insert), Remoção (deleteByVal) e Impressão (printInOrder).
    # Insert
    def insert(self, value):
        # Regular insertion
        new_node = RBNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.right
        self.insert_fix(new_node)

    # deleteByVal
    def deleteByVal(self, value):
        node_to_remove = self.search(value)

        if node_to_remove is None:
            return

        if node_to_remove.left is None or node_to_remove.right is None:
            self._replace_node(
                node_to_remove, node_to_remove.left or node_to_remove.right)
        else:
            successor = self._find_min(node_to_remove.right)
            node_to_remove.value = successor.value
            self._replace_node(successor, successor.right)

        self.delete_fix(node_to_remove)


    # PrintInOrder
    def printInOrder(self, node):
        if node is not None:
            self.printInOrder(node.left)
            print(node.value, end=" ")
            self.printInOrder(node.right)


    # Questão 2) Implementar as funções find (buscar um elemento específico), findMin (buscar o menor valor) e findMax (buscar o maior valor) em  ́arvores rubro-negras.

    # Find
    def find(self, value):
        curr_node = self.root
        while curr_node is not None:
            if value == curr_node.value:
                print(f"Valor encontrado! {curr_node.value}")
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        print("Valor nao encontrado!")
        return None


    # Find Min
    def findMin(self):
        curr_node = self.root
        while curr_node.left != None:
            curr_node = curr_node.left
        return curr_node.value
        
    # Find Max
    def findMax(self):
        curr_node = self.root
        while curr_node.right != None:
            curr_node = curr_node.right

        return curr_node.value        
    



    # Questão 3) Implementar a função findKth, em que o valor de entrada  ́e o k- ́esimo menor valor (ex:findKth(1) consiste em buscar o menor valor e findKth(2) o segundo menor valor da  ́arvore).

    # FindKth
    def findKth(self, n):
        result = []

        self.inorderTraversal(self.root, result)
        if n <= 0 or n > len(result):
            return None
        return result[n - 1]
    

    # Questão 4) Escreva um método de árvore de busca binária, chamado findInterval, que usa duas chaves, low e high, e imprime todos os elementos X que estão no intervalo especificado por low e high.
    
    # Find Interval
    def findInterval(self, low, high):
        def _findInterval(node, low, high):
            if node is None:
                return

            # Explora a subárvore esquerda se houver chance de encontrar valores no intervalo
            if low < node.value:
                _findInterval(node.left, low, high)

            # Se o valor do nó estiver dentro do intervalo, imprime
            if low <= node.value <= high:
                print(node.value, end=" ")

            # Explora a subárvore direita se houver chance de encontrar valores no intervalo
            if high > node.value:
                _findInterval(node.right, low, high)

        _findInterval(self.root, low, high)

    
        



        
        

    
        

    # Funções auxiliares
    # Function to fix RB tree properties after insertion
    def insert_fix(self, new_node):
        while new_node.parent and new_node.parent.color == 'red':
            if new_node.parent == new_node.grandparent().left:
                uncle = new_node.uncle()
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.grandparent().color = 'red'
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.color = 'black'
                    new_node.grandparent().color = 'red'
                    self.rotate_right(new_node.grandparent())
            else:
                uncle = new_node.uncle()
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.grandparent().color = 'red'
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.color = 'black'
                    new_node.grandparent().color = 'red'
                    self.rotate_left(new_node.grandparent())
        self.root.color = 'black'


    # Function for left rotation of RB Tree
    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    # function for right rotation of RB Tree
    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    # function to replace an old node with a new node
    def _replace_node(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        else:
            if old_node == old_node.parent.left:
                old_node.parent.left = new_node
            else:
                old_node.parent.right = new_node
        if new_node is not None:
            new_node.parent = old_node.parent
    
    # function to fix RB Tree properties after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.right:
                        sibling.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.left:
                        sibling.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def inorderTraversal(self, node, result):
    
        if node is None:
            return
        self.inorderTraversal(node.left, result)
        result.append(node.value)
        self.inorderTraversal(node.right, result)


    

# Example driver code
if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)

    print("Inorder traversal of the Red-Black Tree:")
    tree.printInOrder(tree.root)    
    #tree.printInOrder(tree.root.right)
    print()

    
    #tree.find(20)
    #tree.delete(20)
    #tree.find(20)
    #print(tree.findMin())
    #print(tree.minimum().value)
    #print(tree.findMax())
    #print(tree.findKth(1))
    #print(tree.findKth(3))

    tree.findInterval(25,30)
    print()
    
    
    
    #print("Inorder traversal of the Red-Black Tree after deleting 20")
    #tree.printInOrder(tree.root)
    #print()