from faker import Faker

faker = Faker()

with open('data.txt','w') as f:
    for _ in range(10000000):
        name = faker.name()
        age = faker.random_int(min=18,max=65)
        address = faker.address().replace('\n','')
        f.write(f"{name},{age},{address}\n")

