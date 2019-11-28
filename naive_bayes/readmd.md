### 朴素贝叶斯(Native Bayes,NB) 
朴素贝叶斯是基于**特征是独立的**这个朴素假设，应用贝叶斯定理的监督学习算法
#### Gaussian Native Bayes

$$p(y|x_1,x_2)$$
$$p(y|x_1,x_2,\dots , x_n) = \frac{p(y)p(x_1,x_2,\dots , x_n | y)}{p(x_1,x_2, \dots , x_n)}$$

$$p(x_i|y,x_1,x_2, \dots , x_n) = p(x_i|y)$$

$$p(x_1,x_2, \dots , x_n|y) = p(x_1|y) \cdot p(x_2,x_3, \dots , x_n |y,x_1)$$