from faker import Faker

faker = Faker("pt_br")
for i in range(200):
    
    print(faker.name())
    print(faker.address())
    print(faker.email())