import random
#the names are in a db file split into names for male, female and surnames
names_fm_file = open("db-names-fm","r")
names_m_file = open("db-names-m","r")
surnames_file = open("db-surnames","r")

#open files
names_fm = names_fm_file.read().splitlines()
names_m = names_m_file.read().splitlines()
surnames = surnames_file.read().splitlines()

#input from user for male or female
if input("(M)ale or (F)emale?: ") == 'F':
	rand = random.randint(1,57)
	print (names_fm[rand],end = " ") 
else:
	rand = random.randint(1,51)
	print (names_m[rand],end = " ") 

#random surname
rand = random.randint(1,76)
print(surnames[rand])

#close files
names_fm_file.close
names_m_file.close
surnames_file.close