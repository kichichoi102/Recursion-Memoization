# Recursion-Memoization
Taking common recursion algorithms and memoizing it to greatly improve the efficiency

## Dynamic Programming
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map,etc).
In these examples, I used an empty dictionary to store the key-value pairs which correspond to their respective index and their solution.

## 1. Fibbonacci Sequence: fib(n)
The Fibbonacci sequence can be solved by adding the previous two numbers in the sequence together.
The time was O(2^n) and storage O(n) for brute force, and O(2n) and storage (n) after memoization.

## 2. Grid Traveler / Shortest path: gridTraveler(n, m)
Given a matrix of size nxm, and only being allowed to move left or down, how many ways can you go from top left to bottom right?


