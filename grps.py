import random as rand
import string as alf
m_names = input("Enter file name and omit '.txt': ").lower()
per_grp = int(input("\nEnter people per group: "))
members = open(m_names + ".txt", "r").readlines() # Open the inserted file
all_plys = len(members)
grp_count = 0 # Counts and increment number of groups
rand.shuffle(members)

for i in range(0,all_plys,per_grp): # Steps with the number of people/group
	grp_count += 1
	team = members[i:i+per_grp]
	print("Group {}:".format(alf.ascii_uppercase[grp_count-1]))
	for i in range(len(team)):
		print ("\t {}. {}".format(i+1,team[i]))
