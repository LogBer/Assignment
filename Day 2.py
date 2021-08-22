inp_str = "AssignmentDay2"
out = {x : inp_str.count(x) for x in set(inp_str )} 
print ("Occurrence of all characters in This Word is :\n "+ str(out))
