#1.print welcome python1 from list11
'''
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
print(list11[0:5:4])

#2.print table of 2 and 3
list12 =(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(list12[1:21:2])
print(list12[2:21:3])
print(list12[3:21:4])
'''
#3.add 'end' after python1 in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
list11.insert(5,"end")
print(list11)

#4. reverse list 'new'
new = [10,29,1,2,3,7,9,0,4,55]
new.reverse()
print(new)

#5.only print sorted list in ascending and descending order
list1 = [10,29,1,2,3,7,9,0,4,55]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#6.changing the list to sort descending order
list1 = [10,29,1,2,3,7,9,0,4,55]
list1.sort(reverse=True)
print(list1)

#7.deleting 3 from list 'new' (use index)
new = [10,29,1,2,3,7,9,0,4,55]
new.pop(4)
print(new)

#8.delete 29 from list 'new' (use values)
new = [10,29,1,2,3,7,9,0,4,55]
new.remove(29)
print(new)

#9.pop 9 from list 'new' (print the poped value and list)
new = [10,29,1,2,3,7,9,0,4,55]
print(new.pop(-4))
print(new)

#10.copy new list
new = [10,29,1,2,3,7,9,0,4,55]
newlist= new.copy()
print(newlist)

#11. count '2' in list a
a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]
a1=a.count(2)
print(a1)

#12.clear list
a=[1,2,12,2,2,2,3,3,4,4,5,5,6,6,7,7,8,9,9,5,6,5,7,6,7,6,3,4,5]
print(a.clear())

#13.append "cup" in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
print(list11.append("cup"))

#14.extend "tea" in list11
list11 = ['welcome',1,2,3,'python1',6,5,13,'python2','python3',10.5]
print(list11.extend("tea"))
#15.add 32,41,56 in list 'new'
new = [10,29,1,2,3,7,9,0,4,55]
print(new.extend([32,41,56]))

#17.replace '29' by 'done' in list 'new'
new = [10,29,1,2,3,7,9,0,4,55]
new[1]="done"
print(new)

