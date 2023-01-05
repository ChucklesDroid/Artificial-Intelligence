# Create a set
football = { 'Brazuca', 'Jabulani', 'Telstar', 'Al-Rihla'}
print("set created: "+str(football))


# Add elements to the set
football.add('T-Model')
print("Adding 'T-Model' to football: "+str(football))

# Remove elements from the set
football.remove('Brazuca')
print("Removing 'Brazuca' from football: " + str(football))

# Remove element from the set if element is present
if 'Jabulani' in football:
    football.remove('Jabulani')
print("Set after removing the desired element(in this case 'Jabulani'): "+str(football))

# update() function in python
football2 = {'Federale 102', 'Allen', 'Superball Duplo T', 'Top Star'}
football.update(football2)
print("update function in python"+ str(football))

# discard() function in python
football.discard('Telstar')
football.discard('Azteca')