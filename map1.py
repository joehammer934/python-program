#!/usr/bin/env python
import sys 
# Read records from stdin 
for line in sys.stdin:    # Split them on commas    
	fields = line.strip().split(' ')
    # Output the state followed by the full name    
	print "%s\t%s %s" % (fields[0], fields[1],fields[3]) 