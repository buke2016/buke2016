class Apollo:
    # define a variable
    destination = "moon"
    
    # defining the member functions
    def fly(self):
        print ("Spaceship flying...");
    
    def get_destination(self):
        print ("Destination is: " + self.destination);
        
# 1st object
objFirst = Apollo();
# 2nd object
objSecond = Apollo();

# lets change the destination for objFirst to mars
objFirst.destination = "mars";