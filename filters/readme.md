### 滤波
基于物理一些物理模型，今天我们了解什么滤波以及滤波在图像处理和计算机视觉上重要性。首先我们看什么滤波。
我们通过对图像进行滤波来

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

#### 导数(Derivative)
这个在初中可能就学习过去，速度是表示距离单位时间的变化率，那么加速度表示单位时间速度变化率。
$$\frac{df}{dx} = \lim_{\Delta x \rightarrow 0 } \frac{f(x) - f(x - \Delta x)}{\Delta x} = f \prime (x) = f_x$$
$$v = \frac{ds}{dx}$$

#### 均值(Average)
将样本的总数除以样本的个数

#### 2D 导数(Derivatives in 2 Dimensions)
$$f(x,y) \tag{Given function}$$

$$\nabla f(x,y) = \begin{bmatrix}
    \frac{\partial f(x,y)}{\partial f(x)} \\
    \frac{\partial f(x,y)}{\partial f(y)} 
    \end{bmatrix} = \begin{bmatrix}
        f_x \\
        f_y
    \end{bmatrix}$$

$$|\nabla f(x,y)| = \sqrt{f_x^2 + f_y^2}$$

$$\theta = \tan^{-1} \frac{f_x}{f_y}$$

####

$$f_x \Rightarrow \frac{1}{3} \begin{bmatrix}
    -1 & 0 & 1 \\
    -1 & 0 & 1 \\
    -1 & 0 & 1 
\end{bmatrix}$$