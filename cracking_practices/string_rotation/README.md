[Table of Contents](../../README.md)


# Problem: String Rotation 1.9

[Whiteboard approach](https://docs.google.com/document/d/1MpX1R90D8ZRo0Daw0r2VnlIEZpeFknlZUN1S0ZmRI2A/edit?usp=sharing)

### PROBLEM DOMAIN
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstrig.

### VISUALS
s1 = waterbottle
s2 = erbottlewat

here, I can split s1 in part x and y: waterbottle, and then rearrange them and then check them again.


### EDGE CASES
- Empty strings.
- Different lengths of s1 and s2.
- Same lengths, different letters.
- If s2 is a substring, s1 shouldn't have more letters than the ones on s2. eg:waterbottlepink is not a valid case in this exercise.



### ALGORITHMS

#### APPROACH 1
- Traverse s2 until I find the start of s1, concatenate the rest of the letters, then check is they are the same word.


```
create a function that receives two strings
	validate if they have the same length and are not empty
    set both strings to lower case
    loop thru s2
        check if s2[1] if equal to s1[0], if so,
            ckeck if s1 == s2[i:] + s2[0:i]: # concant in the right order s2
                if equal,  return True

    return False
```


#### TESTS
```
s1 = waterbottle
s2 = erbottlewat
             ^
   i  0 1 2 3 4 5 6 7 8
s2[i]:e,r,b,o,t,t,l,e,w
werbottle = wat + erbottle

```


#### BIG O
**Time O(s2):** O(s2) Because in the worst-case scenario I'm traversing all s2.
**Space O(1):** Because I'm not creating a new ds.


### CODE
[cracking_practices/string_rotation/string_rotation.py](string_rotation.py)


### TESTS
[tests/test_string_rotation.py](../../tests/test_string_rotation.py)

### GITHUB BRANCH

[Pull Request # 14, Branch: string_rotation](https://github.com/ilealm/cracking-practices/pull/14)
