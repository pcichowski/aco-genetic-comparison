<h1 align="center">
  Comparison of Ant Colony Optimization algorithm and Genetic algorithm for the traveling salesman problem
</h1>

<h4 align="center">
  Measuring the performance and calculating the optimal parameters of ACO and Genetic in approximating the solution to TSP
  <br><br><br>
</h4>



## Description of the problem
The Travelling salesman problem asks, "For a given list of cities and the distance between each, what is the shortest possible path to visit all cities exactly once and return to the initial city?".

In short, the task is to find the minimal Hamiltonian cycle in a complete weighted graph.

The problem is NP-hard - this is due to the large number of combinations to check. For *n* cities the number of cycles to check is *(n + 1)! / 2*

In our project we compare two approximation algorithms - Ant Colony Optimization and Genetic.
<br><br>

## Results

Testing of the algorithms consisted of checking the execution time and the path length returned for different graph sizes.

The tests were carried out for three complete graphs:
- 25 vertices
  
  |  | ACO | Genetic |
  | --- | --- | --- |
  | Average execution time | 8,32 s | 5,37 s |
  | Average distance | 4296 | 4399 |
  | Standard deviation of time | 0,66 s | 1,46 s |
  | Standard deviation of distance | 371,67 | 374,13 |
    
   ![image](https://user-images.githubusercontent.com/81694867/170877993-74679bf9-b611-4a21-8aa5-28b11f47da5a.png)
- 50 vertices   
  
  |  | ACO | Genetic |
  | --- | --- | --- |
  | Average execution time | 93,98 s | 25,01 s |
  | Average distance | 6222 | 11326 |
  | Standard deviation of time | 15,02 s | 5,6 s |
  | Standard deviation of distance | 308,07 | 908,55 |

  ![image](https://user-images.githubusercontent.com/81694867/170878060-1044a449-1975-45fc-8d7d-a79278fb1018.png)
- 75 vertices

  |  | ACO | Genetic |
  | --- | --- | --- |
  | Average execution time | 78,04 s | 7,92 s |
  | Average distance | 7526 | 20557 |
  | Standard deviation of time | 2,18 s | 0,21 s |
  | Standard deviation of distance | 336,86 | 1076,92 |

  ![image](https://user-images.githubusercontent.com/81694867/170878087-6098b6ff-2618-440f-a631-bab2480daff0.png)
  
<br>

## Implementation

We generated a complete graph representing a certain set of points by randomly generating coordinates from a fixed interval. Based on the distances between these points we determined the weights of the edges being incident to them.

We determined the optimal parameters of the algorithms by checking all permutations in the selected ranges on a full graph with 25 vertices. The heuristic function, value of which we minimised took distance into the account more than the total time of execution.
<br><br>

## Conclusion

Based on the results above we can conclude that for graphs with less vertices the performance of both algorithm is quite similar.

While increasing the number of nodes however, we can see the advantage of the ACO algorithm when it comes to the calculated distance.
Nonetheless, Genetic is much faster in every case.

If we were to decide which algorithm to choose, it would depend mainly on the size of the graph being tested. For relatively small graphs the genetic algorithm would be better, as the results are similar, but it is faster than the ant colony algorithm. As the number of vertices increases, the obvious choice is ACO, which achieves a much better performance (for a complete graph with 75 vertices it achieves an almost 3-fold advantage). 

Translated with www.DeepL.com/Translator (free version)

## Credits
#### Created by
 - [Michał Ziemiec](https://github.com/Mixss)
 - [Kacper Cencelewski](https://github.com/kapselccc)
 - [Paweł Cichowski](https://github.com/Silentsky0)

#### License
This project is a free and open-source software licensed under the [**MIT license**](https://opensource.org/licenses/MIT)
