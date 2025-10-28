#Task 1

num1 = 2 * (3-1)

print(num1)


num2 = (5-1) * (5+1)

print(num2)

num3 = 0.3 * (4-1)

print(num3)

num4 = (91 - 1) / (2 + 1)

print(num4)

import math as mt

num5 = mt.sqrt(5 * 4) / 3

print(num5)


num6 = (1 / 3) + 5 * (0.2 - 0.001) / 91

print(num6)

num7 = (40-(4.25 * 7.08 + (6.768 / 0.75))) * 2050

print(num7)

num7 = (0.16 * (3.2 - 3/40) + 2 * (3/11) * 4.125 / (3 * (3/4))) / (5 * (1/6) * 0.3 - 0.3 * 4.5 + (1/3) * 0.3)

print(num7)

# Task 2 

x = 24

y = 31.4

print(type(x))

print(type(y))

# Task 3 

a = 20

b = 10

diff = abs(a - b)

print(diff)

#Task 4 

potatos = 290

bag_potatos = 25

full_bags = 290 // 25

other_potatos = 290 % 25

print (full_bags)
print(other_potatos)

#Task 5

h_1 = 13
m_1 = 25

h_2 = 19
m_2 = 40

h = h_2 - h_1  
m = m_2 - m_1  

print(f"Василий работал {h} часов и {m} минут")

# Task 6


old_price = int(input('Write old price: '))
new_price = int(input('Write new price: '))

percentage_change = ((new_price - old_price) / old_price) * 100

res = round(percentage_change, 1)

print(res)


#Task 7 
x= 2
y = mt.exp(1 / (1 + x**2))

print(y)


#Task 8 


total_details = 1500  

details_per_worker = 45

res = mt.ceil(total_details / details_per_worker)

print(res)



#Task 9

katet_1 = int(input('Введите длину катета: '))
katet_2 = int(input('Введите длину катета: '))
gip = int(input('Введите длину гипотенузы: '))


min_katet = min(katet_1, katet_2)


sin_angle = min_katet / gip

print(sin_angle)

#Task 10

katet_1 = int(input('Введите длину катета: '))
katet_2 = int(input('Введите длину катета: '))
gip = int(input('Введите длину гипотенузы: '))


min_katet = min(katet_1, katet_2)


sin_angle = min_katet / gip


angle_rad = mt.asin(sin_angle)


angle_deg = (angle_rad * 180) / mt.pi

print(angle_deg)