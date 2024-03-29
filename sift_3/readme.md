#### 图像局部特征
- 全局特征，容易受到
#### 局部特征检测
- (斑点)blob 稳定性好
    - LOG
    - DOH Hessian 矩阵
- 角点(corner) 物体边缘拐角，两条直线 
    - SIFT
    - SURF
#### 特征描述
梯度统计直方图或二进制字符串特征描述
- BRIEF
- 
SVM 和 Sift
作者 David Lowe 申请专利
![david_lowe.jpg](https://upload-images.jianshu.io/upload_images/8207483-6dfd995590e9f8ac.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

David Lowe在1999年所发表，2004年完善总结。并且听说他们在这个算法的 20 周年开一个 party 来庆祝 SIFT 算法。此算法有其专利，专利拥有者为英属哥伦比亚大学。只有在早期的 opencv 中提供该算法，在新版 opencv 已经不再提供该算法。

### 尺度空间

#### 建立高斯差分金子塔
SIFT 算法 是在不同的尺度空间上查找关键点，而尺度空间的获取需要使用高斯模糊来实现，Lindeberg 等人已证明高斯卷积核是实现尺度变换的唯一变换核，并且是唯一的线性核。本节先介绍高斯模糊算法。
![difference_of_gaussian.png](https://upload-images.jianshu.io/upload_images/8207483-9b7ca515df06ee72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

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
关键点就是比较稳定()的点，而且包含许多信息的
什么是关键点稳定性
- 尺度
- skew
- 旋转
- 位移
- 视角
- 遮挡
- 强度，色温
- 
#### 阈值化

$$\begin{cases}
    abs(val) > 0.5 \times \frac{T}{n} \\
    T = 0.04
\end{cases}$$
现在我们极值点查找是在 26 点上查找，以为包含该层上下2两层对应位置点。 

![sift_feature_pointer.png](https://upload-images.jianshu.io/upload_images/8207483-6cba5edbae78b7bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
在检测到极值点$X_0(x_0,y_0,\sigma_0)^T$做三元二阶的泰勒展开

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

