### Motivation
- Cameras generate a projected image of the world
- Euclidian geometry is suboptimal to describe the central projection
- In Euclidian geometry the math can get difficult
- Projective geometry is an alertnative algebraic represetation of geometric objects and transformations
- Math becomes simpler

From Homogeneous to Euclidian Co
### 齐次坐标
### 一切源于全景图
我们主要研究一系列线性变换
 
### 运动模型
- **平移**(translation)
- **旋转**(rotation)
$$ R = \left[ \begin{matrix}
    \cos \theta & -\sin \theta \\
    \sin \theta & \cos \theta 
\end{matrix} \right] $$
这个坐标变换需要用于描述变换之前和之后的点对应关系。
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

但是现在问题是2x2 矩阵虽然可以描述缩放和旋转但是无法描述平移变换，为了表示平移变换我们引入齐次坐标(Homogeneous Coordinates)
我们平时了解空间就是欧式空间，那么齐次坐标和欧式坐标之间转换为
$$ (x,y) \Rightarrow \begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix}$$
反过来
$$  \begin{bmatrix}
    x \\
    y \\
    1
\end{bmatrix} \Rightarrow (\frac{x}{w},\frac{y}{w}) $$

### 二维图形的几何变换矩阵推导
- 平移

$(x,y)$ 找到变换后坐标
$$
\begin{aligned}
    x' = x + dx \\
    y' = y + dy
\end{aligned}
$$
- 缩放

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

