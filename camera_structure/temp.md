
现在解释一下有关 y-axis 显示 1-4 而 x-axis 显示 0-3 原因
如果为 plot（）命令提供单个列表或数组，matplotlib 是一个 y 值序列，并自动为生成 x 值。
在 python 取值范围是 0 开始这个和其他语言没有任何区别，默认 x 向量的长度与 y 相同，这也是 x 数据是[0,1,2,3]。

```
def draw_line():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('draw line')

def draw_line_2():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.ylabel('draw line 2')
```
plot 前两个参数对应于每个点的 x，y , 而第三个参数是可选的，是表示绘图颜色和线型。
使用的字母和符号来自 MATLAB，可以将表示颜色与线条样式的文字连接起来使用。
默认格式为 "b-"，表示一条蓝色实线。例如，要用红色圆圈绘制上述内容，您可以

```
def draw_points():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
  def draw_points_2():
    t = np.arange(0., 5., 0.2)

    # 红色虚线, 蓝色方块和绿色三角形
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()
D:\ml\basic_ml_tut\matplotlib_tut\screenshots
```
有些情况下，数据的格式允许您使用字符串访问特定变量。例如，使用 numpy.recarray 或 pandas.DataFrame。
Matplotlib 允许您使用data关键字参数提供这样的对象。如果提供，则可以使用与这些变量对应的字符串生成绘图。
```
def draw_points_3():
    data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()
```