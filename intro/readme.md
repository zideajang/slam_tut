最近看了SLAM 虽然应用范围很广但是介绍 SLAM 的无论是书籍还是视频都是少之又少，这也给我们学习 SLAM 带来困难。
#### SLAM 定义
SLAM是同步定位与地图构建(Simultaneous Localization And Mapping)的缩写，最早由Hugh Durrant-Whyte 和 John J.Leonard提出。SLAM主要用于解决移动机器人在未知环境中运行时定位导航与地图构建的问题。


#### 术语
在我们开始对一些术语进行介绍，说明帮助理解经常在分享中出现的术语。

- **状态估计**(state estimation) 是机器人对位置环境的估计，包括对地标位置进行估计，这里可能用到似然估计，通过正态分布概率模型来推测地标位置
- **定位**(localization) 在SLAM 问题中定位包括坐标以及机器人运动方向
- **构建**(mapping) 通过对地标估计，提取特征点然后通常是进行稀疏建模，不过向 3D 漫游我们就需要稠密的点来构建环境
- SLAM
- **导航**(Navigation) 导航并不是我们在 SLAM 讨论范围，但是导航是依赖于SLAM。
- 路径规划(Motion Planning) 与导航紧密相关概念

#### 什么是SLAM 问题
那么我们在看一看 SLAM 问题是什么样的问题解决以及我们如何解决问题，有问题就有已知条件，然后我们根据已知条件来找答案，那么什么是已知条件呢?
- 机器控制信息，例如机器人控制信息或者是驾驶车辆速度
- 以及通过传感器（雷达或摄像机）获得环境观察信息

然后我们求解的是什么呢?求解就是定位和地图构建。

#### 人类是如何探索未知环境

当我们身处一个陌生的环境，我们是如何熟悉环境确定自己在环境中位置。在探索我们并不了解的陌生环境，我们是如何熟悉环境和搜寻目标呢?其实这就是 SLAM 所做的事情，我们通常会边走边留心周围环境，记住看到一些标志性建筑或者是特殊的标识，来作为自己位置的参照。通过这些来确定我们的位置，然后根据自己看到来在脑海中形成地图。
而且我们可以走过程中根据自己步长来估计距离，而且我们眼睛看到估计标志物离我们距离也是有很大误差，因为这些误差我们是无法得到估计出自己精确的定位的。
###### 我们认知未知环境
- 估计(Prediction)
    - predict our location using compass and steps
- 观察(Observation)
    - 观察周围环境表示点
    - 并且记住自己位置
- 校正(Correction)
    - 利用我们看到地标来纠正位置
- 绘制(Mapping)
    - 更新修正之前观察点表示点
    - 绘制新的标识点

#### 机器人是如何探索未知环境

![slam_2_1.jpeg](https://upload-images.jianshu.io/upload_images/8207483-cceb02de6a103d93.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

机器人来到未知环境，通过对自己定位和对环境进行构建来认知陌生环境，整个流程类似于人类认知未知环境。

- X 表示实际位置
- k 表示时刻那么 $X_k$ 表示 k 时刻所处位置(黄色三角，这里位置信息包括姿态，三角表示进行方向)
- 虚线的路径表示我们估计位置，我们需要缩小估计位置和实际位置的差
- 星型表示参照物（landmarkder)
- 红色带箭头
这些点我们在时间的离散的位置点，开始估计

从一个已知坐标点出发，根据位置推测周围地标坐标点，然后来到一下个时刻 k 根据速度和方向来推测直接位置，然后根据再推测周围地标位置。

![slam_2_2.jpeg](https://upload-images.jianshu.io/upload_images/8207483-75ce6d74c1e276d3.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

图中箭头表示，他们之间依赖关系，例如在 k 时刻 x 是依赖于前一时刻 k - 1 的坐标和在 k 时刻控制量，然后我们在 k 时刻的观测 z 是依赖于 k 时刻位置，m 表示地图他是依赖所有观测点。

图上箭头

#### SLAM 问题的难点
SLAM 难点就是机器身处一个一无所知的环境，我们需要估计其位置和用于判断位置的周围环境。也就是我们的方程需要相互作为已知条件来确定对方情况下都是未知条件
![屏幕快照 2019-11-27 上午5.03.55.png](https://upload-images.jianshu.io/upload_images/8207483-2089e78b6758c184.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 我们初始位置观察左右两个地标，然后估计其位置，蓝色圈表示我们根据高斯分布会估计出坐标点位置的概率分布范围，也就是地标可能出现位置范围
2. 然后来到下一个位置，这样我们位置也是根据控制速度估计出来的带有一定误差。同时观察地标也误差也会随之增加。这两个地标位置不确定现在不仅源于其本身还源于机器人在 2 的不确定
3. 有意思事情发生在机器人 3 位置，在 3 时候机器人重新观察到图上面在 2 时刻已经观察过地标，这样就会给地标带来更多定位信息，那么地标不确定就会相应缩小到黑色圈范围，因为在 2 时刻机器人定位也依赖于此地标那么他的位置取值范围与会缩小，他位置精确了同时以带来 3 位置机器位置定位范围缩小。

也正是相互依赖关系给 SLAM 计算带来了难度。我们无法单独对某一个对象进行估计，一切都是相关的。

在上图 3 时刻我们重新观察到在 2 时刻地标点，如何判别这些点同一个地标点对机器也是一个难题
观察点数据的选择可能带来更多不确定性

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

#### 观察模型

#### 运动模型


### 似然估计方法在 SLAM 应用(Probailistic Approaches)
我们因为位置和观察点位置误差，我们在某一个时刻无法确定机器人准确位置，我们可以给出一个概率分布来代替确定机器人准确的位置。
即使我们设备很精确，可以精确到厘米或者更小的数量级，但是误差还是不可避免而且，这误差是会不断积累，在一个长距离运动后误差可能就会影响我们判断了。
- 在机器人运动和观察的不确定性
- Uncertainty in the robot's motions and observations
- 使用似然估计来描述和解释这些不确定性

我们会用贝叶斯过滤器
$$ p(x_{0:T} , m | z_{1:T}, u_{1:T})$$

- p 表示分布
- $x_T$ 表示轨迹
- m 表示地图
- $z_T$ 表示观察地标
- u 表示控制
用不同计算，我们表示，dense ,multimodal distribution
估计，假设

整个 SLAM 过程都是估计 考虑计算量 

