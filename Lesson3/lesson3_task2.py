from smartphone import Smartphone

catalog = []

phone1 = Smartphone ('Samsung', 's3', '+7913312131213')
phone2 = Smartphone ('Apple', 'IPhone 11', '+798989898989')
phone3 = Smartphone ('Xiomi', 'Mi 11', '+7987878787878')
phone4 = Smartphone ('Redmi', 'Max Pro Ultra 10000', '+797676767676')
phone5 = Smartphone ('Google', 'Pixel 5', '+79656565656565')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.number}')