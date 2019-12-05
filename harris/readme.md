## 特征
### 测量特征
这里提取特征，不是识别出是什么物体，这里需要说一下，这里我们所说的特征并不是机器学习用于分类的识别特征。
例如，我们需要通过识别图像的特征来识别一些标志性旅游点和建筑物。更进一步说，不但要识别还要定位（导航）出现在位置，这也就是 SLAM 了。还有今天会介绍全景图，现在手机都提供了全景图效果。我们可以通过检测两张图片的共同特征点然后根据这些相同特征点进行拼接取图片




图像全局特征包括颜色特征、纹理特征以及形状特征。今天我们来介绍一些局部特征，今天本来想在完成傅里叶变换和拉普拉斯变换后，在继续向下进行。不过避免让大家因过多的公式推导而感觉枯燥乏味，今天插播一个比较贴近使用的 harris 角点检测​。


局部特征包括边特征、角点特征点，通过提取这些特征点可以帮助我们分析物体在空间上运动。在 3D 重建和照相机推导问题中也会用到局部特征点检测，今天介绍 harris 角点检测

## Haars特征原理
### 什么是角点，角点的用途

图像中有学多角点，例如建筑物的角，电视的边角，期盼的边角，这些都是角点。​角点作为图片的一个特征，可以用于描述图片中一些位置信息，尤其对于图像中的物体定位特别有用。
### 如何识别角点
那么首先我们需要区分边和角，并行于边方向变化像素灰度变化不大，垂直方向像素变化大。那么相对于边角点在各个方向上都变化就认为是边。

![harris_1.jpeg](https://upload-images.jianshu.io/upload_images/8207483-c21208d1a53aa29e.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- (flat) 在任意方向没有明显的变化
- 边(edge) 沿边方向没有明显的变化
- 角点(corner) 在所有方向都有变化

### 公式推导
在推导过程中我们会用到高等数学的知识，
$$ E(u,v) = \sum_{x,y}w(x,y)[I(x+u,y+v) - I(x,y)]^2$$
- w 我们暂时忽略考虑 w，在窗口 w 内的值全部都为 1 而窗口外面的值都 0
- UV u 表示向竖直方向移动一个,v 表示水平单位
- w 窗口会包括一定数量像素，数量根据 w 窗口的大小而定。w 窗口内每一个点位置是由 x 和 y 而定，然后移动窗体 w 水平方向 u 距离，在垂直方向移动 v 距离后得到新窗口，那么新窗口包括点位置就是对应点就是 (x+u,y+v) 通过对相对于窗口相同位置两次对应点进行差值后平方在取和来表示变化率，变换率越大说明这里就是边或角点，如果是角点我们就是希望无论窗口向哪个方向移动，变化率都要比较低。

![harris_window_gaussian.png](https://upload-images.jianshu.io/upload_images/8207483-7794c8ace148f78c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
高斯核(窗口)权重分布按高斯分布，距离中心的权重较高，四周的权重较小。
![harris_window_uniform.png](https://upload-images.jianshu.io/upload_images/8207483-620d4a3bcda5540c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这样卷积核(窗口)内点值为 1 窗口外点都为零。

好了现在我们明确目标，完成对角点检测的建模。

### 泰勒展开
$$ 
\begin{aligned}
    f(x+u,y+v) = f(x,y) + uf_{x}(x,y) + vf_y(x,y) +  \\
\frac{1}{2!}[u_{2}f_{xx}(x,y) + uvf_{xy}x,y+ v^2f_{yy}(x,y)] + \\
\frac{1}{3!}[u^3f_{xxx}(x,y) + u_{2}f_{xx}(x,y) + uvf_{xy}x,y+ v^2f_{yy}(x,y) + v^3f_{yyy}(x,y)]
\end{aligned}
$$

上面是泰勒展开，不过这里我们这里只需要泰勒展开一阶导数

$$f(x+u,y+v) \approx f(x,y) + uf_{x}(x,y) + vf_y(x,y)$$


$$\begin{aligned}
    \sum_{x,y} \left[ I(x+u,y+v) - I(x,y) \right]^2  \tag{1}\\
    \sum_{x,y} \left[ I(x,y) +uI_x + vI_y - I(x,y) \right]^2 \\
    \sum_{x,y} \left[ u^2I_x^2 + 2uvI_x^2I_y^2 + v^2I_y^2 \right] 
    \end{aligned}
$$
上面推导应该不难理解，这里用泰勒一阶展开式将方程进行化简。


然后我们将上面线性方程写出矩阵的形式
$$
    \sum_{x,y} \begin{bmatrix}
        u & v
    \end{bmatrix} \begin{bmatrix}
        I_x^2 & I_xI_y \\
        I_xI_y & I_y^2
    \end{bmatrix} \begin{bmatrix}
        u \\
        v
    \end{bmatrix} \\
$$
因为求和是和x和y 相关与 u和 v 相关可以将求和sigma移动到内部矩阵
$$
      \begin{bmatrix}
        u & v
    \end{bmatrix} \sum_{x,y} \left( \begin{bmatrix}
        I_x^2 & I_xI_y \\
        I_xI_y & I_y^2
    \end{bmatrix} \right)
    \begin{bmatrix}
        u \\
        v
    \end{bmatrix} 
$$

$$E(u,v) = \begin{bmatrix}
        u & v
    \end{bmatrix} \sum_{x,y} \left( \begin{bmatrix}
        I_x^2 & I_xI_y \\
        I_xI_y & I_y^2
    \end{bmatrix} \right)
    \begin{bmatrix}
        u \\
        v
    \end{bmatrix} $$
在 u v 取任意值，都让 E(u,v)尽量大,我们在方程进行化简一下。

$$\begin{cases}
    E(u,v) \approx \begin{bmatrix}
        u & v
    \end{bmatrix}
    M
    \begin{bmatrix}
        u \\
        v
    \end{bmatrix} \\
    M = \sum_{x,y} w(x,y) \begin{bmatrix}
        I_x^2 & I_xI_y \\
        I_xI_y & I_y^2
    \end{bmatrix}
\end{cases}$$

在继续进行化简我们需要了解什么**实对称矩阵**，以及什么是
如果有n阶矩阵A，其矩阵的元素都为实数，且矩阵A的转置等于其本身（aij=aji）(i,j为元素的脚标)，则称A为实对称矩阵。

我们知道实对称矩阵是可以相似对角化，那么什么是相似对角化呢，他定义是假设 A 为 n 阶方阵，若存在可逆矩阵P，使得$P{-1} A P = \Lambda$ 其中$\Lambda$ 是对角矩阵，则称矩阵 A 可视化。

$$ \begin{cases}
    P \begin{bmatrix}
        \lambda_1 & 0 \\
        0 & \lambda_2
    \end{bmatrix} P^{-1}\\
    P^T = P^{-1}
\end{cases} $$

有了上面实对称矩阵和相似对角化的知识，我们就可以将 M 进行变换为上面矩阵并且 P 是正交矩阵，所以 P 的转置等于 P 的逆。

$$\begin{aligned}
    E(u,v) = \begin{bmatrix}
        u & v
    \end{bmatrix} P \begin{bmatrix}
        \lambda_1 & 0 \\
        0 & \lambda_2
    \end{bmatrix} P^T \begin{bmatrix}
        u & v
    \end{bmatrix}^T \\
    E(u \prime,v \prime) = \begin{bmatrix}
        u & v
    \end{bmatrix} \begin{bmatrix}
        \lambda_1 & 0 \\
        0 & \lambda_2
    \end{bmatrix}  
    \begin{bmatrix}
        u \prime \\ 
        v \prime
    \end{bmatrix} \\
    \lambda_1(u \prime)^2 + \lambda_2(v \prime)^2 \\
    = \frac{(u \prime)^2}{\frac{1}{\lambda_1}} + \frac{(v \prime)^2}{\frac{1}{\lambda_2}}
\end{aligned}$$

有了实对称矩阵 M ，这个可以根据上面实对称矩阵定义而知，然后将 P 的转置写成 P 的逆，然后我们可以 P 和 uv 矩阵进行合并，因为 P是正交矩阵所以相当对矩阵进行旋转操作。经过一系列化简我们发现如果想让E(u,v)尽可能大，就得让$\lambda_1$ 和$\lambda_2$尽可能大。而且从形式上看这就是一个椭圆方程，那么椭圆中方程 $a^2 = \lambda_1^{-1}$ 以及 $b^2 = \lambda_2^{-1}$ 

![harris_region.jpg](https://upload-images.jianshu.io/upload_images/8207483-360863f862f143f0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

那么到现在我们明白了上图$\lambda_1$和$\lambda_2$ 含义，以及他们不同取值会得到不同特征，如果其中一个lambda 很大就是边，如果两个 lambda 都很大就是角点。

为了方便描述 $\lambda_1$ 和 $\lambda_2$ 都大，方便计算对行列式也就是特征值的乘积也就是lambda1 和lambda2乘积，对角线元素和就是

$$ R = det M - k(trace M)^2$$
$$\begin{cases}
    det M = \lambda_1 \cdot \lambda_2 \\
    trace M = \lambda_1 + \lambda_2 \\
    k 是一个参数
\end{cases}$$

计算出 R值就是每一个像素点得分，$\lambda_1 ,\lambda_2$越大得分越大。