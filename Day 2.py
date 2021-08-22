inp_str = "AssignmentDay3"

out = {x : inp_str.count(x) for x in set(inp_str )}  

print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(out))
