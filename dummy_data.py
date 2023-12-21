import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup() #These above three lines are important to make this files belongs to django 


from faker import Faker
import random
from products.models import Product , Brand , Review



def seed_brand(n):
    fake = Faker() #object from class Faker

    images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']

    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brand/{images[random.randint(0,9)]}"
            )
    print(f"{n} Brands was added succssefully")    

def seed_products(n):
     
     fake = Faker() #object from class Faker
     flag_type = ['New','sale','Feature']
     brands=Brand.objects.all()
     images = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']

     for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image =f"products/{images[random.randint(0,9)]}",
            flag = flag_type[random.randint(0,2)],
            price = round(random.uniform(20.99,99.99),2),
            sku = random.randint(100,1000000),
            subtitle = fake.text(max_nb_chars=450),
            description = fake.text(max_nb_chars= 4000),
            brand = brands[random.randint(0,len(brands)-1)],
        )
     print(f"{n} Products was added succssefully")   



def seed_reviews(n):
    pass 


#seed_brand(200)
seed_products(1500)