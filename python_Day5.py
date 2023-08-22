#Python enables you to interact with files through file objects and a range of techniques facilitated by the integrated open() function.
# Here is a breakdown of how file reading and writing are accomplished in Python

#read a file

file1 = open('test.txt') #opening a file. by default read mode

print(file1)#show the encoding and mode of a file
print(file1.mode) #it only show the mode  of a file



print(file1.read()) #print the contain of the file
file1.seek(0) #after reading  single time python will not read the file again so it is mandetory to use seek() function to read from the beginning.
print('\n', file1.readline())#it will read a single line
print('\n', file1.readline())
file1.seek(0)
print(file1.readlines())#show content as a list format
file1.seek(0)
for file in file1:
    #print(file)#there will be a space between content
    print(file.strip()) #so we are using .strip to remove those spaces



file1.close()#best practice always close the file

#write inside a file

file2 = open('month.txt', 'w')#changed the file mode from read to write and also create a file if the file is not there
print(file2)
file2.write('jan') #next input overwrite the previous content



file2.close()

#mode 'w' will write inside a file but to append the next input we have to use 'a'

file3 = open('list.txt', 'a')
file3.write('\nbanana')
file3.write('\napple')
file3.close()