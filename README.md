
# Superpermutations
This repository contains code for searching for shortest superpermutations by builing a weighted complete graph with the permutations as vertices, where the weights represents how many symbols must be concatenated to and removed from one permutation to obtain the other (see 
[this section](#constructing-the-graph)). Then we try to find the minimum weight path that visits each vertex (at least once).

## Superpermutations
A superpermutation on *n* symbols is a string that contains each permutation of *n* symbols as a substring.   
For example 123121321 is a superpermutation of the symbols 1, 2 and 3. Since all permutations of 
1, 2 and 3  are contained in 123121321:

**123**121321  
12312**132**1  
1231**213**21  
1**231**21321  
12**312**1321  
123121**321**  

### Shortest superpermutations

The shortest superpermutation is the shortest string that containg all permutations of the *n* symbols. The example above is the shortest superpermutation of 3 symbols.  

It has been shown that the shortest superpermutations for 1 < *n* &#8804; 5 have lengths 1, 3, 9, 33 and 153 [1]. For *n* &#8804; 4 the superpermutations are unique, but for *n* = 5 there are eight superpermutations, all of length 153 [1].  

The shortest superpermutations for n &#8805; 6 symbols are still unknown. But lower and upper bounds of the lengths has been found [2].

There is a simple algorithm for producing the optimal superpermutations for *n* &#8804; 5 symbols [1]. For 
greater *n* there is no know algorithm that yeilds optimal superpermutations. Usign various methods some small superpermutations has been found for *n* = 6, 7, 8. The
best know so far are. 

| Num. symbols  | Shortest (so far) | Optimal | Source |
| ------------- |:------------------|:--------|:-------|
| 1             | 1                 | Yes     | [1]    |
| 2             | 3                 | Yes     | [1]    |
| 3             | 9                 | Yes     | [1]    |
| 4             | 33                | Yes     | [1]    |
| 5             | 153               | Yes     | [1]    |
| 6             | 872               | Unknown | [3]    |
| 7             | 5906              | Unknown | [4]    |
| 8             | 46205             | Unknown | [5]    |


### Searching for shortest superpermutations
The shortest superpermutations so far for *n* &#8805; 6 has been found by translating the problem into an instances of the traveling salesman problem. 

#### Constructing the graph
First, construct a graph where the permutations of the *n* symbols are the vertices. Then add wighted directed edges between each vertex.  

The weight associated to an edge between permutations *s* and *t* is the smallest number of symbols 0 &#8804; *k* &#8804; *n* such that the *(n − k)*-suffix of *s* is equal
to the *(n − k)*-prefix of *t* [1]. 

For example, if *n* = 5 the weight of the edge between permutations *s =* 12345 and *t=* 45321 is *k = 3*. Since the *(5 - 3)*-suffix of 123**45** is equal to the *(5 - 3)*-prefix of **45**321, and this is the smallest *k* for which this is true.

Note that the weight between two permutations *s* and *t* may not be the same as the weight between *t* and *s*. This is why the graph should be directed.

The code for calculating the distances can be found in `src/metrics.py`, and the code for generating a matrix containing the weights between every pair of vertices can be found in `src/generate_matrix.py`.

#### Finding a superpermutation
Next we want to find the shortest path (lowest total weight) in the graph that visits all vertices at least once. This is equivalent to the assymetric traveling salesman problem, since the weights may not be the same in both directions between vertices.

It is intractable to find the optimal solution to this problem even for small *n* since the number of vertices are *n!*. Still, for small graphs heursitic algorithms can be used to find an approximate solution.

We use the algorithms found in the Google OR-Tools suite, which includes different search strategies, to find an approximate solution. 

## Usage
To generate the weight matrix for *n = 4* symbols, run 
```
python src/generate_matrix.py 4 data/weight_matrix.npz
```
To search for superpermutation candidates, run
```
python src/find_superpermutation.py data/weight_matrix.npz 11
```
The result will be printed out
```
Superpermutation:
243124321432413242314234123421342

Superpermutation length:
33
```

## Built with
* [Numpy](http://www.numpy.org/): Matrices and arrays.
* [Google OR-Tools](https://developers.google.com/optimization/): Routing optimization.

## To do
- [ ] Allow for weights to be calculated at runtime.  
- [ ] Improve command line interface, add named parameters.  
- [ ] Allow for selecting search strategy from command line.  

## Authors

* **Fredrik Fagerholm** - [ffagerholm](https://github.com/ffagerholm)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## References

[1] Houston, Robin ("2014"). "Tackling the Minimal Superpermutation Problem". arXiv e-prints, , arXiv:1408.5108.  
[2] Johnston, Nathaniel ("2013"). "Non-Uniqueness of Minimal Superpermutations". arXiv e-prints, , arXiv:1303.4150.  
[3] https://github.com/superpermutators/superperm/tree/master/PermutationChains  
[4] https://groups.google.com/forum/#!topic/superpermutators/Ya-H_wwt_HY  
[5] https://github.com/superpermutators/superperm  