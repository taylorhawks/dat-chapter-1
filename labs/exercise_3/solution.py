import csv

f=open('rock.csv')
rock = csv.reader(f)

row_count = sum(1 for row in rock)
print "row count:"
print row_count

#how many songs were released in 1981?

songsin81=0
if 'Release Year' == 1981:
	songsin81 += 1
print "songs in 1981:"
print songsin81

#what are the top 20 songs by playcount?
import operator
sort = sorted(rock,key=operator.itemgetter(6))
print "sorted by play count:"
for x in sort:
	print x
