#!/usr/bin/env python
import sys

count = 0

java = 0
python = 0
cpp = 0

for line in sys.stdin:
	
	line = line.strip()

	language , count = line.split()

	count = int(count)
	
	if language == "java":
		java += count
	
	if language == "python":
		python += count

	if language == "c++":
		cpp += count	

print("java",java)
print("python",python)
print("c++",cpp)
