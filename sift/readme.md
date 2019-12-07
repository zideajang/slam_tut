### SIFT 的介绍
- 找有兴趣点
- 描述兴趣点

当我们看到一张图片，我们怎么描述一张图
- 颜色
- 材质
- 局部、全局
- 形状（我们怎么关注局部)
    - 那些点附近形状是**特征点**
    - 如何描述或量化

#### 如何决定好的描述法
- 辨识度
不同样子，希望在描述空间位置不同
- 不变性
同样样子，希望在描述空间的位置相同

#### 常见不变性
免疫于变换
- scale
- skew
- rotation/orientation
- tranlsation
- 视角
- occulusion 遮挡
- luminance 强度，色温

#### 辨识度与不变性之间权重
- 不变性一定
  6 和 9
- 更极端的例子
- 正如 ML 中，太 Robust 的 model 也会把用的信息吃掉

#### 我们
- 独特性 没有 ambiguous 没有 depeneracy
- 角落和blob(corner 和 blob)

blob
- 1D Blobs
- 2D Blobs

### 高斯一阶，二阶微分算子

在卷积等效为微分，
### 尺度空间

$$Blob size $$

$$(x,\sigma) = \arg \max_{(x,\sigma)} |\frac{\partial^2 n_{\sigma}}{\partial x^2}|$$

#### 卷积和微分是有交换律

laplacian of Gaussian VS Difference of Gaussian

$$G(x,y,s \sigma) - G(x,y,\sigma) \approx (s-1) \sigma^2 \nabla^2 G$$