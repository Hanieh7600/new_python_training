arry=['mobile','apple','book','and']
arry.sort(reverse=True)
print(arry)


#set
set1 = {7,12 , 0}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Keep All, But NOT the Duplicates
x.symmetric_difference_update(y)

print(x)

#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

