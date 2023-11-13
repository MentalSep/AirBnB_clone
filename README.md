
# AirBnB_clone

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

currently implemented is the ***the console***

## The command interpreter (the console)

The main tasks of this project projects consist of:

- putting in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances

- creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

- creating all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`

- creating the first abstracted storage engine of the project: File storage.

- create all unittests to validate all our classes and storage engine.

Then comes **the console** to help us manage the objects of the project, such us:

- Creating a new object (ex: a new User or a new Place)

- Retrieving an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Updating attributes of an object

- Destroying an object

### how to use

after cloning the repository to your system and changing your working directory to the project's folder. Run `./console.py`in your terminal to open the CLI console.

Use `help` to get the list of available commands.

### Examples

In interactive mode;

```powershell

$ ./console.py

(hbnb) help

  

Documented commands (type help <topic>):

========================================

EOF all create destroy help quit show update

  

(hbnb)

(hbnb)

(hbnb) quit

$

```

in non-interactive mode:

```powershell

$ echo 'help'  | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF all create destroy help quit show update

  

(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):

========================================

EOF all create destroy help quit show update

  

(hbnb)

```

## Unittests

To run all the tests, simply run this command in the base directory:

```powershell

python3 -m unittest discover tests

```

## AUTHORS

[AUTHORS](AUTHORS)
