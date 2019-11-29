### 特征点检测
特征点检查是我们分析问题模型。特征点是一切分析基础，也就是我们收集数据，所以再好的模型在不好土壤上也无法长出。

### SIFT 历史
David Lowe在1999年所发表，2004年完善总结。并且听说他们在这个算法的 20 周年开一个 party 来庆祝 SIFT 算法。此算法有其专利，专利拥有者为英属哥伦比亚大学。只有在早期的 opencv 中提供该算法，在新版 opencv 已经不再提供该算法。

1. 尺度空间极值检测：搜索所有尺度上的图像位置。通过高斯微分函数来识别潜在的对于尺度和旋转不变的兴趣点。


2. 关键点定位：在每个候选的位置上，通过一个拟合精细的模型来确定位置和尺度。关键点的选择依据于它们的稳定程度。


3. 方向确定：基于图像局部的梯度方向，分配给每个关键点位置一个或多个方向。所有后面的对图像数据的操作都相对于关键点的方向、尺度和位置进行变换，从而提供对于这些变换的不变性。


4. 关键点描述：在每个关键点周围的邻域内，在选定的尺度上测量图像局部的梯度。这些梯度被变换成一种表示，这种表示允许比较大的局部形状的变形和光照变化。


首先我们需要不同模糊程度的图片

$$f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{- \frac{(x-\mu)^2}{2 \sigma^2}}$$

SIFT 算法 是在不同的尺度空间上查找关键点，而尺度空间的获取需要使用高斯模糊来实现，Lindeberg 等人已证明高斯卷积核是实现尺度变换的唯一变换核，并且是唯一的线性核。本节先介绍高斯模糊算法。

高斯模糊是一种图像滤波器，它使用正态分布(高斯函数)计算模糊模板，并使用该模板与原图像做卷积运算，达到模糊图像的目的。

N维空间正态分布方程为：


ISO感光度是CCD/CMOS（或胶卷）对光线的敏感程度

本文沿着Lowe的步骤，参考Rob Hess及Andrea Vedaldi源码，详解SIFT算法的实现过程。


如图2.3所示，使用二维的高斯模板达到了模糊图像的目的，但是会因模板矩阵的关系而造成边缘图像缺失(2.3 b,c)，越大，缺失像素越多,丢弃模板会造成黑边(2.3 d)。更重要的是当变大时，高斯模板(高斯核)和卷积运算量将大幅度提高。根据高斯函数的可分离性，可对二维高斯模糊函数进行改进。

高斯函数的可分离性是指使用二维矩阵变换得到的效果也可以通过在水平方向进行一维高斯矩阵变换加上竖直方向的一维高斯矩阵变换得到。从计算的角度来看，这是一项有用的特性，因为这样只需要次计算，而二维不可分的矩阵则需要次计算，其中，m,n为高斯矩阵的维数，M,N为二维图像的维数。

另外，两次一维的高斯卷积将消除二维高斯矩阵所产生的边缘。(关于消除边缘的论述如下图2.4所示， 对用模板矩阵超出边界的部分——虚线框，将不做卷积计算。如图2.4中x方向的第一个模板1*5，将退化成1*3的模板，只在图像之内的部分做卷积。)

