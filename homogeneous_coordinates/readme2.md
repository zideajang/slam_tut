摄像头是将 3D 压缩为 2D 平面，压缩过程会损失一些位置、角度以及一些平行关系。在 SLAM 我们需要将这些压缩过 2D 图像进行还原来重新构建3D 的地图模型。

图像用的变换模型(可以理解手段或者方式)有如下几种
- 刚性变换
- 仿射变换
- 透视变换
- 非线形变换

Harris 

SIFT
这是 SLAM 一个关键技术，特别在使我们是使用摄像头作为传感器来识别环境时候我们都会用到 SIFT 特征点检查。一些地标都是通过 SIFT 来进行检查
要想很好使用 SIFT

我们是怎么识别物体的呢? 无论物体离我们远近，无论物体是否模糊。我们都能很容地认出物体，当然也想让机器具有我们这样能力，在不同环境都能快速容易识别出物体。这就需要对我们认识物体过程进行建模。找到那些物体特征，这些特征可以帮助我们对其进行识别，并且这些特征不会因环境而改变。

从上面的图像来看，很明显我们不能使用同一个窗口来检测不同尺度的关键点。小角落也可以。但是为了探测更大的角落，我们需要更大的窗户。为此，使用比例空间过滤。其中，对于不同 sigma 值的图像，找到高斯拉普拉斯。LoG充当blob检测器，检测由于sigma变化而产生的各种大小的blob。简而言之，西格玛是一个缩放参数。例如，在上面的图像中，具有低sigma的高斯核对于小角点给出高值，而具有高sigma的高斯核对于大角点则很适合。因此，我们可以找到在尺度和空间上的局部极大值，它给出了一个（x，y，σ）值的列表，这意味着在σ尺度上存在（x，y）的一个潜在的关键点。
但是这个日志有点昂贵，所以SIFT算法使用Gaussians的差值，它是日志的近似值。高斯差是指两个不同sigma图像的高斯模糊差，设为sigma和k sigma。这个过程是针对高斯金字塔中图像的不同倍频程进行的。如下图所示：

在最后几章中，我们看到了一些角点检测器，如 Harris等，是旋转不变的，这意味着即使图像旋转，我们也可以找到相同的角点。这是显而易见的，因为角仍然是旋转图像中的角。但是缩放呢？如果缩放图像，则角点可能不是角点。例如，检查下面的简单图像。在同一窗口中缩放时，小窗口中的小图像中的角是平的。所以 Harris 角不是标度不变的。
