# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2

print(new_class)

new_class.append('Peter Warden')

print(new_class)

new_class.remove('Carla Gentry')

print(new_class) 




# --------------
# Code start
courses = {'course':'Marks'}
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}

total = sum((courses.values()))

print (total)

percentage = (total/500)*100

print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffery Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

max_marks_scored = max(mathematics,key = mathematics.get)

topper = max_marks_scored

print (topper)
# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


last_name = topper.split()[-1]

first_name = topper.split()[-2]
print(last_name)
print(first_name)

full_name = last_name + ' ' + first_name

print (full_name)

certificate_name = full_name.upper()

print(certificate_name)






