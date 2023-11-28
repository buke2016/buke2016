import numpy as np
class ReverseArray:
    def ReverseArray(self,array):
      self.array = None
      arr = [12, 34, 56, 78]
      #The original array
      arr = [12, 34, 56, 78]
      print("Original Array is :",arr)
      #reversing using reversed()
      result=list(reversed(arr))
      print("Resultant new reversed Array:",result)

    def Listslicing(self,array):
      self.array = None
      arr = [11, 22, 33, 44, 55]
      print("Array is :",arr)
      
      res = arr[::-1] #reversing using list slicing
      print("Resultant new reversed array:",res)

    def ReverseMethod(self,array):
      self.array = None
      arr = [11, 22, 33, 44, 55]
      print("Before reversal Array is :",arr)
      arr.reverse() #reversing using reverse()
      print("After reversing Array:",arr)

    def reversed(self,array):
      self.array = None
      arr = [12, 34, 56, 78]
      print("Original Array is :",arr)
      #reversing using reversed()
      result=list(reversed(arr))
      print("Resultant new reversed Array:",result)

    def flip_numpy(self,array):
      self.array = None
      #The original NumPy array
      new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
      print("Original Array is :",new_arr)
      
      #reversing using flip() Method
      res_arr=np.flip(new_arr)
      print("Resultant Reversed Array:",res_arr)

    def flipud_numpy(self,array):
      self.array = None
      new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
      print("Original Array is :",new_arr)
      
      #reversing using flipud() Method
      res_arr=np.flipud(new_arr)
      print("Resultant Reversed Array:",res_arr)    # https://www.askpython.com/python/array/reverse-an-array-in-python
    
    def slicing_numpy(self,array):
      self.array = None
      #The original NumPy array
      new_arr=np.array([1,3,5,7,9])
      print("Original Array is :",new_arr)
      
      #reversing using array slicing
      res_arr=new_arr[::-1]
      print("Resultant Reversed Array:",res_arr)

    #Python program to reverse an array
    def list_reverse(arr,size):
    
        #if only one element present, then return the array
        if(size==1):
            return arr
        
        #if only two elements present, then swap both the numbers.
        elif(size==2):
            arr[0],arr[1],=arr[1],arr[0]
            return arr
        
        #if more than two elements presents, then swap first and last numbers.
        else:
            i=0
            while(i<size//2):
    
        #swap present and preceding numbers at time and jump to second element after swap
                arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
          
        #skip if present and preceding numbers indexes are same
                if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
                    arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
                i+=2
            return arr
    
    arr=[1,2,3,4,5]
    size=5
    print('Original list: ',arr)
    print("Reversed list: ",list_reverse(arr,size))

