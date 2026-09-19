---
title: "磁镜为什么能够产生沿磁力线方向的反射力？"
date: 2026-09-17T08:44:00+08:00
draft: false
description: "从柱坐标下的磁场散度出发，逐步推导磁镜轴线附近的径向磁场分量，并进一步得到沿磁力线方向的磁镜力。"
categories: []
tags: []
math: true
showToc: true
---

> 本文由 2026-09-17 的手写笔记整理而来。整理原则是：原稿中正确且已经展开的步骤全部保留；原稿中存在跳步的地方补齐；原稿中不够准确或缺少适用条件的地方补充说明，而不改变原来的推导主线。

## 问题

磁镜为什么能够产生沿磁力线方向的反射力？

已知洛伦兹力

$$
\mathbf F=q\mathbf v\times\mathbf B,
$$

磁场写成柱坐标形式

$$
\mathbf B=B_r\hat{\mathbf r}+B_\theta\hat{\boldsymbol\theta}+B_z\hat{\mathbf z},
$$

以及 Maxwell 方程

$$
\nabla\cdot\mathbf B=0.
$$

下面从一个很小的柱坐标体元开始。

![原手稿中的柱坐标微小体元](cylindrical-volume-element.png)

*图 1　原手稿中的柱坐标微小扇形体元，标出了 $d\theta$、$dr$ 和 $dz$。*

体元的范围为

$$
r\to r+dr,\qquad
\theta\to\theta+d\theta,\qquad
z\to z+dz.
$$

三个方向上的微小长度分别为

$$
dr,\qquad r\thinspace{}d\theta,\qquad dz.
$$

因此体积近似为

$$
dV=r\thinspace{}dr\thinspace{}d\theta\thinspace{}dz.
$$

现在计算这个体元六个面的净流出磁通。

## 磁通的基本形式

磁通微元为

$$
d\Phi=\mathbf B\cdot\hat{\mathbf n}\thinspace{}dA,
$$

其中 $dA$ 是面元面积，$\hat{\mathbf n}$ 是该面的外法向。

## 径向两个面的磁通

![原手稿中的径向面示意](volume-element-radial-face.png)

*图 2　原手稿中用于分析径向两个面的体元示意。*

### 位于 $r$ 处的内侧面

这个面的面积为

$$
dA_{r,\mathrm{in}}=r\thinspace{}d\theta\thinspace{}dz.
$$

内侧面的外法向是 $-\hat{\mathbf r}$，因此

$$
d\Phi_{r,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\mathbf r})
\thinspace{}r\thinspace{}d\theta\thinspace{}dz.
$$

把磁场完整展开：

$$
\mathbf B\cdot(-\hat{\mathbf r})
=
\left(
B_r\hat{\mathbf r}
+
B_\theta\hat{\boldsymbol\theta}
+
B_z\hat{\mathbf z}
\right)
\cdot(-\hat{\mathbf r}).
$$

逐项点乘：

$$
\mathbf B\cdot(-\hat{\mathbf r})
=
-B_r(\hat{\mathbf r}\cdot\hat{\mathbf r})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\mathbf r})
-B_z(\hat{\mathbf z}\cdot\hat{\mathbf r}).
$$

由于柱坐标三个单位基矢两两正交，

$$
\hat{\mathbf r}\cdot\hat{\mathbf r}=1,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\mathbf r}=0,
\qquad
\hat{\mathbf z}\cdot\hat{\mathbf r}=0,
$$

所以

$$
\mathbf B\cdot(-\hat{\mathbf r})=-B_r.
$$

于是

$$
\boxed{
d\Phi_{r,\mathrm{in}}
=
-B_r(r,\theta,z)\thinspace{}r\thinspace{}d\theta\thinspace{}dz
}.
$$

### 位于 $r+dr$ 处的外侧面

这个面的面积为

$$
dA_{r,\mathrm{out}}
=
(r+dr)d\theta\thinspace{}dz.
$$

在 $r+dr$ 处，磁场是

$$
\mathbf B(r+dr,\theta,z),
$$

外法向为 $+\hat{\mathbf r}$，所以

$$
d\Phi_{r,\mathrm{out}}
=
\mathbf B(r+dr,\theta,z)\cdot\hat{\mathbf r}
\thinspace{}(r+dr)d\theta\thinspace{}dz.
$$

同样把点乘完整展开：

$$
\begin{aligned}
\mathbf B(r+dr,\theta,z)\cdot\hat{\mathbf r}
&=
\left[
B_r(r+dr,\theta,z)\hat{\mathbf r}
+
B_\theta(r+dr,\theta,z)\hat{\boldsymbol\theta}
+
B_z(r+dr,\theta,z)\hat{\mathbf z}
\right]\cdot\hat{\mathbf r}\\
&=
B_r(r+dr,\theta,z)(\hat{\mathbf r}\cdot\hat{\mathbf r})
+
B_\theta(r+dr,\theta,z)(\hat{\boldsymbol\theta}\cdot\hat{\mathbf r})
+
B_z(r+dr,\theta,z)(\hat{\mathbf z}\cdot\hat{\mathbf r})\\
&=
B_r(r+dr,\theta,z).
\end{aligned}
$$

因此

$$
\boxed{
d\Phi_{r,\mathrm{out}}
=
B_r(r+dr,\theta,z)(r+dr)d\theta\thinspace{}dz
}.
$$

### 两个径向面的净流出

$$
d\Phi_r
=
d\Phi_{r,\mathrm{out}}
+
d\Phi_{r,\mathrm{in}}.
$$

代入两面的磁通：

$$
d\Phi_r
=
\left[
(r+dr)B_r(r+dr,\theta,z)
-
rB_r(r,\theta,z)
\right]d\theta\thinspace{}dz.
$$

定义

$$
f(r)=rB_r(r,\theta,z),
$$

于是

$$
d\Phi_r
=
[f(r+dr)-f(r)]d\theta\thinspace{}dz.
$$

根据导数定义，

$$
\frac{df}{dr}
=
\lim_{\Delta r\to0}
\frac{f(r+\Delta r)-f(r)}{\Delta r}.
$$

因为这里的 $dr$ 是无穷小量，可以写成一阶近似

$$
\frac{f(r+dr)-f(r)}{dr}
\approx
\frac{df}{dr},
$$

所以

$$
f(r+dr)-f(r)
\approx
\frac{df}{dr}dr.
$$

这里 $f$ 实际来自多变量函数 $rB_r(r,\theta,z)$，在变化 $r$ 时把 $\theta,z$ 固定，因此应写成偏导数：

$$
f(r+dr)-f(r)
\approx
\frac{\partial[rB_r(r,\theta,z)]}{\partial r}dr.
$$

所以

$$
\boxed{
d\Phi_r
=
\frac{\partial(rB_r)}{\partial r}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$

## $\theta$ 方向两个面的磁通

原稿在这里继续重复同样的投影过程。虽然形式和径向面相似，但仍然完整保留。

### 位于 $\theta$ 处的内侧面

这个面的两条边分别是 $dr$ 和 $dz$，所以

$$
dA_\theta=dr\thinspace{}dz.
$$

该面的外法向是 $-\hat{\boldsymbol\theta}$，因此

$$
d\Phi_{\theta,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\boldsymbol\theta})
\thinspace{}dr\thinspace{}dz.
$$

展开磁场：

$$
\mathbf B\cdot(-\hat{\boldsymbol\theta})
=
\left(
B_r\hat{\mathbf r}
+
B_\theta\hat{\boldsymbol\theta}
+
B_z\hat{\mathbf z}
\right)
\cdot(-\hat{\boldsymbol\theta}).
$$

逐项点乘：

$$
\mathbf B\cdot(-\hat{\boldsymbol\theta})
=
-B_r(\hat{\mathbf r}\cdot\hat{\boldsymbol\theta})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta})
-B_z(\hat{\mathbf z}\cdot\hat{\boldsymbol\theta}).
$$

利用

$$
\hat{\mathbf r}\cdot\hat{\boldsymbol\theta}=0,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta}=1,
\qquad
\hat{\mathbf z}\cdot\hat{\boldsymbol\theta}=0,
$$

得到

$$
\mathbf B\cdot(-\hat{\boldsymbol\theta})=-B_\theta.
$$

因此

$$
\boxed{
d\Phi_{\theta,\mathrm{in}}
=
-B_\theta(r,\theta,z)\thinspace{}dr\thinspace{}dz
}.
$$

### 位于 $\theta+d\theta$ 处的外侧面

另一面位于 $\theta+d\theta$，外法向为 $+\hat{\boldsymbol\theta}$：

$$
d\Phi_{\theta,\mathrm{out}}
=
\mathbf B(r,\theta+d\theta,z)\cdot\hat{\boldsymbol\theta}
\thinspace{}dr\thinspace{}dz.
$$

展开点乘：

$$
\begin{aligned}
\mathbf B(r,\theta+d\theta,z)\cdot\hat{\boldsymbol\theta}
&=
\left[
B_r\hat{\mathbf r}
+
B_\theta(r,\theta+d\theta,z)\hat{\boldsymbol\theta}
+
B_z\hat{\mathbf z}
\right]\cdot\hat{\boldsymbol\theta}\\
&=
B_r(\hat{\mathbf r}\cdot\hat{\boldsymbol\theta})
+
B_\theta(r,\theta+d\theta,z)
(\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta})
+
B_z(\hat{\mathbf z}\cdot\hat{\boldsymbol\theta})\\
&=
B_\theta(r,\theta+d\theta,z).
\end{aligned}
$$

所以

$$
\boxed{
d\Phi_{\theta,\mathrm{out}}
=
B_\theta(r,\theta+d\theta,z)\thinspace{}dr\thinspace{}dz
}.
$$

### 两个 $\theta$ 面的净流出

$$
d\Phi_\theta
=
d\Phi_{\theta,\mathrm{out}}
+
d\Phi_{\theta,\mathrm{in}},
$$

所以

$$
d\Phi_\theta
=
\left[
B_\theta(r,\theta+d\theta,z)
-
B_\theta(r,\theta,z)
\right]dr\thinspace{}dz.
$$

和前面一样，把其他变量固定，只考察 $\theta$ 的变化：

$$
B_\theta(\theta+d\theta)-B_\theta(\theta)
\approx
\frac{\partial B_\theta}{\partial\theta}d\theta.
$$

因此

$$
\boxed{
d\Phi_\theta
=
\frac{\partial B_\theta}{\partial\theta}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$

## $z$ 方向两个面的磁通

![原手稿中的上下表面与外法向](volume-element-normal-directions.png)

*图 3　原手稿中上下表面及其外法向的示意。*

### 位于 $z$ 处的底面

底面的两条边分别为 $dr$ 和 $r\,d\theta$，所以

$$
dA_z
=
r\thinspace{}dr\thinspace{}d\theta.
$$

底面的外法向是 $-\hat{\mathbf z}$，因此

$$
d\Phi_{z,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\mathbf z})
\thinspace{}r\thinspace{}dr\thinspace{}d\theta.
$$

展开点乘：

$$
\mathbf B\cdot(-\hat{\mathbf z})
=
\left(
B_r\hat{\mathbf r}
+
B_\theta\hat{\boldsymbol\theta}
+
B_z\hat{\mathbf z}
\right)
\cdot(-\hat{\mathbf z}),
$$

即

$$
\mathbf B\cdot(-\hat{\mathbf z})
=
-B_r(\hat{\mathbf r}\cdot\hat{\mathbf z})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\mathbf z})
-B_z(\hat{\mathbf z}\cdot\hat{\mathbf z}).
$$

由于

$$
\hat{\mathbf r}\cdot\hat{\mathbf z}=0,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\mathbf z}=0,
\qquad
\hat{\mathbf z}\cdot\hat{\mathbf z}=1,
$$

所以

$$
\mathbf B\cdot(-\hat{\mathbf z})=-B_z.
$$

因此

$$
\boxed{
d\Phi_{z,\mathrm{in}}
=
-B_z(r,\theta,z)\thinspace{}r\thinspace{}dr\thinspace{}d\theta
}.
$$

### 位于 $z+dz$ 处的顶面

顶面的外法向是 $+\hat{\mathbf z}$：

$$
d\Phi_{z,\mathrm{out}}
=
\mathbf B(r,\theta,z+dz)\cdot\hat{\mathbf z}
\thinspace{}r\thinspace{}dr\thinspace{}d\theta.
$$

展开点乘：

$$
\begin{aligned}
\mathbf B(r,\theta,z+dz)\cdot\hat{\mathbf z}
&=
\left[
B_r\hat{\mathbf r}
+
B_\theta\hat{\boldsymbol\theta}
+
B_z(r,\theta,z+dz)\hat{\mathbf z}
\right]\cdot\hat{\mathbf z}\\
&=
B_r(\hat{\mathbf r}\cdot\hat{\mathbf z})
+
B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\mathbf z})
+
B_z(r,\theta,z+dz)(\hat{\mathbf z}\cdot\hat{\mathbf z})\\
&=
B_z(r,\theta,z+dz).
\end{aligned}
$$

所以

$$
\boxed{
d\Phi_{z,\mathrm{out}}
=
B_z(r,\theta,z+dz)\thinspace{}r\thinspace{}dr\thinspace{}d\theta
}.
$$

### 两个 $z$ 面的净流出

$$
d\Phi_z
=
d\Phi_{z,\mathrm{out}}
+
d\Phi_{z,\mathrm{in}},
$$

所以

$$
d\Phi_z
=
\left[
B_z(r,\theta,z+dz)
-
B_z(r,\theta,z)
\right]
r\thinspace{}dr\thinspace{}d\theta.
$$

根据前面相同的有限差分近似，

$$
B_z(r,\theta,z+dz)-B_z(r,\theta,z)
\approx
\frac{\partial B_z}{\partial z}dz.
$$

因此

$$
\boxed{
d\Phi_z
=
r\frac{\partial B_z}{\partial z}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$

## 从三个方向的磁通得到柱坐标散度

六个面的总净流出磁通为

$$
d\Phi
=
d\Phi_r+d\Phi_\theta+d\Phi_z.
$$

代入三个方向的结果：

$$
\begin{aligned}
d\Phi
&=
\frac{\partial(rB_r)}{\partial r}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz\\
&\quad+
\frac{\partial B_\theta}{\partial\theta}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz\\
&\quad+
r\frac{\partial B_z}{\partial z}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz.
\end{aligned}
$$

把公共的体积微元部分提出来：

$$
d\Phi
=
\left[
\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_\theta}{\partial\theta}
+
r\frac{\partial B_z}{\partial z}
\right]
dr\thinspace{}d\theta\thinspace{}dz.
$$

散度的定义是

$$
\nabla\cdot\mathbf B
=
\lim_{dV\to0}
\frac{\text{净流出磁通}}{\text{体积}}.
$$

对于当前微小体元，

$$
dV=r\thinspace{}dr\thinspace{}d\theta\thinspace{}dz,
$$

因此

$$
\nabla\cdot\mathbf B
=
\frac{d\Phi}{dV}.
$$

把 $d\Phi$ 和 $dV$ 都代进去：

$$
\nabla\cdot\mathbf B
=
\frac{
\left[
\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_\theta}{\partial\theta}
+
r\frac{\partial B_z}{\partial z}
\right]
dr\thinspace{}d\theta\thinspace{}dz
}{
r\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$

约去公共因子 $dr\,d\theta\,dz$：

$$
\boxed{
\nabla\cdot\mathbf B
=
\frac1r
\left[
\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_\theta}{\partial\theta}
+
r\frac{\partial B_z}{\partial z}
\right]
}.
$$

也就是熟悉的形式

$$
\boxed{
\nabla\cdot\mathbf B
=
\frac1r\frac{\partial(rB_r)}{\partial r}
+
\frac1r\frac{\partial B_\theta}{\partial\theta}
+
\frac{\partial B_z}{\partial z}
}.
$$

## 利用磁镜的轴对称性

磁镜绕 $z$ 轴旋转后不变，因此各物理量不依赖 $\theta$。于是

$$
\frac{\partial B_\theta}{\partial\theta}=0.
$$

原稿还另外采用了“没有环向磁场”的设定：

$$
B_\theta=0.
$$

需要区分这两个条件：轴对称性给出的是对 $\theta$ 的偏导为零；$B_\theta=0$ 是额外的磁场结构假设。

于是

$$
\nabla\cdot\mathbf B
=
\frac1r\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_z}{\partial z}.
$$

Maxwell 方程又规定

$$
\nabla\cdot\mathbf B=0,
$$

所以

$$
\boxed{
\frac1r\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_z}{\partial z}
=0
}.
$$

## 由 $\nabla\cdot\mathbf B=0$ 求轴线附近的 $B_r$

由上式，

$$
\frac1r\frac{\partial(rB_r)}{\partial r}
=
-\frac{\partial B_z}{\partial z},
$$

即

$$
\frac{\partial(rB_r)}{\partial r}
=
-r\frac{\partial B_z}{\partial z}.
$$

![原手稿中的磁镜磁力线](magnetic-mirror-field-lines.png)

*图 4　原手稿中的磁镜轴线附近磁力线示意；红线表示靠近轴线的一条参考线。*

原稿在这里说，在靠近红色轴线的区域，$B_z$ 的变化可以近似视为足够缓慢，因此把 $\partial B_z/\partial z$ 当作常量。

更准确地说，这一步真正需要的是：**在轴线附近，对固定的 $z$，$\partial B_z/\partial z$ 对 $r$ 的变化可以忽略到当前的一阶近似。** 轴对称性下，轴线附近可以写成

$$
B_z(r,z)=B_0(z)+O(r^2),
$$

因此

$$
\frac{\partial B_z}{\partial z}
=
\frac{dB_0}{dz}
+
O(r^2).
$$

在保留最低阶项时，可以把 $\partial B_z/\partial z$ 从关于 $r$ 的积分中提出。

为避免积分变量混淆，把积分内部的 $r$ 写成 $r'$：

$$
\int_0^r
\frac{\partial(r'B_r)}{\partial r'}dr'
=
-\frac{\partial B_z}{\partial z}
\int_0^r r'\thinspace{}dr'.
$$

左边直接积分：

$$
\int_0^r
\frac{\partial(r'B_r)}{\partial r'}dr'
=
rB_r(r)-\left.r'B_r(r')\right|_{r'=0}.
$$

在轴线上 $r'=0$，只要 $B_r$ 有限，就有

$$
\left.r'B_r(r')\right|_{r'=0}=0.
$$

右边为

$$
-\frac{\partial B_z}{\partial z}
\int_0^r r'\thinspace{}dr'
=
-\frac{\partial B_z}{\partial z}\frac{r^2}{2}.
$$

所以

$$
rB_r(r)
=
-\frac12r^2\frac{\partial B_z}{\partial z},
$$

最终得到

$$
\boxed{
B_r(r)
=
-\frac r2\frac{\partial B_z}{\partial z}
}.
$$

更严格地说，这是轴线附近的最低阶结果：

$$
B_r(r,z)
=
-\frac r2\frac{dB_0}{dz}
+
O(r^3).
$$

如果沿 $+z$ 方向运动时 $B_z$ 慢慢增大，

$$
\frac{\partial B_z}{\partial z}>0,
$$

那么

$$
B_r<0,
$$

即径向磁场分量指向 $-\hat{\mathbf r}$。

## 从径向磁场得到沿 $z$ 方向的力

粒子本身还在做回旋运动，回旋速度记为 $v_\theta$。

洛伦兹力仍然是

$$
\mathbf F=q\mathbf v\times\mathbf B.
$$

在当前轴对称、$B_\theta=0$ 的情况下，

$$
\mathbf B=B_r\hat{\mathbf r}+B_z\hat{\mathbf z}.
$$

把速度写成

$$
\mathbf v
=
v_r\hat{\mathbf r}
+
v_\theta\hat{\boldsymbol\theta}
+
v_z\hat{\mathbf z}.
$$

我们只看洛伦兹力的 $z$ 分量。叉乘中能够产生 $\hat{\mathbf z}$ 分量的是

$$
v_\theta\hat{\boldsymbol\theta}
\times
B_r\hat{\mathbf r}.
$$

因为

$$
\hat{\boldsymbol\theta}\times\hat{\mathbf r}
=
-\hat{\mathbf z},
$$

所以

$$
(\mathbf v\times\mathbf B)_z
=
-v_\theta B_r.
$$

于是

$$
\boxed{
F_z=-qv_\theta B_r
}.
$$

代入

$$
B_r
=
-\frac r2\frac{\partial B_z}{\partial z},
$$

得到

$$
F_z
=
qv_\theta\frac r2\frac{\partial B_z}{\partial z}.
$$

### 补上原稿这里隐含的 $r$ 与 Larmor 半径关系

原稿下一步直接使用

$$
qv_\theta r_L
=
-\frac{mv_\perp^2}{B}.
$$

要让它和上一式中的 $r$ 直接衔接，需要说明当前这一步所采用的局部几何图像：把导引中心取在轴线上，此时粒子绕轴线做局部 Larmor 回旋，粒子到轴线的距离就是回旋半径，

$$
r=r_L,
$$

并且

$$
|v_\theta|=v_\perp.
$$

这个有符号的 Larmor 关系也可以直接从径向洛伦兹力推出。

在局部把磁场近似看成

$$
\mathbf B\simeq B\hat{\mathbf z},
$$

粒子的圆周运动需要向心加速度

$$
a_r=-\frac{v_\theta^2}{r_L}.
$$

而径向洛伦兹力是

$$
F_r
=
qv_\theta B.
$$

于是

$$
qv_\theta B
=
-m\frac{v_\theta^2}{r_L}.
$$

当 $v_\theta\neq0$ 时，

$$
qv_\theta r_L
=
-\frac{mv_\theta^2}{B}.
$$

又因为回旋速度的大小就是 $v_\perp$，

$$
v_\theta^2=v_\perp^2,
$$

所以

$$
\boxed{
qv_\theta r_L
=
-\frac{mv_\perp^2}{B}
}.
$$

代回 $F_z$：

$$
\begin{aligned}
F_z
&=
\frac12
(qv_\theta r_L)
\frac{\partial B_z}{\partial z}\\
&=
-\frac{mv_\perp^2}{2B}
\frac{\partial B_z}{\partial z}.
\end{aligned}
$$

定义磁矩

$$
\boxed{
\mu=\frac{mv_\perp^2}{2B}
},
$$

于是

$$
F_z
=
-\mu\frac{\partial B_z}{\partial z}.
$$

### 从 $z$ 方向写成沿磁力线方向

原稿这里直接从

$$
-\mu\frac{\partial B_z}{\partial z}
$$

写到了

$$
-\mu\frac{\partial B}{\partial z},
$$

又写成

$$
-\mu\nabla_\parallel B.
$$

这中间实际上包含两个近似，需要明确写出来。

第一，在轴线附近，径向分量 $B_r$ 是小量，磁场主要沿 $z$ 方向，因此

$$
B
=
|\mathbf B|
=
\sqrt{B_z^2+B_r^2}
\simeq
B_z,
$$

所以在当前最低阶近似下

$$
\frac{\partial B}{\partial z}
\simeq
\frac{\partial B_z}{\partial z}.
$$

于是

$$
F_z
\simeq
-\mu\frac{\partial B}{\partial z}.
$$

第二，沿磁力线方向的梯度定义为

$$
\boxed{
\nabla_\parallel B
\equiv
\hat{\mathbf b}\cdot\nabla B
},
\qquad
\hat{\mathbf b}=\frac{\mathbf B}{B}.
$$

在轴线附近，

$$
\hat{\mathbf b}\simeq\hat{\mathbf z},
$$

所以

$$
\nabla_\parallel B
\simeq
\frac{\partial B}{\partial z}.
$$

同时此时 $z$ 方向也近似就是磁力线方向，因此

$$
F_\parallel\simeq F_z.
$$

综合起来，在当前磁镜轴线附近、磁场缓慢变化的近似下，

$$
\boxed{
F_\parallel
=
-\mu\nabla_\parallel B
}.
$$

这里最后写成标准磁镜力形式。它描述的是对快速回旋运动取平均后的慢运动结果。

### 这一推导还隐含了什么适用条件？

为了使用局部 Larmor 回旋和磁矩 $\mu$，还隐含了磁场在一个回旋半径尺度上变化缓慢，即典型地要求

$$
\frac{r_L}{L_B}\ll1,
$$

其中 $L_B$ 是磁场显著变化的空间尺度。

在这个绝热条件下，粒子快速回旋，而导引中心只感受到缓慢变化的磁场，磁矩

$$
\mu=\frac{mv_\perp^2}{2B}
$$

才可以在一阶近似下作为绝热不变量使用。

## 结论

整个推导的逻辑链可以整理为：

1. 从 $\nabla\cdot\mathbf B=0$ 出发；
2. 在柱坐标中逐面计算微小体元的磁通，推导出散度公式；
3. 对轴对称、无环向磁场的磁镜，在轴线附近得到

$$
B_r
\simeq
-\frac r2\frac{\partial B_z}{\partial z};
$$

4. 粒子的回旋速度 $v_\theta$ 与这个小的径向磁场 $B_r$ 通过洛伦兹力耦合，产生 $z$ 方向的力；
5. 在导引中心近似和绝热近似下，对快速回旋运动取平均，得到标准磁镜力

$$
\boxed{
F_\parallel=-\mu\nabla_\parallel B
}.
$$

因此，磁镜中的“沿磁力线反射力”并不是磁场直接沿磁力线对粒子施加了一个新的基本力，而是非均匀磁场、回旋运动以及 $\nabla\cdot\mathbf B=0$ 共同作用后，在导引中心尺度上表现出来的有效平行力。
