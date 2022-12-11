print("Hello World!")

# Простой цикл while
i = 1
while i<=3:
    print(i)
    i= i+1
print("")

# Печать в одну строку
i=1
while i<=10:
      print(i, end=' ')
      i += 1  
print("")
print("")

# Печать только четных
i = 1
while i<=10:
    if i%2 == 0:
      print(i, end=' ')
    i += 1 

print("")
print("")

# Простой цикл for
for color in 'Красный','Зеленый','Синий','Желтый':
    print(color, end=' ')

print("")
print("")

# Цикл for с разными типами элементов
for i in 1,2,3,'один','два','три':
    print(i, end=' ')    
    
print("")
print("")
# Цикл for по интервалу
for i in range(10): # 0,1,2,3...8,9
    print(i, end=' ') 
print("")
print("")

# Печать списка
numbers = [2, 3, 15, 7, 11,16]
for number in numbers:
    print(number, end=' ')
print("")
print("")
# Печать только четных чисел с использованием continue
for i in range(10): # 0,1,2,3...8,9
    if i%2 !=0:
        continue
    print(i, end=' ') 
print("")

# Поиск в списке первого элемента, большего 20, с использованием break
numbers = [2,3,15,7,11,21,7,11,16]
for number in numbers:
    if number >20:
        print(number)
        break
        
print("")
# Поиск в списке первого элемента, большего 20, с использованием break
# Печатаем, что элемнт не найден, при помощи else
numbers = [2,3,15,7,11,12,7,11,16]
for number in numbers:
    if number >20:
        print(number)
        break
else:
    print("Элемент не найден")

print("")
# Печать в одну строку от 10 до 20 
i=10
while i<=20:
      print(i, end=' ')
      i += 1 
print("")

# Печать только делящихся на 3 чисел с использованием continue
for i in range(20): # 10,11,12,13...18,19
    if i%3 !=0:
        continue
    print(i, end=' ') 
print("")
# Поиск в списке первого элемента, меньшего 1, с использованием break
# Печатаем, что элемнт не найден, при помощи else
numbers = [2,3,15,7,11,12,7,11,16]
for number in numbers:
    if number <1:
        print(number)
        break
else:
    print("Элемент не найден")
