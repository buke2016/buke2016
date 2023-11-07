import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while (arr[j-1] > arr[j] and j > 0):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        
    return(arr)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(right >= left):
        mid = (left + right) // 2 
        print(arr[left:right])
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
    
    return -1

class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class singly_linked_list:
    def __init__(self,val):
        self.head_node = node(val)
    def __str__(self):
        res = ''
        current = self.head_node
        count = 0
        while current != None:
            res += '{}: {} -> '.format(count,current.val)
            current = current.next
            count += 1
        res +=  'End'
        return res

    def add_node(self, val, index = None):
        current = self.head_node

        if(index == None):

            while(current.next != None):
                current = current.next
            current.next = node(val)
        else:
            if index == 0:
                new = node(val)
                new.next = self.head_node
                self.head_node = new
            else:
                previous = self.head_node
                current = previous.next
                
                for i in range(1, index):
                    previous, current = current, current.next

                    if current == None:
                        raise IndexError('Index Out of Bounds')
                
                previous, current = current, current.next
                new = node(val)
                previous.next, new.next = new, current

                    
                



class queue:
    def __init__(self):
        self.lis = None
        

    def add(self, val):
        if (self.lis == None):
            self.lis = singly_linked_list(val)
            self.end = self.lis.head_node
        else:
            
            self.lis.add_node(val)

    def pop(self):
        temp = self.lis.head_node
        self.lis.head_node = temp.next

        return temp.val
    def __str__(self):
        return str(self.lis)


class Stack:
    def __init__(self, val = None):

        if val == None:
            self.lis = None
        else:
            self.lis = singly_linked_list(val)
    def add(self, val):
        if self.lis == None:
            self.lis = singly_linked_list(val)
        else:
            self.lis.add_node(val, 0)
    def pop(self):
        temp = self.lis.head_node
        self.lis.head_node = temp.next
        return temp.val
    def __str__(self):
        return str(self.lis)

#TODO fix printing tree repr function
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
    def add_node(self, val):
        if self.val < val:
            if self.left == None:
                self.left = TreeNode(val)
                self.left.parent = self
            else:
                self.left.add_node(val)
        else:
            if self.right == None:
                self.right = TreeNode(val)
                self.right.parent = self
            else:
                self.right.add_node(val)
    def print(self,lvl):
        res = ' -' * lvl
        res += str(self.val)

        print(res)
        if self.left != None:
            self.left.print(lvl + 1)
        if self.right != None:
            self.right.print(lvl + 1)
    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)

#TODO test delete node function
class BinaryTree:
    def __init__(self, val = None):
        if val == None:
            self.root = None
        else:
            self.root = TreeNode(val)
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.add_node(val)
    def print(self):
        self.root.print(0)

        
    def delete(self, val):
        curr = self.root

        while (curr.val != val):
            if curr.val == None:
                break
            else:
                if val > curr.val:
                    curr = curr.right
                else:
                    curr = curr.left



        if curr == None:
            return 

        parent = curr.parent

        if curr.left == None and curr.right == None:
            
            if parent.val < curr.val:
                parent.right = None
                print('Deleting {} ...'.format(curr.val))
            else:
                parent.left = None
                print('Deleting {} ...'.format(curr.val))

        if curr.left == None and curr.right != None:

            if parent.val < curr.val:
                parent.right = curr.right
                print('Deleting {} ...'.format(curr.val))
            else:
                parent.left = curr.right
                print('Deleting {} ...'.format(curr.val))

        if curr.right == None and curr.left != None:

            if parent.val < curr.val:
                parent.right = curr.left
                print('Deleting {} ...'.format(curr.val))
            else:
                parent.left = curr.left
                print('Deleting {} ...'.format(curr.val))
        else:

            temp = curr.right

            while temp.left != None:
                temp = temp.left
            
            self.delete(temp.val)
            
            
            temp.right, temp.left = curr.right, curr.left
            temp.parent = parent


            if parent.val < curr.val:
                parent.right = temp
                print('Deleting {} ...'.format(curr.val))
            else:
                parent.left = temp
                print('Deleting {} ...'.format(curr.val))
            
            
# TODO fix duplicate values in bst
def construct_balanced_bst(arr):
    arr = sorted(arr)
    low = 0 
    high = len(arr) // 2 - 1
    middle = (low + high) // 2

    left = high + 2
    right = len(arr) - 1
    mid = (left + right) // 2

    root = BinaryTree(arr[high + 1])

    while left <= right and low <= high:
        root.insert(arr[mid])
        root.insert(arr[middle])
        low +=1
        left += 1

        mid = (left + right) // 2
        middle = (low + high) // 2



   
    return root

class PrefixNode:
    def __init__(self, char = None):
        self.char = char
        self.children = {}
        self.isWord = False
    def insert(self,target, index = 0 ):
        if index >= len(target):
            self.isWord = True
            return
        
        if target[index] not in self.children.keys():
            self.children[target[index]] = PrefixNode(target[index])
            self.children[target[index]].insert(target, index + 1)
        else:
            self.children[target[index]].insert(target, index + 1)
    def print(self):
        for i in self.children.values():
            print(i.char)
            i.print()
    def isWord(self, target, index = 0):
        if target[index] not in self.children.keys() or index > len(arr):
            return False
        if index == len(target) - 1 and target[index] in self.children.keys():
            return True
        else:
            self.children[target[index]].isWord(target, index + 1)
        


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self,target):
        self.root.insert(target)
    def print(self):
        self.root.print()
    def isWord(self, target):
        return self.root.isWord(target)







class max_heap:
    def __init__(self):
        self.heap = [0]
    def insert(self, val):

        newIndex = len(self.heap)
        self.heap.append(val)
        parent = newIndex // 2
        curr = newIndex

        while parent >= 1 and self.heap[parent] < self.heap[curr]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[curr]
            self.heap[curr] = temp

            curr, parent = parent, parent //2
    def pop(self):
        temp = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap[-1] = temp
        res = self.heap[-1]

        print('Removing {} from the max heap...'.format(temp))
        del self.heap[-1]

        curr = 1
        leftChild = curr *2
        rightChild = curr * 2 + 1
        while (rightChild < len(self.heap) and leftChild< len(self.heap)) and (self.heap[curr] < self.heap[leftChild] or self.heap[curr] < self.heap[rightChild]):
            if self.heap[leftChild] > self.heap[rightChild]:
                temp = self.heap[curr]
                self.heap[curr] = self.heap[leftChild]
                self.heap[leftChild] = temp
                curr = leftChild
            else:
                temp = self.heap[curr]
                self.heap[curr] = self.heap[rightChild]
                self.heap[rightChild] = temp
                curr = rightChild
            leftChild = curr * 2
            rightChild = curr * 2 + 1
        return res
            
            

    def __str__(self):
        return str(self.heap)




class min_heap:
    def __init__(self):
        self.heap = [0]
    def insert(self, val):

        newIndex = len(self.heap)
        self.heap.append(val)
        parent = newIndex // 2
        curr = newIndex

        while parent >= 1 and self.heap[parent] > self.heap[curr]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[curr]
            self.heap[curr] = temp

            curr, parent = parent, parent //2
    def pop(self):
        temp = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap[-1] = temp
        res = self.heap[-1]

        print('Removing {} from the max heap...'.format(temp))
        del self.heap[-1]

        curr = 1
        leftChild = curr *2
        rightChild = curr * 2 + 1
        while (rightChild < len(self.heap) and leftChild< len(self.heap)) and (self.heap[curr] > self.heap[leftChild] or self.heap[curr] > self.heap[rightChild]):
            if self.heap[leftChild] < self.heap[rightChild]:
                temp = self.heap[curr]
                self.heap[curr] = self.heap[leftChild]
                self.heap[leftChild] = temp
                curr = leftChild
            else:
                temp = self.heap[curr]
                self.heap[curr] = self.heap[rightChild]
                self.heap[rightChild] = temp
                curr = rightChild
            leftChild = curr * 2
            rightChild = curr * 2 + 1
        return res
            
            

    def __str__(self):
        return str(self.heap)

import math

def heap_sort(arr):
    temp = min_heap()

    res = []

    for i in arr:
        temp.insert(i)

    while(len(temp.heap) > 0):
        res.append(temp.pop())

    return res

class grid_point:
    def __init__(self,x = None, y = None):
        self.x = x
        self.y = y
        self.next = None

class bin:
    def __init__(self):
        self.root = grid_point()
    def insert(self, x, y):
        curr = self.root

        while curr.next != None:
            curr = curr.next
        
        curr.next = grid_point(x, y)
import math
class grid:
    def __init__(self, x_max, y_max, num_bins):
        self.x_max, self.x_min = float(x_max), 0.0
        self.y_max, self.y_min = float(y_max), 0.0
        self.x_bin_width = (self.x_min - x_max) / num_bins
        self.y_bin_width = (self.y_min - y_max) / num_bins
        self.num_bins = num_bins
        self.grid = [[bin() for x in range(int(num_bins))] for x in range(int(num_bins))]

    def insert(self, x, y):
        x_bin = math.floor((x - self.x_min) / self.x_bin_width)
        y_bin = math.floor((y - self.y_min) / self.y_bin_width)
        
        if x_bin < 0 or x_bin > self.num_bins:
            return False
        if y_bin < 0 or y_bin > self.num_bins:
            return False
        
        self.grid[x_bin][y_bin].insert(x, y)

        return True
    def _aprox_equal(self, x1, x2, y1, y2):

        if abs(x1 - x2) > .1:
            return False
        if abs(y1 - y2) > .1:
            return False
        return True
    
    def delete(self, target_x , target_y):

        x_bin = math.floor((target_x - self.x_min) / self.x_bin_width)
        y_bin = math.floor((target_y - self.y_min) / self.y_bin_width)

        if x_bin < 0 or x_bin > self.num_bins:
            return False
        if y_bin < 0 or y_bin > self.num_bins:
            return False
        
        curr = self.grid[x_bin][y_bin]

        previous = curr


        while curr != None:
            if self._aprox_equal(target_x, curr.x,target_y, curr.y):
                previous.next = curr.next
                return True
            else:
                temp = curr
                previous = temp
                curr = temp.next
        
        return False

    def minDistToBin(self, xbin, ybin, x, y):
        if xbin < 0 or xbin > self.num_bins:
            return False
        if ybin < 0 or ybin > self.num_bins:
            return False
        
        x_min = self.x_min + xbin * self.x_bin_width
        x_max = self.x_max  + (xbin + 1) * self.x_bin_width
        if x < x_min:
            x_dist = x_min - x
        if x > x_max:
            x_dist = x - x_max

        y_min = self.y_min + ybin * self.y_bin_width
        y_max = self.y_max  + (ybin + 1) * self.y_bin_width
        if y < y_min:
            y_dist = x_min - x
        if y > y_max:
            y_dist = x - x_max

        return math.sqrt(x_dist * x_dist + y_dist*y_dist)

    def euclidean_dist(self, x1,y1,x2,y2):
        return  math.sqrt((x1 - x2)**2 + (y1 - y2 )**2)

    def GridLinearScaNN(self, x,y):
        best_dist = None
        best_candidate = None

        xbin = 0
    

        while xbin < self.num_bins:
            ybin = 0
            while ybin < self.num_bins:
                if (self.minDistToBin(xbin, ybin, x,y) < best_dist) or best_dist == None:
                    current = self.grid[xbin][ybin]
                    current = current.next

                    while current != None:
                        dist = self.euclidean_dist(x,y, current.x,current.y)

                        if dist < best_dist:
                            best_dist = dist
                            next_candidate = current
                        current = current.next
                    ybin = ybin + 1
                xbin = xbin + 1
            return best_candidate




        



        




