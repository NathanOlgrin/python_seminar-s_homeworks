#Напишите программу, которая найдёт произведение пар чисел
#списка. Парой считаем первый и последний элемент, второй
#и предпоследний и т.д.

def function(list):
    list_result=[]
    for i in range(0,len(list)):
        j=len(list)-i-1
        list_result.append(list[i]*list[j])
        if i==j or j-i==1:
            return(list_result)

list = [0,1,2,3,4,5,6,7,8,9,10]
print(function(list))