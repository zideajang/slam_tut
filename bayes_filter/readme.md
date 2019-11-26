### state Estimation

### Goal
Estimate the state x of a system given observations z and controls u

$$p(x|z,u)$$

$$\begin{aligned}
    bel(x_t) = p(x_t|z_{1:t},u_{1:t}) \\
    = \eta p(z_t|x_t,z_{1:t},u_{1:t})p(x_t|z_{1:t},u_{1:t}) \\
    =\eta p(z_t|x_t)p(x_t|z_{1:t},u_{1:t}) \\
    =\eta p(z_t|x_t) \int_{x_{t-1}} p(x_t|x_{t-1},z_{1:t-e},u_{1:t})
\end{aligned}$$
- x 姿态(位置和方向)
- u 控制(速度)
- z 表示观察
  


pea distribution Bayse rule to estimate 
Kalman filter algorithm 

$$bel(x_t) = p(x_t|z_{1:t},u_{1:t})$$

Markov assumption

law of total probability
$$P(A) = \int_B P(A|B) \cdot P(B) dB$$
$$ P(A) =  \sum_B P(A|B) P(B)$$