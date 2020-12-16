# Recursion-Memoization
Taking common recursion algorithms and memoizing it to greatly improve the efficiency

## Dynamic Programming
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).
In these examples, I used an empty dictionary to store the key-value pairs which correspond to their respective index and their solution.

## 1. Fibbonacci Sequence: fib(n)
According to wikipedia (and common sense), the Fibonacci sequence is a list of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The proceeding (or any) values of Fibbonacci sequence can be solved by adding the previous two numbers in the sequence together.
```
fib(n) = fib(n-1) - fib(n-2)
```
The time was O(2^n) and storage O(n) for brute force, and O(n) and storage O(n) after memoization.

## 2. Grid Traveler / Shortest path: gridTraveler(n, m)
Given a matrix of size nxm, and only being allowed to move either left or down at one time, how many ways can you go from top left to bottom right?
The algorithm in this case is that if you move down, you can consider the solution to be gridTraveler(n-1, m), and moving right to be gridTraveler(n, m-1). Using this idea, we can deduce that given a size nxm, the number of paths are **gridTraveler(n, m) = gridTraveler(n-1, m) + gridTraveler(n, m-1)** 
Storing the values into memo={} greatly increases the efficiency
Brute Force rec:
time: O(m^n), storage: O(m)
Memoized rec:
time: O(mxn), storage: O(m)

## to be continued i have a final soon

