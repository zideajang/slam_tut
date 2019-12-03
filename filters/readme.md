### 滤波(filter)
今天我们了解什么是**滤波**以及滤波在图像处理和计算机视觉上的重要性。首先我们来看什么滤波。我们通过对图像进行滤波来进行降噪和特征提取。其中一些重要特征提取的算法都少不了滤波。我们可能会疑惑图像跟波有什么关系?我们可以将图像灰度变化理解为信号的波。通过对灰度变化观察和处理来分析和处理图像。

#### 卷积核
无论是在计算机视觉还是机器学习中图像识别问题都少不了卷积核，卷积核扫图像，通过对像素邻域(周围)点像素值加权求和后取平均值来更新当前像素值。那么卷积核可以看为我们需要滤波器，在波经过滤波器被滤波器所处理。

#### 复习导数和均值
我们在是如何观察灰度变化率，求曲线变化率就是对曲线进行求导，所以有必要复习导数知识。
##### 导数(Derivative)
这个在初中可能就学习过去，速度是表示距离单位时间的变化率，那么加速度表示单位时间速度变化率。
$$\frac{df}{dx} = \lim_{\Delta x \rightarrow 0 } \frac{f(x) - f(x - \Delta x)}{\Delta x} = f \prime (x) = f_x$$

我们知道距离求导就是物体的运动在某个时刻的速度
$$v = \frac{ds}{dx}$$
我们知道对速度求导就是物体的运动在某个时刻的加速度（衡量速度变化）
$$ a = \frac{dv}{dx}$$

因为图像数据是一个一个像素点，所以数据是离散的，我们将连续问题转化为离散上，假设最小变换就是移动一个单位，现在我们将变换参照从时间上转移到空间上
$$ \frac{df}{dx} = \frac{f(x) - f(x-1)}{1} = f \prime (x)$$

$$ \frac{df}{dx} = f(x) - f(x-1) = f \prime (x)$$

- 前向差值
$$ \frac{df}{dx} = f(x) - f(x-1) = f \prime (x)$$
- 后向差值
$$ \frac{df}{dx} = f(x) - f(x+1) = f \prime (x)$$
- 差值
$$ \frac{df}{dx} = f(x+1) - f(x-1) = f \prime (x)$$

通过下方程我们可以看出是如何去像素进行求导
$$
\begin{aligned}
    f(x) = [10,15,10,10,25,20,20,20] \\
    f \prime (x) = [0,5,-5,0,15,-5,0,0] \\
    f \prime \prime (x) = [0,5,-10,5,15,-20,5,0]
\end{aligned}
$$
这里大家自己计算一下很简单后项减去前项除以1即可[-1,1],这样就会发现一维变化率。

我们图片是2D维数据，我们可以用 openvc 的命令查看一下图片具体数据结构
```python
   img = cv2.imread("img/bird.jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(gray)
```
```
[[136 135 133 ... 101 101 101]
 [136 135 133 ... 101 101 101]
 [136 134 133 ... 101 101 101]
 ...
 [204 213 206 ...  86  86  87]
 [198 200 186 ...  86  86  87]
 [191 189 162 ...  86  87  87]]
 ```
##### 2维 导数(Derivatives in 2 Dimensions)
那么我们来看一看对有两个特征的函数进行求导，也就是 2维求导
$$f(x,y) \tag{Given function}$$

因为函数变换率体现在 x 和 y 两个变量上，所以我们需要分别对 x 和 y 进行求偏导，然后用一个向量来表示变化率。
$$\nabla f(x,y) = \begin{bmatrix}
    \frac{\partial f(x,y)}{\partial f(x)} \\
    \frac{\partial f(x,y)}{\partial f(y)} 
    \end{bmatrix} = \begin{bmatrix}
        f_x \\
        f_y
    \end{bmatrix} \tag{Gradient vector}$$

下面变化率大小，就是通过对 x 和 y 取模，也就是求距离
$$|\nabla f(x,y)| = \sqrt{f_x^2 + f_y^2} \tag{Gradient magnitude}$$
一维变化率是一个向量，向量不但有大小而且有方向表示变化率方向

$$\theta = \tan^{-1} \frac{f_x}{f_y} \tag{Gradient direction}$$

#### 滤波一个简单应用
我们现在停下做一个小实验，通过过滤做一个有趣的简单实验
$$
\begin{bmatrix}
    0 & 0 & 0 \\
    0 & 0 & 1 \\
    0 & 0 & 0 
\end{bmatrix}
$$
我们用这样卷积核扫过图像，会起到像右侧平移图像一个像素的效果。要做到这个件事我们需要几个步骤
- 将图片灰度化处理
- 然后创建一个 3 x 3 的卷积核
- 实现卷积核在图像上游走，将像素更新为其周围的像素和卷积核相乘等于对于取权重后求和在做标准化。

```
for i in (1,img_height - 1)
    for j in (1,img_width - 1)
        更新 img[i,j]
```

```python
def move_img_by_filter(img):
    conv = cnp.array([0,0,0,0,0,1,0,0,0]).reshape(3,3)
    h = img.shape[0]
    w = img.shape[1]
    for i in range(1,h-1):
        for j in range(1,w-1):
            print(img[i,j])
            img[i,j] = (img[i-1,j-1] * conv[0,0] + img[i-1,j]*conv[0,1] + img[i-1,j+1]*conv[0,2] +
                img[i,j-1] * conv[1,0] + img[i,j]*conv[1,1] + img[i,j+1]*conv[1,2] +
                img[i+1,j-1] * conv[2,0] + img[i+1,j]*conv[2,1] + img[i+1,j+1]*conv[2,2])
            # print(img[i,j])
    return img
```



### 滤波的应用
在今天我们计算机视觉和图像处理中少不了边缘检测和特征点检测。在今天边缘检测依旧具有重要地位。
#### 边缘检测
所谓边缘也就是灰度变化的位置，在连续函数跳跃的
$$f\prime(x) = \lim_{x \rightarrow \infty} \frac{f(x + 0.5h) - f(x-0.5h)}{h}$$

我们可以通过卷积核实现在图像求导，我们知道在计算机视觉中难点是噪声，因为噪声我们无法通过导数来判断出边缘。
我们可以先做高斯模糊，这样就不噪声模糊掉，虽然也将跳跃信号模糊掉，但是当我们再进行求导时，这回我们信号变化就不会受到噪声变化。
#### Binary Images
我们通过 0 或 1 来表示(描述)一张图片
#### Gray Level Images
#### Gray Scale Image
#### Color Image Red Green Blue 
#### Image Histogram

#### Image Noise
- Light Variations
- Camera E

- I(x,y) 真实值
- n(x,y) 噪声
- $$\hat{I}(x,y) $$ 

高斯概率分布
$$n(x,y) = e^{\frac{-x^2}{2 \sigma^2}}$$
- x 表示

### 图像滤波
#### 高斯滤波
$$ \frac{1}{16} \begin{bmatrix}
    1 & 2 & 1 \\
    2 & 4 & 2 \\
    1 & 2 & 1 
\end{bmatrix}$$
#### 线性滤波
$$ \frac{1}{9} \begin{bmatrix}
    1 & 1 & 1 \\
    1 & 1 & 1 \\
    1 & 1 & 1 
\end{bmatrix}$$

平移
$$
\begin{bmatrix}
    (i-1,j-1) & (i-1,j) & (i-1,j+1) \\
    (i,j-1) & (i,j) & (i,j+1) \\
    (i+1,j-1) & (i+1,j) & (i+1,j+1) 
\end{bmatrix}
$$


####

$$f_x \Rightarrow \frac{1}{3} \begin{bmatrix}
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
    -1 & 0 & 1 
\end{bmatrix}$$

```python
def create_kernel():
    arr = np.array([0,0,0,0,1,0,0,0,0])
    return arr.reshape(3,3) 
```

#### 均值(Average)
将样本的总数除以样本的个数




#### 高斯求导(DoG)
因为图像有噪声，我们无法找到灰度变化，通常的做法是现用高斯滤波去噪，然后在对其进行求导就可以。这样我们就先进行高斯滤波降噪，然后再进行一次求导，这样进行两次运算。
$$\frac{\partial}{\partial x}(h * f) = (\frac{\partial}{\partial x}h)*f$$
在上面方程中 f 表示图像像素点值，h 表示高斯函数，我们可以先进行高斯卷积操作然后对其进行求导来，也可以先对高斯进行求导然后在进行卷积。
有时候我们要找信号跳动
#### 卷积核
其实卷积就是一个滤镜，我们通过滤镜可以对图片进行模糊处理，也就是降噪。但是滤镜不但可以做模糊可以做图片锐化处理，这个是由卷积核来决定的。使用滤镜过程就是在原图不断移动滤镜。
![numerical_padding_strides.gif](https://upload-images.jianshu.io/upload_images/8207483-a802ea80e1b76afd.gif?imageMogr2/auto-orient/strip)

#### 均值滤波(模糊)
均值模糊，也称为均值滤波，相当于卷积核的矩阵值全部为1/(卷积SIZE)。均值模糊相对要简单一些。

代码实现
```python
def mean_blur(img):
    height,width,deep = get_img_info(img)
    dst = np.zeros((height,width,3),np.uint8)
    for i in range(0,height - 3):
        for j in range(0,width - 3):
            sum_b = int(0)
            sum_g = int(0)
            sum_r = int(0)
            for m in range(-3,3): #-3,-2,-1,0,1,2
                for n in range(-3,3):
                    (b,g,r) = img[i+m,j+n]
                    sum_b = sum_b + int(b)
                    sum_g = sum_g + int(g)
                    sum_r = sum_r + int(r)
                b = np.uint8(sum_b/36)
                g = np.uint8(sum_g/36)
                r = np.uint8(sum_r/36)
                dst[i,j] = (b,g,r)
    return dst
```

#### 高斯滤波(模糊)

#### 高斯分布
首先我们介绍一下高斯分布，个人决定这个高斯分布是一个比较重要概念，无论是在计算机视觉和机器学习中都在占据重要地位，在随后介绍 Kalman filter（卡尔曼滤波)都是基于高斯分布。有关高斯分布重要性随着大家学习，大家就会发现其有多么重要。

$$f(x) = \frac{\sigma \sqrt{2 \pi}}{1} e^{ - \frac{(x-\mu)^2}{2 \sigma^2}}$$

- 关于 x =

接下来我们就要介绍
### 傅里叶变换
#### 傅里叶变换的重要性
我们现在机器学习上音频和图像上处理上都会用到傅里叶变换，今天我们在 app 中用到声音处理和美图都是基于傅里叶变换的。所以傅里叶变换还是比较重要的，和贴近生活的。这是一些额外的知识，不了解也没有什么关系，我们在 SLAM 有时候只要会用公式就行，也没有必要探究其背后的原理。
#### 什么是傅里叶变换

我们先把最重要的内容说出来，也就是什么是傅里叶变换。将任意周期函数拆解为一系列一个正（余）函数的和。好有了这样一个目标我们看看傅里叶变换是怎么推导。

#### 什么是变换
说到变换，我们先来说一说什么是变换，变换很好理解也就是不同的表达，下图中在坐标系(空间)的两个点，我们可以用这样图形方式表示
![屏幕快照 2019-12-03 上午5.29.59.png](https://upload-images.jianshu.io/upload_images/8207483-dbd1f858cc5b318e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

也可以用向量方式表示为A(2,1)和B(2,1),这就是变换，大家看了可能感觉无趣，其实是有好处，不同表达有时候利于我们计算
![屏幕快照 2019-12-03 上午5.31.18.png](https://upload-images.jianshu.io/upload_images/8207483-8dbe8d2e117478c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

例如我们要计算这样一个平行四边形对角线，将图形问题转换为向量计算就比较容易。


#### 时域和频域
我们生活的世界都以时间为序列，我们成长，听到的音乐、汽车的轨迹都会随着时间发生改变。这种以时间作为参照来观察动态世界的方法被称为时域分析。不过我们可以从另一个角度来观察世界，例如我们不是听音乐，而是看乐谱，可能会发现世界是永恒不变的，这个静止的世界就叫做频域

那么我们可以将时域上观察的函数，换一个角度从时域上按频率不同来将函数分解为若干周期函数，这就是从图形上对傅里叶变换进行解释。
![Fourier_transform.jpeg](https://upload-images.jianshu.io/upload_images/8207483-55df8d54a68ab16c.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 傅里叶级数构成
图形上我们了解什么是傅里叶变换，现在再从公式来推导一下傅里叶变换
$$ f(x) = C + \sum_{n=1}^{\infty}(a_n \cos(\frac{2 \pi n}{T}x) + b_n \sin (\frac{2 \pi n}{T} x)) , c \in \mathbb{R}$$

1. 这样一个公式就很好理解，首先我看常数项 C
- g(x) = C 一定是一个周期函数，这个应该没有问题，而且他周期是任意的
- 常数项可以用于调节函数值

2. 我们来思考一下为什么傅里叶级数需要 sinx 和 cosx 函数
- 我们知道任何一个函数都可以写成一个奇函数和偶函数的和
$$f(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$$
这样形式，其中$ \frac{f(x) + f(-x)}{2}$ 是偶函数相当于 cosx 而 $\frac{f(x) - f(-x)}{2}$ 相当于奇函数(sinx)
- 那么我们再来看一看周期$\frac{2 \pi n}{T}$,我们看一函数的周期是 $\frac{2 \pi}{\frac{2 \pi n}{T}} = \frac{T}{n}$, 我们对于$\frac{T}{n}$ 周期函数他的周期可以看做T。这个应该没有问题
3. 我们在看一看系数$a_n$ 和$b_n$ 因为我们知道 $\sin x$ 的取值范围为$-1 \le \sin x \le 1$,所以我们需要$a_n$来调节振幅

#### 从自然数到复数
我们在继续介绍傅里叶变换前，来简单地介绍一下复数来来历，因为随后我们会用到复数。
开始最熟悉是自然数，然后随着减法的出现，一个较小自然数减去一个较大自然数,这时自然数就无法满足这个要求了，于是出现整数，增加了负数。然后随着除法的出现，因为有些整数是无法进行整除的，为了满足这个需求，这时在整数基础上引入了分数来解决这个问题，开发了，因为平方都是整数，那么我们如何对负数进行开方，这就引入了复数。

#### 基向量和基函数


在线性空间里我们的一个向量是可以表示为
$$\vec{a} = a_1 \vec{i} + a_2 \vec{j}$$
通过基向量的组合来表示向量，这里$\vec{i}$ 看做基向量而$a_1$看做系数，那么我们函数也存
这里基向量$\vec{i}$和$\vec{j}$需要满足他们是正交基向量，如果两个向量正交那么需要满足$\vec{i} \cdot \vec{j} = 0$，这样一组基向量
在用基函数和系数组合来表示一个函数
$$\int_{-\pi}^{\pi}f(x)g(x)$$

$$\begin{cases}
    \frac{\vec{a}\vec{u}}{\vec{u}\vec{u}} = a_1 \\
    \frac{\vec{a}\vec{v}}{\vec{v}\vec{v}} = a_2
\end{cases}$$

$$\begin{aligned}
    a_n = \frac{\int_0^Tf(x)\sin(\frac{2\pi n}{T}x)dx}{\int_0^Tf(x)\sin^2(\frac{2\pi n}{T}x)} \\
    b_n = \frac{\int_0^Tf(x)\cos(\frac{2\pi n}{T}x)dx}{\int_0^Tf(x)\cos^2(\frac{2\pi n}{T}x)} 
\end{aligned}$$

#### 欧拉公式

$$e^{it} = \cos t + i \sin t$$
$$e^{-it} = \cos t - i \sin t$$

$$\begin{cases}
    \cos mt = e^{imt}+e^{-imt} \\
    \sin nt = 
\end{cases}$$


#### 拉普拉斯变换
信号分析都会用到拉普拉斯变换，感性的认知。对于基本公式，有了之前傅里叶变换基础拉布拉斯变换也就不难理解，因为拉布拉斯是傅里叶加强版。

$$f(t) = \sum_{n-1}^{\infty} A_n \cos(n w_0 t + ) + B$$

$$F(w) = \int_{-\infty}^{\infty}$$

欧拉公式
$$e^{ix} = \cos x + i \sin x$$

#### 笔记
- 加性噪声
- 乘性噪声
- 高斯噪声
- 白噪声

##### Box Filter
$$ \frac{1}{9} \begin{bmatrix}
    1 & 1 & 1 \\
    1 & 1 & 1 \\
    1 & 1 & 1 
\end{bmatrix}$$

$$h[m,n] = \sum{k,l} g[k,l] f[m+k,n+l]$$

互相关(cross-correlation)
矩形框进行滤波，门限滤波器在高频会有跳跃，
- blur
- boxFilter 可用归一化

##### 卷积
$$h[m,n] = \sum{k,l} g[k,l] f[m-k,n-l]$$ 都是线性操作，好的性质两个滤波器依次处理，可以先对两个滤波器进行处理然后在进行。微分运算