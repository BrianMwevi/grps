import random as rand
m_names = input("Enter file name and omit '.txt': ").lower()
per_grp = int(input("\nEnter people per group: "))
members = open(m_names + ".txt", "r").readlines() # Open the inserted file
all_plys = len(members)
counter = 0 # Counts and increment number of groups
results = {}
rand.shuffle(members)

for i in range(0,all_plys,per_grp): # Steps with the number of people/group
	counter += 1
	team = members[i:i+per_grp]
	results["Group " + str(counter)] = team
for grp in range(len(results)):
	print("{} {}:".format("Group",grp + 1))
	vals = results["Group " + str(grp+1)]
	for v in vals:
		print("\t",v, end="")
