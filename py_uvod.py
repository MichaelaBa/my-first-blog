girls = ["Miska", "Lenka", "Julia", "Nana"]

def hi(name):
	print("Hello " + name + " ;-)")

for name in girls:
	hi(name)
	print("-"*len(name))

for i in range(0,3): 
	print ("{}.".format(i))
