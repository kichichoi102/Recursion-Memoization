# Recursion-Memoization
Taking common recursion algorithms and memoizing it to greatly improve the efficiency

## Dynamic Programming
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).
In these examples, I used an empty dictionary to store the key-value pairs which correspond to their respective index and their solution.

## 1. Fibbonacci Sequence: fib(n)
According to wikipedia (and common sense), the Fibonacci sequence is a list of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The proceeding (or any) values of Fibbonacci sequence can be solved by finding the sum of the previous two numbers in the sequence.
```
fib(n) = fib(n-1) - fib(n-2)
```
The time was O(2^n) and storage O(n) for brute force, and O(n) and storage O(n) after memoization.

## 2. Grid Traveler / Shortest path: gridTraveler(m,n)
Given a matrix of size nxm, and only being allowed to move either left or down at one time, how many ways can you go from top left to bottom right?
The algorithm in this case is that if you move down, you can consider the solution to be gridTraveler(n-1, m), and moving right to be gridTraveler(n, m-1). Using this idea, we can deduce that given a size nxm, the number of paths are **gridTraveler(n, m) = gridTraveler(n-1, m) + gridTraveler(n, m-1)** 
Storing the values into memo={} greatly increases the efficiency
Brute Force rec:
time: O(m^n), storage: O(m)
Memoized rec:
time: O(mxn), storage: O(m)

## 3. Target Calculator: canSum(target, numbers)
Given an array of potential numbers and a target number, is there a way to add up to the target number using a sum of the given numbers? For example, if we want to find if we can add up to 17, given an array of [10, 5, 2], the answer would be True (10+5+2 = 17). To make a dynamic program to solve this, we need a recursive algorithm, and a memoized version to greatly reduce processing time.
