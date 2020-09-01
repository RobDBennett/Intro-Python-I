"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import io

f = open('foo.txt')
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", 'w', encoding= 'utf-8') as f:
    f.write("This song is just\n")
    f.write("Threeeeee liiiiinnnneeeessss long\n")
    f.write("This song is just three lines long.\n")

y = open('bar.txt')
print(y.read())
y.close()