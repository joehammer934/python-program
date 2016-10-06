#!/usr/bin/env python

import sys 

# Track the last key seen 

last = None 

# Read records from stdin 

for line in sys.stdin:    

# Split the records on tabs

    	fields = line.strip().split('\t')    

# If this is a new key...

	if last != fields[0]:

        # If there was a previous key...        

		if last != None:            

          		print "%s,%s" % (last, len(users))        

		last = fields[0]       

		users = list()    

# Add this name to the cache 

	users.append(fields[1]) 

if last != None:

	print "%s,%s" % (last, len(users))

