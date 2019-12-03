### Kalmen Filter
卡尔曼滤波
在不确定信息，指出
连续

$$\hat{x} = \begin{bmatrix}
    p \\
    \mu
\end{bmatrix}$$

state vector with noise

协方差矩阵

$$p_k = \begin{Bmatrix}
    \sum_{pp} & \sum_{pv} \\
    \sum_{pp} & \sum_{pv} 
\end{Bmatrix}$$

$$p_k = p_{k-1} + u_{k-1}$$