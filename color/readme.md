颜色看似一个简单话题，其实并没那么简单，因为我们没思考过其背后的秘密，今天我们一起看看我们是如何感知颜色和区分颜色的。这是一次有趣分享，希望大家关注。

### 颜色
颜色不单纯作为我们感知世界区分物体一个特征，颜色有时候还反应我们心情，我们通常用一些颜色来反应我们的心情，例如绿色代表生机勃勃、灰色和蓝色代表淡淡的忧伤，红色和橘红色代表热情和温暖。其实颜色涵盖理论也很多，因为我们是在 SLAM 研究。这里就只做简单介绍，并不作为重点，如果大家感性可以自己找一些资料再深入学习。

### 如何感知颜色
计算机是如何感知颜色，其实这是一门仿生学，计算机认识和区分颜色过程类似于人类的认识颜色。虽然这并不是最优方式，但是这是至少是一种可行方案。我们先从我们人类是如何感知颜色说起，然后让计算机模仿人类认识颜色方式来认知颜色和识别颜色。
#### 视锥细胞分
大部分人类的视网膜上有三种感知颜色的感光细胞，叫做视锥细胞，分别对不同波长的光线敏感，称为 L/M/S 型细胞。三种视锥细胞最敏感的波长分别是波长为 700nm 的红色（Red）、波长为 546.1 nm 的绿色（Green）以及波长为 435.8 nm 的蓝色（Blue）
![color_spectrum.png](https://upload-images.jianshu.io/upload_images/8207483-6fc7de059d7e8896.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在上图中可以看到 L 型视锥细胞与 M 型视锥细胞的感光曲线差别很小，实际上这两种视锥细胞起源于一次基因变异，在这之前人类可都是红绿色盲呢，因为这个基因变异，人类才可以看到更加多彩的世界。
#### 视柱细胞分
除了视锥细胞分我们还柱形细胞，在环境比较暗环境下对颜色进行感光，也就是我们在月光比较好情况下，观察外面景物会发现他们都是变灰白的，看到物体色彩饱和度不高， 这是因为柱形细胞是对颜色感知较弱。

还要说明物体本身是没有颜色的，这是我们通过其反射光来感知其颜色，那么我们接受到光频谱是由两个方面决定的，一个是照射物体的光源的光谱的频率，一个看到物体对这个光哪些频率进行反射。

好我们现在分析一下人眼如何看到东西的
1. 首先要有光源发射可见光
2. 物体接收可见光，并且根据自身材质会发射光
3. 我们看到光是自然光和反射光的叠加 

### 颜色的表述
上面介绍我们是如何感知光来看见物体的颜色，下面介绍我们是如何是如何区分光。
在生活中我们往往想用语言来表述一种颜色，最终都会发现这是一件很难的事，例如现在手机厂商创造出许多关于颜色的新词来定义手机外壳颜色。这是因为我们人类语言中几十种颜色的表述是无法对应上上百万种的颜色。那么我们如何表示颜色呢?这里就引入 GRB 通过3种主色来混合表示一种颜色，不同主色量表示不同颜色这种形式来描述一个颜色。

| 区分  |  颜色数量 |
|---|---|
| 彩虹  | 7  |
| 蜡笔  | 120  |
| HTML 中颜色 | 121  |
| X11/rgb.txt （linux window 系统颜色） | 881  |
| 英文出现颜色种类  | ~4000  |

下面介绍一个我们通过实验来区分颜色方法，这是实验性的定律

#### 颜色匹配
格拉斯曼定律是一个实验规律，并没有物理或者生物学上的依据。然而这个规律大大简化了我们对人类彩色视觉系统的建模，并且给我们使用线性代数理论分析人类彩色视觉系统提供了一个前提和基础。

实验过程大致是这样的，把一个屏幕用不透光的挡板分割成两个区域，左边照射某个被测试的颜色的光线，这里记为 C （以下用大写字母表明颜色，用小写字母表明分量大小），右边同时用三种颜色的光同时照射，这里记为 R，G，B。然后，调节右边三种颜色光源的强度，直到左右两边的颜色看上去一样为止。假设这个时候三种颜色的光源强度分别为r，g，b，那么根据光色叠加的线性性质，我们可以写出

$$ C = rR + gG + bB $$

有了颜色匹配函数，我们就对任意频谱的光都可以用RGB组合来描述。


### 色彩空间
下面介绍一些用来描述颜色的色彩空间，通过这些空间我们可以定位和区分颜色。

#### CIE XZY
在 CIE XZY 色彩空间，好处就是我们通变换避免了在 RBG 某一个维度出现负数，以色匹配函数作为基底，将物理上的光谱分布投影到三维空间中，就可以得到 CIE RGB 和 CIE XYZ 色彩空间。 CIE RGB 的色匹配函数（归一化后）是这样的：


#### RGB 和 XZY
我们通常接触更多的是 RGB 色彩空间而不是 XZY 色彩空间，那么他们两者有什么不同，以及如何相互转换呢。首先 XYZ 是标准颜色空间，XYZ 要比 RGB 更加准确。sRGB 是标准 RGB 空间，而其他RGB 不同公司有不同的标准。
由于 CIE RGB 和 CIE XYZ 两者其实是同一个线性空间的不同表达，因此两者的转换可以通过转换矩阵实现。

注意这里进行了归一化处理，因此曲线与上一篇文章中的曲线形状有变化。为了消除部分负数坐标，我们变换到 CIE XYZ 空间，满足一些约束条件：

- 所有坐标都是正的保持等能点作为白色
- 使得新的 Y 坐标能够代表明度，也就是使得新的 Y 坐标等于视觉的明度响应
- 使得新的 Z 坐标在红光端保持为 0
- 使得所有色彩尽可能充满新的空间

$$
\begin{bmatrix}
    X \\
    Y \\
    Z
\end{bmatrix} = \begin{bmatrix}
    2.7688 & 1.7517 & 1.1301 \\
    1.0000 & 4.5906 & 0.0601 \\
    0 & 0.0565 & 5.5942 
\end{bmatrix} = \begin{bmatrix}
    R \\
    G \\
    B
\end{bmatrix}
$$

$$
\begin{bmatrix}
    R \\
    G \\
    B
\end{bmatrix} = \begin{bmatrix}
    0.4185 & -0.1587 & 0.0828 \\
    -0.0912 & 0.2524 & 0.0157 \\
    0.0009 & 0.0025 & 0.1786 
\end{bmatrix} = \begin{bmatrix}
    X \\
    Y \\
    Z
\end{bmatrix}
$$
  
![rgb_color_space.png](https://upload-images.jianshu.io/upload_images/8207483-fb0a67aa5cb68afc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


很多数码相机都可以设置色彩空间，常见的有 sRGB 和 Adobe RGB，从上面的图中我们可以看到， Adobe RGB 所能表达的色彩比 sRGB 要丰富很多。由于 sRGB 是目前屏幕显示的**事实标准**，大多数屏幕空间都在 sRGB 内（这是颜色复现设备本身决定的），所以我的建议是，对用于网络交流目的的图片，统一转换到 sRGB 中进行保存。但是无论怎么设置色彩空间，都无法用三角形来覆盖整个色彩空间,因为色彩空间并不是三角形。但是一些高端相机声称有第4种主色来试图涵盖更广色彩空间。


#### YUV 
图像和视频压缩都会用到 YUV 这个色彩空间。我们做一个实验，我们知道图片分别是 R，G 和 B 三个通道值叠加而成，我们可以将三个通道进行分离，然后进对一个通道进行高斯模糊，然后再将三个通道进行叠加，由于我们对于某一个通道进行模糊，所以图片也随之变得模糊。这里有一个有趣的事情就是我们会发现其中绿色通道模糊要比其他两个通道模糊对图像影响更大。这是因为我们对绿色比较敏感，而对于红色和蓝色并不那么敏感。

那么对于 YUV 色彩空间图片，如果我们对 UV 进行模糊处理影响了，我们几乎是发现不了的。这样我们可以对 UV 通道进行压缩而不会影响图片效果

#### 如何得到一张彩色图像
在彩色照相机出现之前，就有人用一些技巧来拍摄彩色照片。我们知道黑白照相机是可以拍摄到光的强弱的，一个简单做法就是在拍照时候，在镜头加一个滤光片（红绿蓝）。如果将红色滤光片，就可以过滤掉蓝色和绿色光，将红色光记录拍摄下来。然后如何将色彩呈现到胶片也是一件难事，通过一些技巧也可以解决，就是找到 3 个白色灯，，每一个灯方方一个滤光片对其
![bayer_pattern.jpeg](https://upload-images.jianshu.io/upload_images/8207483-41906de711bd777d.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过滤镜将普通的入射光分为红绿蓝RGB三个分量。很容易联想到普通的图片每个像素点都包含RGB三个分量的信息，这很容易误导我们认为CCD也接收了每个像素点的三个通道的信息。然而并不是，原理图如上图，每一个像素点都只接收了RGB三个分量中的一个分量。一般而言是按照“RG/GB”的方式排列。因为我们介绍过我们对绿色比较敏感所以绿色接收器多一些。

将Bayer Pattern的格式转换为RGB，那就需要通过插值的方式将每个像素点中丢失的两个颜色找回来。有几种插值的方式可以使用，但是最常用的方法是线性插值的修正调节版本。

#### 逆马赛克算法(Demosaicing)
逆马赛克算法是一种数字图像处理方法，用于重建图像的所有色彩信息，其算法对象为装有彩色滤镜阵列（CFA）的图像传感器，这种彩色滤镜阵列中所有滤镜的通过波长是不完全一致的。逆马赛克变换也称作CFA插值或色彩重建。
![demosaicing.jpeg](https://upload-images.jianshu.io/upload_images/8207483-962f43bc633a13c1.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### OpenCV 中的色彩空间



#### chromaticity coor

当然，色彩空间并不是真正数学意义上的三维线性空间。由于不存在真正数学意义的「减法」，在实际应用中是有所限制的。数学中的「线性组合」在这里就要被替换为「锥组合」，也就是每个分量都必须是大于等于 0 的。