#Sets
cs_courses ={'History','Math','Physics','CompSci',}
art_courses ={'History','Math','Art','Design'}
print('Math'in cs_courses)# This will determine if Math is in cs_courses
print(cs_courses.intersection(art_courses))#This prints the subjects found in the two courses aka math and history
print(cs_courses.difference(art_courses))#This priints the courses in cs_courses that arent in art_courses
print(cs_courses.union(art_courses))#Ths will print out all courses offered with cs and art

#Empty Lists
empty_list =[]
empty_list = list()

#Empty Tuples
empty_tuple =()
empty_tuple = tuple()

#Empty Sets
empty_set ={} 
empty_set = set()