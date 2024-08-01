#1.creat an empty set
newset= set()
print (type(newset))
print(newset)

#2.create a set with multiple values,repetitions and all possible data type, print the set
newset={2,3,4,5,4,4,49.5,2j,'data',(6,8,9)}
print(newset)

#3.add 100 in the set
newset.add(100)
print(newset)

#4.add 23,'little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'},set1
set1 = {1,2,3,4,7,9}
set1.update('23','little',[11,'done',33],('a','b',10),{'d','f'},{71:'one',72:'two'})
print(set1)

#5. delete tuple from set
set1.discard(('a','b','10'))
print(set1)

#6.delete random element from set
set1.pop()
print(set1)

#7.print all elements of these sets
set1 = {1,2,3,4,7,9}
set2 = {1,4,5,6,11,3}
print(set1|set2)
#8.print the common elements of these sets
print(set1&set2)
#9.print the uncommon elements of both set1 and set2
print(set1^set2)
#10.print difference of set2 and set1
print(set1-set2)



#11.check if s1 and s2 are same
s1 = {1,3,4,11}
s2 = {3,2,4,5,6}
s3 = {2,3,4,5,6,8,9,1,10,11,12,20}
s1==s2
print(s1==s2) 


#12.check if s1 is subset of s3
s1<=s3
print(s1<=s3)

#13.check if s2 is proper set of s3
s2<s3
print(s2<s3)