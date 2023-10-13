#To restrict external access and modification of a variable outside of a class, make it a private variable by using double underscores
class Grocery:
  def __init__(self, item: str, price:float):
    self.__price = price
    self.item = item

  def get_price(self):
    print(f"The price of {self.item} is ${self.__price}")

grocery_item = Grocery("Apples", 2.99)

#Access the private varable using the getter method
grocery_item.get_price()
'The price of Apples is $2.99'

#Access the private variable directly
grocery_item.__price
#AttributeError: 'Grocery' has no attribute '__price'