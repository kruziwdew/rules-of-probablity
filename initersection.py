set1 = {'a','b','c','d','e','f'}
set2 = {'a','b','g','h','i','j','k'}

listset = set1.intersection(set2)
total= list(listset)

print("The common number of guests", len(total))
print("common guests are   ", total)