0x00. AirBnB clone - The console.

Projet description:
The AirBnB project's goal is to replicate the AirBnB website. This first part of the project - The console, is a back-end aspect of building the website. The first step to achieving this is by writing a command interpreter to manage the AirBnB objects, made  possible with the help of the cmd module in python.

The Command Interpreter:
This web application interface works like the shell but limited to a specific use case. For the purpose of this project, the use of this interface will be to:
# Create a new object (ex: a new User or a new Place)
# Retrieve an object from a file, a database etc…
# Do operations on objects (count, compute stats, etc…)
# Update attributes of an object
# Destroy an object

The interface should work in both interactive and non-interactive mode.

In interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
