# LRU-cache

I am implementing a double-ended queue (deque) for fast pops and appends on either end of the data structure. I implement a dictionary for fast access during the get operation. This implementation should work in O(1) for all necessary operations. My original thought was to use a regular linked list but inserting or removing from the front would have been O(N).

testing.txt is used for testing the algorithm. A valid SET command saves the value and lets us know that it worked, a valid GET command should output GET value. The SIZE parameter sets the maximum size of the cache.

Assumptions:
Input does not have space separated keys or values in the key:value pair.
Size of those pairs is not an issue.
