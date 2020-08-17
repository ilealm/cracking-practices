[Table of Contents](../../README.md)

# Rotate Matix - 1.7: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees.

# Problem 1.7: Rotate Matix

[Whiteboard approach](https://docs.google.com/document/d/10vzgltoSKS4sVhVFzypuv-ZAD-NDxEEuDL6KL4t2L-I/edit?usp=sharing)

### PROBLEM DOMAIN
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes. Write a method to rotate the image by 90 degrees.

### INPUT,

```
INPUT 			OUTPUT
[				[
  0 1 2			  0 1 2
0[1,2,3],			0[7,4,1],
1[4,5,6],			1[8,5,2],
2[7,8,9]			2[9,6,3]
]				]

element  	row, col   	moves to 	rowTo	colTo
1		0	0			0	2
2		0	1			1	2	n 	row is same value as col
3		0	2			2	2		and col is n-row
4		1	0			0	1
5		1	1			1	1	n-1
6		1	2			2	1
7		2	0			0	0
8		2	1			1	0	n-n
9		2	2			2	0

```


### EDGE CASES
- The matrix will be n*n
- Can have more than 4 bites of info.
- The matrix can be any length.
- Matrix can be empty.


### ALGORITHMS

#### APPROACH 1, Brute approach, Create a new matrix and traverse using 2 loops.
- Have 2 inner loops, one will be row(i) and the other col(j)
I will insert in the new matrix(in row, the value of col, in col n- row)


```
create a function that receives a n*n matrix
	add basic validation
	create a n*n empty matix with the same length of input matrix (return_Matrix)-1
	create a n variable with the length of the matrix
	create a outer loop to traverse the rows of the matrix (row)
		create a inner loop to traverse the columns of the matrix (col)
			set return_matrix(col,n-row) equals to matrix(row,col)

	return return_matrix


```


#### TESTS
```
row:0,1
col:0,1,2,0,1,2
n: 2

[				[
  0 1 2			  0 1 2
0[1,2,3],			0[,4,1],
1[4,5,6],			1[,5,2],
2[7,8,9]			2[,,3]
]				]
```


#### BIG O
**Time O(n^2):** Because I have 2 inner loops

**Space O(n):** I'm Because I'm creating a new ds.

### CODE

[cracking_practices/rotate_matix_90/rotate_matix_90.py](rotate_matix_90.py)

### GITHUB BRANCH

[Pull Request # n, Branch: rotate_matix_90](https://github.com/ilealm/cracking-practices/pull/X)
