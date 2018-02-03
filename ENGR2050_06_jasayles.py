# ENGR2050_06_jasayles.py
# Ethan Sayles
# Mar 9, 2017
import numpy as np

def calcpi(tolerance=1e-12):                                     #Default tolerance is set to 12 decimal places
    def func(n):                                                            #Calculates the nth multiple in Viete's formula for 2/pi
        if n == 0:
            return np.sqrt(.5)
        return (np.sqrt(.5 +.5*func(n-1)))                     #Alternate form of Viete's formula that is easier to iterate.
    answer = 2/np.pi
    estimate = 1
    n = 0
    while (abs(answer - estimate) > tolerance):         #Keep looping until the error is less than the tolerance
        estimate *= func(n)
        n += 1
    return(2/estimate)                                                 #return 2/estimate since that should be pi accurate to 12 decimal places

def nroot(n, N, xo,  tolerance = 1e-12):                   #Find the nth root of N with an initial guess of xo and a default tolerance of 12 decimal places
    answer = N ** (1/n)
    estimate = xo 
    while (abs(answer - estimate) > tolerance):         #Loop until the error is less than the tolerance
        estimate = (1/n)*((n-1)*estimate + N / (estimate ** (n-1)))
    return (estimate)                                                    #return the nth root
    
#Conditional to check for test cases
if __name__ == '__main__':
    print  ("Pi is approximately: ", "%0.12f" %(calcpi()))                                #print the value of the estimate for pi to 12 decimal places
    print ("The 5th root of 6436343 is approximately: ", "%0.12f" %(nroot(5, 6436343, 19)))         #print the 5th root of 6436343 (which should be 23) with an initial guess of 19
    print ("The 7th root of 658200 is approximately: ", "%0.12f" %(nroot(7, 658200, 9)))         #print the 7th root of 658200 with an initial guess of 9


        
    

    
