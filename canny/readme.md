### 边缘检测
边缘检测用于图像分割，提取图像形状的信息，那么边缘检测也就是用二值图表示出图片中边缘信息。这里简单介绍一下我们如何判断是边缘，要判断什么是边缘我们就给出边缘定义——图像强度的不连续性就是边缘，那么什么是强度呢，强度暂时可以理解为灰度。

- 表面法向不连续性(surface normal discontinuity)
- 景深不连续性(depth discontinuity)
- 表面颜色不连续性(surface color discontiuity)
- 光照不连续性(illumination discontinuity)

#### 边缘检测历史(了解即可)
通过下面这张图反应了近几十年人类在计算机边缘检测上取得成果。也是如何我们衡量计算机边缘检测的效果好坏。

- Results of Method(RM)
- Ground Truth(GT)
- True Positives(TP)
- True Negatives(TN)
- False Positivies(FP)
- False Negatives(FN)

$$ precision = \frac{GT \bigcap RM}{RM} = \frac{TP}{RM}$$
$$ recall = \frac{GT \bigcap RM}{GT} = \frac{TP}{GT}$$

（图）
边缘是图像强度函数快速变化的地方，通过导数我们可以找到图像强度变化快位置，这个位置就是边缘的位置。
(图)
这里只考虑一行或一列图像(绘制强度随位置变化的曲线)

$$\frac{d}{dx}(f \cdot g) = f \cdot \frac{d}{dx} g $$
根据卷积导数定理，可以先对卷积核进行求导后，再用卷积核扫描图像。这样做较少计算量。

##### 高斯模糊
$$g(x,y) = e^{\frac{-(x^2 + y^2)}{2 \sigma^2}}$$

将求导扩展到二维坐标
- 定义
$$\frac{\partial f(x,y)}{\partial x} = \lim_{\epsilon \rightarrow 0} \left( \frac{f(x+ \epsilon,y) - f(x,y)}{\epsilon} \right)$$
$$\frac{\partial f(x,y)}{\partial y} = \lim_{\epsilon \rightarrow 0} \left( \frac{f(x, y + \epsilon) - f(x,y)}{\epsilon} \right)$$

- 近似
$$\frac{\partial f(x,y)}{\partial x} =   \frac{f(x_{n+1}+y_m ) - f(x_n,y_m)}{1} $$
$$\frac{\partial f(x,y)}{\partial y} =   \frac{f(x_n+ y_{m+1}) - f(x_n,y_m)}{1} $$
- 卷积核
$$\begin{cases}
    f_x = [1 -1] \\
    f_y = \begin{bmatrix}
        1 \\
        -1
    \end{bmatrix}
\end{cases}$$

#### 实例
```python
path = "img/lena.png"
    img = cv2.imread(path,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    k = np.array(([0,0,0],[0,1,0],[0,0,0]),np.float32)
    
    print(k)
    '''
    [[0. 0. 0.]
    [0. 1. 0.]
    [0. 0. 0.]]
    '''
    output = img

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title("Original Image")

    plt.subplot(1,2,2)
    plt.imshow(output)
    plt.title("Filtered Image")

    plt.show()
```
创建数组
```python
k = np.array(np.ones((3,3),np.float32))
k = np.array(np.zeros((3,3),np.float32))
```


#### 梯度算子
##### Prewit
- 读取图片
- 对图片x方向进行平滑（降噪)
- 通过求导计算灰度(强度)变化来检测边缘
$$\begin{bmatrix}
    1 \\
    1 \\
    1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 0 -1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 0 & -1 \\
    1 & 0 & -1 \\
    1 & 0 & -1 
\end{bmatrix}$$
同样做法作用于 y 
##### Sobel
其实 sobel 做的同样事
- 读取图片
- 对图片x方向进行平滑（降噪)
- 通过求导计算灰度(强度)变化来检测边缘
在 x 方向
$$\begin{bmatrix}
    1 \\
    0 \\
    -1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 2 1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 2 & 1 \\
    0 & 0 & 2 \\
    -1 & -2 & -1 
\end{bmatrix}$$
在 y 方向
$$\begin{bmatrix}
    1 \\
    2 \\
    1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 0 -1
\end{bmatrix} \Rightarrow \begin{bmatrix}
    1 & 0 & -1 \\
    2 & 0 & -2 \\
    1 & 0 & -1 
\end{bmatrix}$$

#### 一般步骤
- 对图像灰度处理
- 对图片进行滤波降噪

#### 拉布拉斯高斯

#### 卷积
- 高斯卷积核
    归一化
    二维正态分布，中心对称，会有很多性质，线性可分，可以做平滑，去掉随机噪声，噪点会受到周围点影响，这也是降噪的方式。
- sobel 核
    有两两种分别是水平和垂直方向sobel 核。

我们要找到边，图像变化很大的位置就是边，这样就是边。

我们可以将图像看出二维函数I(x,y)二维离散的函数

$$ G_x =  \begin{bmatrix}
    -1 & -2 & -1 \\
    0 & 0 & 0 \\
    +1 & +2 & +1 \\
\end{bmatrix}$$

$$ G_y = \begin{bmatrix}
    -1 & 0 & +1 \\
    -2 & 0 & +2 \\
    -1 & 0 & +1 \\
\end{bmatrix}$$

$$Edge_Gradient(G) = \sqrt{G_x^2 + G_y^2}$$
梯度的幅值
$$ Angle(\theta) = \tan^{-1} (\frac{G_y}{G_x}) $$
表示梯度方向

#### 

### canny 边缘检测器
canny 是边缘检测算法，在 1986 年提出的

#### 非极大值信号抑制
在梯度方向只保留一点，这样准确找点来表示边缘。由于图像是离散，线性来差值就是解决

我们已知条件 $g_1,g_2,g_3,g_3,\theta$

#### 边缘连接(高低阈值输出二值图像)
双阈值
我们认为大于高阈值maxval的点一定是边，小于最小阈值一定不是边。
- 我们去掉一些边（根据阈值)
- 连接断开的线，

我们可以查看一点的 8 邻域中如果有一个点大于 maxval 也就是说明这一点也一定是边，那么我们就将和当前点进行连接如此下去会得到一条线。压入栈内，然后再出栈然后用这个点的 8 邻域是否为