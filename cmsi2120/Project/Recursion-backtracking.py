def factorial(n):
        #test for a base case
        if n==0:
            return 1
            # make a calculation and a recursive call
            f= n*factorial(n-1)
        print(f)
        return(f)
        factorial(4)