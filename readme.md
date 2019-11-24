### 目标
看了这么诱人的目标，大家一定流出口水。
![slam_1_1.jpg](https://upload-images.jianshu.io/upload_images/8207483-f705f09a3622a162.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 3D 室内漫游 demo
- 无人驾驶的 demo
### 心态
还是上面那碗红烧肉，虽然看起来好吃，不过首先得确定我们吃得下，然后再确定一下消化得了。学习 SLAM 是一个比较困难的事，是因为 SLAM 不但有深度而且有广度。不过有付出就会有回报，这年头凭自己真本事吃猪肉也是值得自豪的事。
### 什么是SLAM
SLAM(Simultaneous Localization And Mapping)
机器处于未知环境通过传感器和摄像头设备进行定位，然后将自己所处环境进行
同时定位与建图、同时定位与地图构建
- 我在哪里 localization
- 我所处环境 mapping
- 到达指定地点 Route Planning
### SLAM 应用
- 机器人，我们熟知的扫地机器人，一直想买一个,2DLiDAR SLAM
- 无人驾驶，这个大家可能没想到会用 SLAM
- 军事上应用，反恐设备，SLAM 技术最早就是源于军事应用
- 物流仓库（AGV)，亚马逊无人
- 室内全景漫游和虚拟装修，贝壳
- 模型重建
- VR 游戏
- 估计特斯拉无人工厂也会用到 SLAM 技术
- 视频特效


### SLAM VS GPS
有些场景是 GPS 不是办不到就是办到了也不是我们想要的
- GPS 精度不够，民用都是 m 级别，我们在无人驾驶需要 cm 级别的定位
- GPS 在室内是没有信号，例如我们水下和隧道作业中是无法通过 GPS 进行定位
- SLAM 可以进行复杂定位，不但定位而且包含姿态信息

### 为什么我们选择学习 SLAM
- 学习成本不高，只要我们有一部手机和摄像机
- 他是一个面向未来的技术

### SLAM 技术框架
- 传感器数据(可以摄像头，也可以激光雷达)
    - 激光传感器 精度高就是价格贵，信息有限
    - 视觉，单目相机、双目相机和RGB-D相机，全景相机，便宜，体积小，信息丰富 
- 视觉里程计(前端)
可以记录里程计也就是轨迹，这里主要使用特征点提取，边角的点，
    - 特征点提取
    - 特征点匹配
- 优化位姿（后端)
    - 优化走过轨迹
- 建图，有了位置和特征点就可以进行建图
- 回环检测
    - 去过以前去过的地方
### 如何学习SLAM
- 线性代数
- 梯度下降
- 编程环境(linux),了解ubuntu 系统
- cmake
- openCV /g2o 等库
- 传感器类型
- 相机模型
- 特征点 ，SHIF 
- 