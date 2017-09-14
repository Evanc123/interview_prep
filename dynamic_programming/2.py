

"""
a) How many possible paths are there for the robot to go from (0, 0) to (X, Y) only
going right and down?


We can imagine this as a combinatorics problem. We know that we will have to go
rigth X number of times, and we know that the robot will have to go down Y number of times. 
So how many strings are there that contain X r's and Y d's. 

If we treat r as 1 and d as 0, then this is the same thing as asking how many ways are there to 
order {0, 1}^n with X 0's and Y 1's? 

The total number of strings of length (X + Y) is (X + Y)! 

But now we need to divide out some things, as it could be the case that the string was all X's. 

So we will divide by X! and Y!. This is the same things as (X + Y choose X)


"""

"""
b) Work backwards and cache the previous candidate with a success condition.

"""