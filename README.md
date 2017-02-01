# LRU-cache

I am implementing a double-ended queue (deque) for fast pops and appends on either end of the data structure. I implement a dictionary for fast access during the get operation.This implementation should work in O(1) for all necessary operations. My original thought was to use a regular linked list but inserting or removing from the front would have been O(N).

Assumptions:
Input does not have space separated keys or values in the key:value pair.
Size of those pairs is not an issue.
