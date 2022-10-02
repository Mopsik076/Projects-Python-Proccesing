with open("File.txt",'r') as f:
    text = f.read().splitlines()
print(text)

a = input('Выберите действие: ')
if a == 'добавить':
    b = input('Выбери название продукта: ')
    with open("File.txt",'a') as f:
        f.write('\n' + b)
        
if a == 'удалить':
    with open("File.txt",'r') as f:
        text = f.read().splitlines()
    print(text)
    text.pop(text.index(input('Выберите продукт: ')))
print(text)              
# with open("File.txt",'r') as f:
#     text = f.read().splitlines()
# print(text)




