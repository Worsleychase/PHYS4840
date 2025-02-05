def sqrt(num):
    if (num < 0):
        raise Exception("Only use non-negatives")
    
    a = num
    b = (a+(num/a))/2

    while (abs(a-b) >= 0.0001):
        a = b
        b = (a+(num/a))/2

    return b

def floor(num):
    if (type(num) is not float):
        raise Exception("Must be a float")
    return num//1

def round(num, digits):
    if (type(num) is not float):
        raise Exception("Must be a float")

    factor = 10 ** digits
    shifted = num * factor
    if shifted >= 0:
        rounded = int(shifted + 0.5)
    else:
        rounded = int(shifted - 0.5)
    return rounded / factor

def min(arr, retIndex = False):
    min = arr[0]
    index = 0
    minIndex = 0
    for i in arr:
        if (i < min):
            min = i
            minIndex = index
        index += 1

    if (retIndex == False):
        return min
    else:
        return min, minIndex

def argmin(arr):
    ignoreMe, index = min(arr,True)
    return index

# Just because I have it, here's my sqrt function in assembly
'''
# Chase Worsley
# Last Edited: 4-25-2024

    .data
float0: .float 0.0 # For comparing floats to 0
errorCheck: .float 0.00001 # Error margin for correct sqrt
enterText: .asciiz "Enter a non-negative number: "
outputText: .asciiz "Square root is "
newLine: .asciiz "\n"

    .text
main:
   	# Request number
	li $v0, 4
	la $a0, enterText
	syscall

	# Read number (float)
	li $v0, 6
	syscall
	s.s $f0, 0($sp) # Save number to 0 on stack
   
    # Calculate square root
    jal fsqrt
   
    # Print square root text
    li $v0, 4
    la $a0, outputText
    syscall
   
    # Print square root number
    li $v0, 2
    l.s $f12, 4($sp)
	l.s $f31, float0
	add.s $f12, $f0, $f31 
    syscall
   
    # Print new line
    li $v0, 4
    la $a0, newLine
    syscall
   
    # Exit program
    li $v0, 10
    syscall
   
fsqrt:
	l.s $f0, 0($sp)   	 # Load input number into $f0(x) from stack
	l.s $f31, float0  	 # Load float0 into $f31
	li.s $f29, 2.0    	 # Load 2.0 into $f29 for divisor
	l.s $f28, errorCheck # Load error check into $f28 for checking error
	
	# Increase stack for output/return (Return will be saved to 4($sp))
	addi $sp, $sp, -4
	
	# Return 0 if input == 0
	c.eq.s $f0, $f31
	bc1t return0
	
	mov.s $f1, $f0	     # Load x into "xhi"
	mov.s $f2, $f31      # Load 0 into "xlo"
	div.s $f3, $f0, $f29 # Load x/2 into "guess"
	mov.s $f4, $f31      # Load 0 into "error"
	
	mul.s $f30, $f3, $f3 # Load guess^2 into $f30 temporarily
	sub.s $f4, $f30, $f0 # error = guess^2 - x
	
	# Error = -Error if less than 0
	c.lt.s $f4, $f31
	bc1t errorLTZero
	
	j while 
	
errorLTZero:
	sub.s $f4, $f31, $f4
	
	j while

while:
	# If error > 0.00001, end loop (exit function)
	c.le.s $f4, $f28
	bc1t exitFunc
	
	mul.s $f30, $f3, $f3   # Loads guess^2 into $f30 for conditional
		
	# if guess^2 < x, xlo = guess
	c.lt.s $f30, $f0
	bc1t guessSqLTx
	mov.s $f1, $f3
	
	j end_of_if
	
guessSqLTx:
	mov.s $f2, $f3

end_of_if:
	add.s $f30, $f1, $f2   # Load "xhi + xlo" into temp float register
	div.s $f3, $f30, $f29  # Load "xhi + xlo / 2" into guess
	
	mul.s $f30, $f3, $f3   # Load guess^2 into $f30 temporarily
	sub.s $f4, $f30, $f0   # Load "guess^2 - x" into error
	
	# Error = -Error if less than 0
	c.lt.s $f4, $f31
	bc1t errorLTZero2	
	
    j while 
	
errorLTZero2:
    sub.s $f4, $f31, $f4 
	j while
	
return0: 
	s.s $f31, 4($sp)
	jr $ra
		
exitFunc:
	add.s $f0, $f3, $f31 #Breakpoint
	jr $ra
'''