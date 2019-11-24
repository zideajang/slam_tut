### Motivation
- Cameras generate a projected image of the world
- Euclidian geometry is suboptimal to describe the central projection
- In Euclidian geometry the math can get difficult
- Projective geometry is an alertnative algebraic represetation of geometric objects and transformations
- Math becomes simpler

From Homogeneous to Euclidian Co
### 齐次坐标
齐次坐标，并不是新的坐标系，将 2 维坐标变为 3 维坐标，齐次坐标是一种记法。可以把 n 维空间中不明确的概念明确出来。齐次坐标可以用来区分(x,y)是坐标还是向量，那么什么是向量呢。
- 向量是有长度和方向,在齐次坐标中添加 0 表示坐标(x,y,0)
- 坐标，在齐次坐标中添加 1 表示坐标(x,y,1)
齐次坐标用作变换的计算，首先我们需要理解我们要变换的是一个点(x,y),
### 一切源于全景图
我们主要研究一系列线性变换
 
### 运动模型
- **平移**(translation)
- **旋转**(rotation)
$$ R = \left[ \begin{matrix}
    \cos \theta & -\sin \theta \\
    \sin \theta & \cos \theta 
\end{matrix} \right] $$
这个坐标变换需要用于描述变换之前和之后的点对应关系。
- **缩放**(scale)
$$ S = \left[ \begin{matrix}
    s & 0 \\
    0 & s 
\end{matrix} \right] $$
$$ S_{inverse} = \left[ \begin{matrix}
    \frac{1}{s} & 0 \\
    0 & \frac{1}{s} 
\end{matrix} \right] $$
上面 3 种变换都是大家比较熟悉的变换，也是一种相似变换。



- **仿射变换** (affine)
其他变换都比较好理解，仿射变换可能大家比较陌生，简单举一个例子就是讲正方形通过变换为平行四边形，所以平行关系依然是保留的。
这样边之间的夹角信息就丢失了。
从而
- 透视(perspective)
透视变换会改变边之间的关系(例如原来并行边不在平行)

但是现在问题是2x2 矩阵虽然可以描述缩放和旋转但是无法描述平移变换，为了表示平移变换我们引入齐次坐标(Homogeneous Coordinates)
我们平时了解空间就是欧式空间，那么齐次坐标和欧式坐标之间转换为
$$ (x,y) \Rightarrow \begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix}$$
反过来
$$  \begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix} \Rightarrow (\frac{x}{w},\frac{y}{w}) $$

### 二维图形的几何变换矩阵推导
- 平移

$(x,y)$ 找到变换后坐标
$$
\begin{aligned}
    x' = x + dx \\
    y' = y + dy
\end{aligned}
$$
- 缩放

$$
\begin{aligned}
    x' = x s \\
    y' = y s
\end{aligned}
$$

- 旋转


单位圆$(\cos \alpha, \sin \alpha)$
$$\begin{aligned}
    x = r \cdot \cos \alpha \\
    y = r \cdot \sin \alpha 
\end{aligned}$$

$$\begin{aligned}
    x = r \cdot \cos (\alpha + \theta) \\
    y = r \cdot \sin (\alpha + \theta)
\end{aligned}$$

$$
\begin{aligned}
    x' = r(cos \alpha \cos \theta - \sin \alpha \sin \theta)\\
    x' = rcos \alpha \cos \theta - r\sin \alpha \sin \theta \\
    x' = x \cos \theta - y \sin \theta
\end{aligned}
$$

$$
\begin{aligned}
    y' = r(sin \alpha \cos \theta + \cos \alpha \sin \theta)\\
    y' = y \cos \theta + x \sin \theta 
\end{aligned}
$$

$$
\begin{aligned}
    x' = x \cos \theta - y \sin \theta \\
    y' = y \cos \theta + x \sin \theta 
\end{aligned}
$$
#### 推导平移公式

$$
\left[ x, y, 1\right] \begin{bmatrix}
    a_0 & a_1 & a_2\\
    b_0 & b_1 & b_2\\
    c_0 & c_1 & c_2  
\end{bmatrix} = \left[ x + dx, y + dy, 1\right]
$$

$$a_0x + b_0y + c_0 = x + dx$$
$$a_1x + b_1y + c_1 = y + dy$$
$$a_2x + b_2y + c_2 = 1$$

$$
\left[ x, y, 1\right] \begin{bmatrix}
    1 & 0 & 0\\
    0 & 1 & 0\\
    dx & dy & 1   
\end{bmatrix} = \left[ x + dx, y + dy, 1\right]
$$
#### 推导平移公式
$$
\left[ x, y, 1\right] \begin{bmatrix}
    a_0 & a_1 & a_2\\
    b_0 & b_1 & b_2\\
    c_0 & c_1 & c_2  
\end{bmatrix} = \left[ sx, sy, 1\right]
$$

$$a_0x + b_0y + c_0 = xs$$
$$a_1x + b_1y + c_1 = sy$$
$$a_2x + b_2y + c_2 = 1$$

$$
\left[ x, y, 1\right] \begin{bmatrix}
    s & 0 & 0\\
    0 & s & 0\\
    0 & 0 & 1   
\end{bmatrix} = \left[sx, sy, 1\right]
$$


$$
\left[ x, y, 1\right] \begin{bmatrix}
    a_0 & a_1 & a_2\\
    b_0 & b_1 & b_2\\
    c_0 & c_1 & c_2  
\end{bmatrix} = \left[ x \cos \theta - y \sin \theta, y \cos \theta + x \sin \theta, 1\right]
$$

$$a_0x + b_0y + c_0 = x \cos \theta - y \sin \theta$$
$$a_1x + b_1y + c_1 = y \cos \theta + x \sin \theta$$
$$a_2x + b_2y + c_2 = 1$$

$$
\left[ x, y, 1\right] \begin{bmatrix}
    \cos \theta & \sin \theta & 0\\
    - \sin \theta & \cos \theta & 0\\
    0 & 0 & 1   
\end{bmatrix} = \left[x \cos \theta - y \sin \theta, y \cos \theta + x \sin \theta, 1\right]
$$