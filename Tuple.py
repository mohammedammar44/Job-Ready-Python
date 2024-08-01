##1. initialize empty tuple
tuple1=()
print(tuple1)

#2. create a tuple of few integer values (dont use tuple function)
tuple2=(2,3,4,5,6,7)
print(tuple2)

#3. create a tuple of few string values
tuple3=('welcome','to','job','ready', 'python')
print(tuple3)

#4. print 'welcome' from list new1
new1=(1,2,3,4,'welcome')
print(new1[-1])


#5. create a tuple of few integer values using tuple function
a = ['hello',3,1.3,[1,2,5]]
newtuple=tuple(a)
print(newtuple)

#8. print all the elements from the tuple
new2 = tuple(('hello','welcome','all','here','python','end'))
print(new2[:])
#9. print last element from the tuple
print(new2[-1])
#10. print 'all' from new2
print(new2[2])
#11. print index of 'end'
print(new2.index('end'))


#12. print index of first list
tuple0 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
print(tuple0.index([10, 20, 30]))
#14. change '20' to 'start'
tuple0[2][1]= 'start'
print(tuple0)
##16. print second list from tuple0
print(tuple0[3])

#17. print tuple from tuple0
print(tuple0[-1])

#18. change 10 to 'start2'
tuple0[2][0]= 'start2'
print(tuple0)


#19. print 45.21 from tuple11(code should run for all students)
tuple11=([2,2,2,5,6,7],'welcome',(5, 15, 25),45.21,2,3,4)
print(tuple11[-4])

#20. print the number of elements in first list in tuple0
tuple0 = ("Orange",2, [10, 20, 30], ['a','b','c'],(5, 15, 25))
t1=len(tuple0)
print(t1)
#21. print the count of 'b' in second list in tuple0
t2=tuple0.count('b')
print(t2)