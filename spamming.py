import pyautigui as pg

words = []

for _ in range(int(input("Enter the number of phases/word you wanna spam"))) :
	print("Enter the phases/words : ")
	words.append(input())

num = int(input("Enter how many time you wanna spam those words/ phases :"))

pg.alert("Take the cursor to the point you wanna spam !")

pg.click(pg.position())
for _ in range(num) :
	for item in words :
		pg.write(item)
		pg.press("enter")

	

