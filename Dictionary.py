#1.initialize dictionary(without using dictionary function)
my_dict={}
print(my_dict)
##2.initialize elements(using dictionary function)
my_dict1=dict()
print(my_dict1)

##3.print new from dict13
dict13 = {1:'python' , 2:'java',3:'new',4:'last',5:'end'}
print(dict13[3])

##4.change 'last' to 'hello'
dict13[4]= 'helo'
print(dict13)

##5.add a new pair where, key=10 and value = 'lecture'
dict13['10']='lecture'
print(dict13)

##6.pop last pair
dict13.pop('10')
print(dict13)

##7.delete second pair
dict13.pop(2)
print(dict13)

##8.print keys from dictionary
a=dict13.keys()
print(a)

##9.print values from dictionary
b=dict13.values()
print(b)

##10.clear dict
c=dict13.clear()
print(c)

##11.creat dictionary by using 1,2,3,4 as keys and 'is integer' as value
j=1,2,3,4
k='is integer'
new_dict=dict.fromkeys(j,k)
print(new_dict)

