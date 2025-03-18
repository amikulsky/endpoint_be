## Directory tree
* Sample input commands: [input.txt](input.txt)
* Expectd output file: [expected_output.txt](expected_output.txt)
* To run the program, run:
```bash
python endpoint.py < input.txt > output.txt
```

## The problem

A common method of organizing files on a computer is to store them in hierarchical directories. For instance:

 ```
photos/
  birthdays/
    joe/
    mary/
  vacations/
  weddings/
```
In this challenge, you will implement commands that allow a user to create, move and delete directories.
A successful solution will take the following input:
```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
```
and produce the following output

```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash
```

 