### 目标
- 了解相机成像原理
- 熟悉相机结构
- 熟悉相机参数

### 照相机是如何成像
![屏幕快照 2019-11-28 上午5.57.26.png](https://upload-images.jianshu.io/upload_images/8207483-15e878218af31f3f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
假设我们现在有一个张胶片，我们想要这个树拍摄到胶片上，我们把树划分成点，然后将这些点一一记录到胶片上，但是每一个点发出光线都是四面八方的，这些点光线会到达胶片上每一个地方，而且概率是均等的。翻过说也就是胶片上每一个点都可以接受树树每一个发生过来光线。这样结构是无法成像。

![camer_1_1.jpeg](https://upload-images.jianshu.io/upload_images/8207483-e938e8a6b9e340a7.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这时候我们在胶片和树之间放置障碍物，然后做一个小孔，这就是小孔成像原理。这样就保证了树每一个点发生光线到胶片上唯一点，中间孔就是**光圈**，其实这样过程就是将 3D 场景转化为 2D 图片。

 3维压缩为 2维胶片上。从而也就丢失距离信息。角度信息的就是丢失，并行关系也没有被保留，长度也发生变化了

![camera_2_1.jpg](https://upload-images.jianshu.io/upload_images/8207483-d7365cd9f54e08e3.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

针孔相机实现

![camera_2_2.jpeg](https://upload-images.jianshu.io/upload_images/8207483-34d96b795fbf8964.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![camera_2_3.jpg](https://upload-images.jianshu.io/upload_images/8207483-4c6779e379ba9815.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
自制针孔相机,因为我们自己做的针孔相机虽然我们已经把孔控制得很小，但是还是会得到一张模糊图片，这是因为因为孔虽然小但是比起光线还是无法控制物体上点发射光线是只允许一条通过。因为当一个点发出多条光线经过小孔投射到胶片上就是一个光斑，因此图像变得模糊。如果孔太小那么问题需要很长时间曝光才能成像。如果你的孔做足够小，小到光波长不能被忽略时候，就会发生干涉现象。这样图像就会变得再次模糊。大家自己可以自己做一个。

在现实生活中相机大家会发现没有是针孔相机

![camera_2_5.jpg](https://upload-images.jianshu.io/upload_images/8207483-da64168adfceee5d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



我们在 SLAM 中需要通过

## 照相机的结构
物体每一个点发出光线都会投射到平面（胶片）上任意位置，这样最终胶片是无法成像的。
针孔照相机，这里针孔不是偷拍的针孔照相机，而是一个经典的照相机模型。通过物体和胶片间的障碍物上小孔，可以保证物体上每一个点都对应胶片上的一点。这个小孔就是我们熟悉**光圈**。其实小孔成像本质是将 3维压缩为 2维胶片上。从而也就丢失距离信息。角度信息的就是丢失，看到相互，并行关系被破坏，长度也发生变化了。所以我们需要通过学习将这些变形和错觉进行还原。当然我们用照相机都不是针孔相机，这是因为如果针孔过大，图像就会blur。如果孔太小那么问题需要很长时间曝光才能成像。可以用一个凸透镜来将到达镜面都聚到一点。凸透镜也会将点散开到小圆。 $$\frac{1}{d_0} + \frac{1}{d_1} = \frac{1}{f}$$
$d_0$ 为物体的到凸透镜距离，$d_1$ 表示成像平面（胶片）到凸透镜的距离。f 表示焦距。存在这么一个公式就可以满足在$d_0$ 位置的物体在 $d_1$ 平面上成像最佳（清晰）。
### 光圈
控制进光的量，光圈就是开孔大小来控制进入光，可以控制景深。一旦光圈开大的就会缩小清晰区域。光圈也就是（depth field)就会变大，一些物体的散射不会那么严重，有时候我们需要大光圈得到背景发虚。小光圈带来问题曝光时间。
f 对于定焦的focal length 是不变，我们只会调整 aperture。
小光圈也会影响快门时间。小光圈的曝光时间可能会引起运动模糊。
### 焦距
(Field of View)
同一位置相机用不同焦距，28mm Field of View 就变小，85mm 时候的 Field of view 也就是只有 28度视野，每一个物体在通常尺寸的胶片上像素也就是越多，
$$\phi = tan^{-1}( \frac{d}{2f})$$
尝试对对相机进行建模
## 针孔照相机
针孔摄像机是计算机视觉中广泛使用的照相机模型，这是因为模型简单且能够提供足够的精度。在针孔照相机模型中，在光线投射到图像平面之前，仅从一个点（孔）经过，也就是照相机模型中。
（图，针孔照相机模型）