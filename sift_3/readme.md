SVM 和 Sift
作者 David Lowe 申请专利
### 尺度空间
#### 建立高斯差分金子塔
SIFT 算法 是在不同的尺度空间上查找关键点，而尺度空间的获取需要使用高斯模糊来实现，Lindeberg 等人已证明高斯卷积核是实现尺度变换的唯一变换核，并且是唯一的线性核。本节先介绍高斯模糊算法。

而且高斯核是唯一可以模糊近处清晰，远处模糊的(线性)卷积核。
##### 组和层的概念
图片大小图片为一组，图片内部分层
高斯核，用不同高斯核对原图进行卷积，不同方差（尺度）得到这些图片
第二组是对第一组的进行降采样，也就是间隔地保留像素点。开始能够看出物体大致的形状，图片缩小，然再用高斯核进行处理后如此循环。

差分就是在同一组内，降临两层进行相减（这里就是普通的减法）differenc of Gaussian(DOG),那我们具体一张图片应该有多少组，一个组内应该有多少层这些
##### 组和层数的计算
- 组数
$$o = \left[ \log_2(min(M,N)) \right] - 3$$
M,N 分别是原图片的大小
- 层数
$$ S = n + 3 $$
n 表示希望提取多少张图片中的特征
我们这有必要解释 n + 3 由来,如果我能够解释清楚也就是说明我也真正明白了如何计算层数，假设我们有 5 层(每一组根据不同高斯核得到相同尺寸不同模糊程度的图片)然后我们两两进行差分得到 4 张图，我们计算特征点是根据每一个点 x y z 三个维度进行计算(x,y 为图像点坐标，z 是也就是尺度空间就是垂直图片维度)因为上下层没有相邻的层所有没有 z ，因此计算只有 2 层 2 + 3 = 5 ，也就是我们因为差分先去掉 1 层，再去掉最上和最下两层就得到 2 。

#### 高斯核
$$ k = 2^{\frac{1}{n}} $$
这里 n 就是上面计算层数公式中 n 
$$ \sigma_0 = \sqrt{1.6^2 - 0.5^2}$$
我们照相机拍摄图片本身也是有模糊，所以默认拍摄模糊尺度为 0.5 ,这是一个经验值，希望第一层卷积能够得到sigma为 1.6 这样才有上面式子。高斯核特性
那么 1.52 这也就是用方差为 1.52 的卷积核对一张已经用过 0.5 方差的高斯核做过卷积处理的图进行卷积处理就会得到一张直接通过 1.6 方差高斯核做过卷积处理图片一样的效果。

- 第1组

| 层数  | $\sigma$  |
|---|---|
|  第1层  | $\sigma_0$  |
|  第2层  | $k^{n-1} \sigma$  |
|  第3层  | $k^{(n)} \sigma$  |
|  第4层  | $k^{(n+1)} \sigma$  |
|  第5层  | $k^{(n+2)} \sigma$  |
首先我们取方差为 $\sigma_0$ 作为第1组第1层的高斯核进行模糊，然后第2层我们取$k^2 \sigma$ 方差作为第1组第2层的高斯核进行模糊

- 第2组

| 层数  | $\sigma$  |
|---|---|
|  第1层  | $k^{n} \sigma$  |
|  第2层  | $k^{(n+1)} \sigma$  |
|  第3层  | $k^{(n+2)} \sigma$  |
|  第4层  | $k^{(n+3)} \sigma$  |
|  第5层  | $k^{(n+4)} \sigma$  |

在2组会去第1组倒数第3层作为第2组第1层的高斯核的方差进行模糊，为什么取层就是为得到$2\sigma$

### 关键点位置确定
关键点就是比较稳定()的点，而且包含许多信息的，这些点通常是极值位置，因为极值位置就是很稳定，不过极值可以是最大也可以是最小值。在 harris。
什么是关键点稳定性
- 尺度
- skew
- 旋转
- 位移
- 视角
- 遮挡
- 强度、色温
#### 阈值化

现在我们极值点查找是在 26 点上查找，以为包含该层上下2两层对应位置点。 
$$\begin{cases}
    abs(val) > 0.5 \times \frac{T}{n} \\
    T = 0.04
\end{cases}$$
这里 T 是经验值，而 n 就是我们上面提到要找多少张图中取特征点的值，如果这个值要小于这个 0.5 * T/n 我们就认为这个点可能是噪声。
#### 在高斯差分金字塔中找极值点
现在找到极值点并不是真正的极值点，以为我们现在空间是离散空间中最小点，所以真正的极值点可能出现当前极值点的周围。而且我们现在将一个二维坐标内像素点值扩展到三维上，也就是添加一个表示不同模糊程度和大小程度的空间上。我们在尺度空间上也是离散的，所以我们现在要找到一个真正的极值点

首先在检测到极值点$X_0(x_0,y_0,\sigma_0)^T$做三元二阶的泰勒展开。

$$ f\left( \begin{bmatrix}
    x \\
    y \\
    \sigma
\end{bmatrix} \right) = f\left( \begin{bmatrix}
    x_0 \\
    y_0 \\
    \sigma_0
\end{bmatrix} \right) + \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} , \frac{\partial f}{\partial \sigma}  \right] \left( \begin{bmatrix}
    x \\
    y \\
    \sigma
\end{bmatrix} - \begin{bmatrix}
    x_0 \\
    y_0 \\
    \sigma_0
\end{bmatrix}  \right) + $$

$$ \frac{1}{2} \left( \begin{bmatrix}
    x \\
    y \\
    \sigma
\end{bmatrix} - \begin{bmatrix}
    x_0 \\
    y_0 \\
    \sigma_0
\end{bmatrix}  \right)^T \begin{bmatrix}
     \frac{\partial f}{\partial x \partial x}, \frac{\partial f}{\partial y \partial x} , \frac{\partial f}{ \partial x \partial \sigma}  \\
     \frac{\partial f}{\partial x \partial y}, \frac{\partial f}{\partial y \partial y} , \frac{\partial f}{ \partial y \partial \sigma}  \\
     \frac{\partial f}{\partial x \partial \sigma}, \frac{\partial f}{\partial y \partial \sigma} , \frac{\partial f}{\partial \sigma \partial \sigma}  
\end{bmatrix} \left( \begin{bmatrix}
    x \\
    y \\
    \sigma
\end{bmatrix} - \begin{bmatrix}
    x_0 \\
    y_0 \\
    \sigma_0
\end{bmatrix}  \right) $$

这里有关经验一眼看出来这这里我们 X 大写来表示上面向量，二用$\hat{X}$ 表示估计，也就是我们估计真正的极值点距离测量极值点距离。
$$f(X) = f(X_0) + \frac{\partial f^T}{\partial X} \hat{X} + \frac{1}{2} \hat{X}^T \frac{\partial^2 f}{\partial X^2} \hat{X}$$

那么这里根据泰勒展开，f(x) 就是可以看做在 x0 附近的函数，那么要找到函数真正的极值点就需要对f(x) 求导，f(x)导数为 0 的地方也就是函数极值点，也就是我们想要找到真正的极值点。

$$\frac{\partial f(X)}{\partial X} = \frac{\partial f^T}{\partial X} + \frac{1}{2}\left( \frac{\partial^2 f}{\partial X^2} + \frac{\partial^2 f^T}{\partial X^2}\right) \hat{X} = \frac{\partial f^T}{\partial X} + \frac{\partial^2 f}{\partial X^2} \hat{X}$$

导数为0就得到极值点距离 
$$\hat{X} = - \frac{\partial^2 f^{-1}}{\partial X^2} \frac{\partial f}{\partial X}$$

$$\begin{alignedat}
f(x) = f(X_0) + \frac{\partial f^T}{\partial X} \hat{X} + \frac{1}{2}\left(-\frac{\partial^2 f^{-1}}{\partial X^2} \frac{\partial f}{\partial X} \right)^T \frac{\partial^2 f^{-1}}{\partial X^2}\left(-\frac{\partial^2 f^{-1}}{\partial X^2} \frac{\partial f}{\partial X} \right) \\
    = f(X_0) + \frac{1}{2} \frac{\partial f^T}{\partial X} \hat{X}
\end{alignedat}$$

迭代次数限制，当三个分量(x,y,z)都小于 0.5 时候就可以停止迭代，或者迭代次数超过一个限制时候也会停止迭代，停止迭代后我们发现这个函数值还是没有收敛，就会舍去这个点。
#### 舍去低对比度的点
$$|f(X)| < \frac{T}{n}$$
则舍去这个这个点

#### 边缘效应的去除
$$ H(x,y) = \begin{bmatrix}
    D_xx(x,y) & D_xy(x,y) \\
    D_xy(x,y) & D_yy(x,y) 
\end{bmatrix}$$

$$\begin{cases}
    Tr(H) = D_xx + D_yy = \alpha + \beta \\
    Det(H) = D_xxD_yy - (D_xy)^2 = \alpha \beta
\end{cases}$$

如何$Det(H) < 0$ 则去除 X 点
$$\frac{Tr(H)^2}{Det(H)} = \frac{(\alpha + \beta)^2}{\alpha \beta} = \frac{(\gamma \beta + \beta)}{\gamma \beta^2} = \frac{(\gamma + 1)^2}{\gamma}$$

如果不满足 
$$\frac{Tr(H)^2}{Det(H)} < \frac{(\gamma + 1)^2}{\gamma}$$
也将舍去 X