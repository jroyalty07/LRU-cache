import sys
from collections import deque

# Deque for tracking LRU item
use_deque = deque()

# dictionary for accessing key:value pairs
cache_table = {}

for i in sys.stdin:
    # Exit condition
    if i == 'EXIT':
        break
        
    if i == None:
        print "ERROR"
    else:
        temp = i.strip().split()

        # Check for valid GET or SIZE statement
        if len(temp) == 2:
            if temp[0] == 'GET':
                cmd = temp[0]
                key = temp[1]
                
                # GET statement output
                if key in cache_table:
                    print "GOT " + cache_table[key]
                else:
                    print "NOTFOUND"
                    
            # Size statement output
            if temp[0] == 'SIZE':
                size = int(temp[1])
                cmd = temp[0]
                print "SIZE OK"
                
        # Check for valid SET statement
        elif len(temp) == 3:
            if temp[0] == 'SET':
                cmd = temp[0]
                key = temp[1]
                value = temp[2]
                # If we already have the key...
                if key in cache_table:
                    # Update table and move the item to MOST recently used spot.
                    cache_table[key] = value
                    temp = use_deque.popleft()
                    use_deque.append(temp)
                    print "SET OK"
                else:
                    # Otherwise, remove LRU from table and list if cache is at capacity.
                    if len(use_deque) >= size:
                        temp = use_deque.popleft()
                        del cache_table[temp]

                    # update table and list
                    cache_table[key] = value
                    use_deque.append(key)
                    print "SET OK"
            # If the input is 3 strings and doesn't start with SET it is invalid.
            else:
                print "ERROR"
        # If the input is not 2 or 3 strings it is invalid.
        else:
            print "ERROR"
