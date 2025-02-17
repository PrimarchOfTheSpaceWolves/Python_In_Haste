# To use packages, you import as "modules".
import cv2
# Then you can use stuff in them by referring to like module.function: cv2.imshow("MY WINDOW", image)

# You can also import with a shorter name.
import numpy as np
# Now you can use "np" instead of "numpy".

# Python uses identation to determine blocks of code.
# You CAN write code at level-0 indentation:
print("Hello from VanillaPython...")
# ...BUT that means if someone imports YOUR code as a module,
# it will run all that code directly (which you may not want).
# Instead, you would make a function for your main() function,
# and later you use a specific check to see whether someone is
# importing this file, OR they are running it directly.
def main():
    ###########################################################################
    # Variables
    ###########################################################################
    
    # Python guesses the type of something based on the right-hand side:
    x = 5       # int (integer)
    y = 3.4     # float (decimal number)
    s = "Hi"    # str (character string)
        
    # Unlike languages like C/C++/Java, you can CHANGE the type of something.
    x = "Hello"     # x is now a str
    
    # You can convert between types
    z = int(y)                      # z equals 3 after this
    t = "The number is " + str(x)   # t equals "The number is 5"
    
    ###########################################################################
    # Printing
    ###########################################################################
    
    # You can print values
    print(x)
    print(y)
    print(z)
    
    # You can also print multiple values (each item is separated by a space)
    print("The numbers are", y, "and", z)
    
    # HOWEVER, if you try to do string concatenation (stapling strings
    # together), you have to convert it to a string:
    print("The best number ever is " + str(y))    
    
    ###########################################################################
    # If Statements
    ###########################################################################
    
    # You can do boolean (True or False) checks:
    x = 5
    if x > 3:
        print("x greater than 3")
        
    # You can also do if-else
    if x > 7:
        print("x greater than 7")
    else:
        print("x is NOT greater than 7")
        
    # ...or if-elif-elif...-else
    if x > 7:
        print("x greater than 7")
    elif x > 6:
        print("x greater than 6")
    elif x > 5:
        print("x greater than 5")
    else:
        print("x is 5 or less")
        
    # You can do complex logical statements involving and, or, not
    
    # AND - BOTH must be true
    if x > 3 and s != "Hi":
        # NOT True, because s == "Hi"
        print("IMPOSSIBLE")
    else:
        print("AND check does not pass")
        
    # OR - either or both must be true
    if x < 1 or s == "Hi":
        # IS True, because s does equal "Hi"
        print("OR check passed")
        
    # NOT - flip value
    if not x < 2:
        # x < 2 --> False
        # not x < 2 --> True
        print("NOT check passed")      
        
    
    
    
    
# The special check I was talking about:
if __name__ == "__main__":
    main()
    