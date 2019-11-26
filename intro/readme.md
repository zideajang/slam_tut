最近看了SLAM 虽然应用范围很广但是介绍 SLAM 的无论是书籍还是视频都是少之又少，这也给我们学习SLAM 带来困难。
#### 什么是SLAM 问题

那么我们在看一看 SLAM 问题是什么样的问题解决以及我们如何解决问题，有问题就有已知条件，然后我们根据已知条件来找答案，那么什么是已知条件呢?
- 机器控制信息，例如机器人控制信息或者是驾驶车辆速度
- 以及通过传感器（雷达或摄像机）获得环境观察信息

然后我们求解的是什么呢?求解就是定位和地图构建。

当我们身处一个陌生的环境，我们是如何熟悉环境确定自己在环境中位置。在探索我们并不了解的陌生环境，我们是如何熟悉环境和搜寻目标呢?其实这就是 SLAM 所做的事情，我们通常会边走边留心周围环境，记住看到一些标志性建筑或者是特殊的标识，来作为自己位置的参照。通过这些来确定我们的位置，然后根据自己看到来在脑海中形成地图。
而且我们可以走过程中根据自己步长来估计距离，而且我们眼睛看到估计标志物离我们距离也是有很大误差，因为这些误差我们是无法得到估计出自己精确的定位的。

![slam_2_1.jpeg](https://upload-images.jianshu.io/upload_images/8207483-cceb02de6a103d93.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- X 表示实际位置
- k 表示时刻那么 $X_k$ 表示 k 时刻所处位置(黄色三角，这里位置信息包括姿态，三角表示进行方向)
- 虚线的路径表示我们估计位置，我们需要缩小估计位置和实际位置的差
- 星型表示参照物（landmarkder)
- 红色带箭头
这些点我们在时间的离散的位置点，开始估计

#### 总结一下
- 估计(Prediction)
    - predict our location using compass and steps
- 观察(Observation)
    - 观察周围环境表示点
    - remember the location
- 校正(Correction)
    - Use what we have seen before to correct our location
- 绘制(Mapping)
    - 更新修正之前观察点表示点
    - 绘制新的标识点

what is Robot Mapping
- Robot equiptment with sensor 里程计 摄像机和雷达
- Mapping 对环境进行建模，表示环境，来做出自己决策

术语

- state estimation(贝叶斯过滤器)
- localization (x,y以及姿态)
- mapping
- SLAM 估计环境状态
- Navigation 导航并不是我们在 SLAM 讨论范围，
- Motion Planning 与导航紧密相关概念

### Full SLAM 和 Online SLAM
- Full SLAM
- Online SLAM
### 定义 SLAM 问题模型
#### 已知条件
- 机器人控制信息，这些控制信息可能速度，控制机器人转向，我们这里拿无人驾驶，我们通过油门、方向盘和刹车这些我们对汽车下的指令都是控制可以按不同时刻进行划分。这些数据例如速度和里程计汽车都会返回给我们，现在电子设备在汽车快速发展，我们通过汽车电子系统提供的接口可以得到足够信息
$$u_{1:T} = \{u_1,u_2,\dots , u_{T}\}$$
- 观察数据
可能这些数据可能是雷达返回数据，也可能是摄像头返回的图片信息
$$z_{1:T} = \{z_1,z_2,\dots , z_{T}\}$$
#### 求解 
- 环境模型
    m
- 机器人移动轨迹
大家可能发现其他时序相关的变量都是从 1 开始，而 x 是从 0 开始这是因为我们机器人是有初始位置的，所以这里用 0 来表示
$$x_{0:T} = \{x_1,x_2,\dots , x_{T}\}$$

??? audiometry 听力测定 odometry 测距法

### 似然估计方法在 SLAM 应用(Probailistic Approaches)
我们因为位置和观察点位置误差，我们在某一个时刻无法确定机器人准确位置，我们可以给出一个概率分布来代替确定机器人准确的位置。
即使我们设备很精确，可以精确到厘米或者更小的数量级，但是误差还是不可避免而且，这误差是会不断积累，在一个长距离运动后误差可能就会影响我们判断了。
- 在机器人运动和观察的不确定性
- Uncertainty in the robot's motions and observations
- 使用似然估计来描述和解释这些不确定性

我们会用贝叶斯过滤器
$$ p(x_{0:T} , m | z_{1:T}, u_{1:T})$$

- path
- p distribution
- map
- given
- observations
- controls
用不同计算，我们表示，dense ,multimodal distribution
估计，假设

整个 SLAM 过程都是估计 考虑计算量 

investigation full slam graphical models ,briefly variable name obser entri arrow dependencs means influences x_t x_{t-1} we have previous post influence commands estimate meter forward quite hight likehood what world like and where i am where good estimateof what i am going to measure landmarks in the world map should world look like itself estimate other variables quantities ilustrating independences estimate ,通过用带有箭头线表示变量之间关系我们可以很好进行计算，这一点tensorflow 也是在用图计算。
