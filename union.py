set1 = {'a','b','c','d','e','f'}
set2 = {'a','b','g','h','i','j','k'}

listset = set1.union(set2)
total= list(listset)

print("The total number of guests", len(total))
print("Total guests are   ", total)