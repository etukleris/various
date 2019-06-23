my_list = [i ** 2 for i in range(1, 11)]
path = 'C:/Users/Edgaras/Desktop/python/InOut/output.txt'
my_file = open(path, 'r+')
#print (my_list)
# Add your code below!
for i in my_list:
  my_file.write(str(i) + "\n")
contents = my_file.readlines()
print (contents)
#my_file.readlines()
my_file.close()
