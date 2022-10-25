[Table of Contents](../../README.md)

# Problem

<!-- [Whiteboard approach](x_x) -->

### PROBLEM DOMAIN
From a given string, return the first non repetated character.

### VISUALS

```
A green apple   => 'g'
aa13d0s211      =>3
aa1 3d0s211     => ' '
bbbbBBBbbB      => 'b'
''              => None
```

### EDGE CASES

- String can be any length and with any character.
- String can be empty.
- String can contain white space.

### ALGORITHMS

#### APPROACH 1,

```
Create a class with a method 'return_first_non_repeted'
    this method will fill a hash table (using Dict in python) to create a key for each ch.
        before adding the character to the dict, it will be lowercase.
        if the ch exist in the Dict, the value will increase by one.
        other wise, its value will be 1

        this method will call get "find_first_non_repeted" which will traverse each character
        of the string and find if its value == 1.
            when founded, return ch

            if not founded, and the len(string)>1, return string[0]

            return None

```

#### TESTS

```
Please review the test section below.
```

#### BIG O

**Time O(n):** I need to traverse all the string to create the dict, and then traverse all the string to get the first non repetitive.

**Space O(n):** I'm creating a dict.

### CODE

[cracking_practices/x_x/x_x.py](x_x.py)

### TESTS

[tests/test_hash_table_find_1st_non_repited_ch.py](../../tests/test_hash_table_find_1st_non_repited_ch.py)

### GITHUB BRANCH

[Pull Request # 103, Branch: hash_table_find_1st_non_repited_ch](https://github.com/ilealm/cracking-practices/pull/103)
