import itertools as it
import random
import datetime

#count(10)
list1=[random.randint(1,10) for i in range(5)]
print list1
now=datetime.datetime.now()
print "current time:= ",(now.strftime("%Y-%m-%d %H-%M-%S"))


#print list(itertools.count(10,1))
#print list(itertools.cycle('ABC'))
print list(it.repeat(10,3))
print list(it.chain('abc','def'));
print list(it.compress('ABC',[1,0,1]))

print list(it.dropwhile(lambda x:x<9,list1))

print list(it.islice(list1,2))
print list(it.islice(list1,2,None))

print list(filter(lambda x:x%2==0,range(10)))

print list(it.imap(pow,[2,3,4],[2,2,2]))
print list(it.starmap(pow,[(2,2),(3,2),(4,2)]))
print list(it.takewhile(lambda x:x<5,list1))
print list(zip('abc','xyz'))

print list(it.product('abc',repeat=3))
print list(it.permutations('ABC',2))
print list(it.combinations('ABC',2))



