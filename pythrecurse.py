 #finding fibonacci using recursion
 #create function and pass in integer as parameter
 #create a default variable thatll hold the multiplied output
#loop through the range of the int uing for loop
#multiply each variable and print output
#call a recusive function,containing n-1
#end function by passing arguments
def recurse(number):
    fact=1
    
    if number==0:
           return 0
    else:
        # recurse(number-1)
        for numb in range(number+1):
            recurse(number-numb)*recurse(number-numb)
        print(fact)
            #  recurse(number-1)

        # number+=1
        # print(fact)
        # recurse(number-1)
recurse(7)