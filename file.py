# from faker import Faker
# from faker.providers import internet
# fake = Faker()
# f= open("guru99.txt","w+")
# for i in range(10):
# 	a = faker.ipv4_private()
# 	f.write(a % (i+1))
# f.close()

# print (faker.ipv4_private())

from faker import Faker
fake = Faker()


f= open("guru99.txt","w+")
for i in range(10):
	rand_date = fake.ipv4_private() 
	f.write(rand_date)
f.close()

print(rand_date)