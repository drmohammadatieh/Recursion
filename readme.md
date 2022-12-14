## Recursion

This is an exercise on recursion as part of the Secure Software Development course of the CS PgCert at the University of Essex Online. 

## Instructions

One of the classic programming problems that is often solved by recursion is the towers of Hanoi problem. A good explanation and walkthrough are provided by Cormen & Balkcom (n.d.) - the link is in the reading list. (the code they used for their visual example is provided on their website as well).

Read the explanation, study the code and then create your own version using Python (if you want to make it more interesting you can use asterisks to represent the disks). Create a version that asks for the number of disks and then executes the moves, and then finally displays the number of moves executed.

1. What is the (theoretical) maximum number of disks that your program can move without generating an error?
   
2. What limits the number of iterations? What is the implication for application and system security?


## Code output

The output after running the code for 3 disks is the following:

<img src="output.jpg" width="300">
## Answers

### Q1

The maximum integer in python 3 is 2147483647. Since 2^n -1 = Number of moves needed. Solving the equation results in 31 disks.

### Q2

The default recursion depth in python is 1000. This can be increased, but there is a risk of stack overflow error that creates security vulnerabilities.
