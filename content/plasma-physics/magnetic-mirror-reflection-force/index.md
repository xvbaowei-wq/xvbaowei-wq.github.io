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

> 本文从柱坐标下的磁通守恒出发，尽量保留完整的中间推导，并在容易产生跳步的地方补充必要的数学步骤与适用条件。

## 问题

磁镜为什么能够产生沿磁力线方向的反射力？

以下只讨论**静态、无电场**的非相对论情形，并选择 $+z$ 方向与轴线附近的主磁场方向一致，因此在所讨论区域有 $B_z>0$。

已知洛伦兹力

<div class="math-display">
$$
\mathbf F=q\mathbf v\times\mathbf B,
$$
</div>

磁场写成柱坐标形式

<div class="math-display">
$$
\mathbf B=B_r\hat{\mathbf r}+B_\theta\hat{\boldsymbol\theta}+B_z\hat{\mathbf z},
$$
</div>

以及 Maxwell 方程

<div class="math-display">
$$
\nabla\cdot\mathbf B=0.
$$
</div>

下面从一个很小的柱坐标体元开始。

![柱坐标微小体元](cylindrical-volume-element.png)

*图 1　柱坐标微小扇形体元，标出了 $d\theta$、$dr$ 和 $dz$。*

体元的范围为

<div class="math-display">
$$
r\to r+dr,\qquad
\theta\to\theta+d\theta,\qquad
z\to z+dz.
$$
</div>

三个方向上的微小长度分别为

<div class="math-display">
$$
dr,\qquad r\thinspace{}d\theta,\qquad dz.
$$
</div>

因此体积近似为

<div class="math-display">
$$
dV=r\thinspace{}dr\thinspace{}d\theta\thinspace{}dz.
$$
</div>

现在计算这个体元六个面的净流出磁通。

## 磁通的基本形式

磁通微元为

<div class="math-display">
$$
d\Phi=\mathbf B\cdot\hat{\mathbf n}\thinspace{}dA,
$$
</div>

其中 $dA$ 是面元面积，$\hat{\mathbf n}$ 是该面的外法向。

## 径向两个面的磁通

![径向面示意](volume-element-radial-face.png)

*图 2　用于分析径向两个面的体元示意。*

### 位于 $r$ 处的内侧面

这个面的面积为

<div class="math-display">
$$
dA_{r,\mathrm{in}}=r\thinspace{}d\theta\thinspace{}dz.
$$
</div>

内侧面的外法向是 $-\hat{\mathbf r}$，因此

<div class="math-display">
$$
d\Phi_{r,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\mathbf r})
\thinspace{}r\thinspace{}d\theta\thinspace{}dz.
$$
</div>

把磁场完整展开：

<div class="math-display">
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
</div>

逐项点乘：

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\mathbf r})
=
-B_r(\hat{\mathbf r}\cdot\hat{\mathbf r})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\mathbf r})
-B_z(\hat{\mathbf z}\cdot\hat{\mathbf r}).
$$
</div>

由于柱坐标三个单位基矢两两正交，

<div class="math-display">
$$
\hat{\mathbf r}\cdot\hat{\mathbf r}=1,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\mathbf r}=0,
\qquad
\hat{\mathbf z}\cdot\hat{\mathbf r}=0,
$$
</div>

所以

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\mathbf r})=-B_r.
$$
</div>

于是

<div class="math-display">
$$
\boxed{
d\Phi_{r,\mathrm{in}}
=
-B_r(r,\theta,z)\thinspace{}r\thinspace{}d\theta\thinspace{}dz
}.
$$
</div>

### 位于 $r+dr$ 处的外侧面

这个面的面积为

<div class="math-display">
$$
dA_{r,\mathrm{out}}
=
(r+dr)d\theta\thinspace{}dz.
$$
</div>

在 $r+dr$ 处，磁场是

<div class="math-display">
$$
\mathbf B(r+dr,\theta,z),
$$
</div>

外法向为 $+\hat{\mathbf r}$，所以

<div class="math-display">
$$
d\Phi_{r,\mathrm{out}}
=
\mathbf B(r+dr,\theta,z)\cdot\hat{\mathbf r}
\thinspace{}(r+dr)d\theta\thinspace{}dz.
$$
</div>

同样把点乘完整展开：

<div class="math-display">
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
</div>

因此

<div class="math-display">
$$
\boxed{
d\Phi_{r,\mathrm{out}}
=
B_r(r+dr,\theta,z)(r+dr)d\theta\thinspace{}dz
}.
$$
</div>

### 两个径向面的净流出

<div class="math-display">
$$
d\Phi_r
=
d\Phi_{r,\mathrm{out}}
+
d\Phi_{r,\mathrm{in}}.
$$
</div>

代入两面的磁通：

<div class="math-display">
$$
d\Phi_r
=
\left[
(r+dr)B_r(r+dr,\theta,z)
-
rB_r(r,\theta,z)
\right]d\theta\thinspace{}dz.
$$
</div>

定义

<div class="math-display">
$$
f(r)=rB_r(r,\theta,z),
$$
</div>

于是

<div class="math-display">
$$
d\Phi_r
=
[f(r+dr)-f(r)]d\theta\thinspace{}dz.
$$
</div>

根据导数定义，

<div class="math-display">
$$
\frac{df}{dr}
=
\lim_{\Delta r\to0}
\frac{f(r+\Delta r)-f(r)}{\Delta r}.
$$
</div>

因为这里的 $dr$ 是无穷小量，可以写成一阶近似

<div class="math-display">
$$
\frac{f(r+dr)-f(r)}{dr}
\approx
\frac{df}{dr},
$$
</div>

所以

<div class="math-display">
$$
f(r+dr)-f(r)
\approx
\frac{df}{dr}dr.
$$
</div>

这里 $f$ 实际来自多变量函数 $rB_r(r,\theta,z)$，在变化 $r$ 时把 $\theta,z$ 固定，因此应写成偏导数：

<div class="math-display">
$$
f(r+dr)-f(r)
\approx
\frac{\partial[rB_r(r,\theta,z)]}{\partial r}dr.
$$
</div>

所以

<div class="math-display">
$$
\boxed{
d\Phi_r
=
\frac{\partial(rB_r)}{\partial r}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$
</div>

## $\theta$ 方向两个面的磁通

下面对 $\theta$ 方向两个面重复同样的投影过程。虽然形式和径向面相似，但完整写出可以明确每一步的法向投影。

### 位于 $\theta$ 处的内侧面

这个面的两条边分别是 $dr$ 和 $dz$，所以

<div class="math-display">
$$
dA_\theta=dr\thinspace{}dz.
$$
</div>

该面的外法向是 $-\hat{\boldsymbol\theta}$，因此

<div class="math-display">
$$
d\Phi_{\theta,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\boldsymbol\theta})
\thinspace{}dr\thinspace{}dz.
$$
</div>

展开磁场：

<div class="math-display">
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
</div>

逐项点乘：

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\boldsymbol\theta})
=
-B_r(\hat{\mathbf r}\cdot\hat{\boldsymbol\theta})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta})
-B_z(\hat{\mathbf z}\cdot\hat{\boldsymbol\theta}).
$$
</div>

利用

<div class="math-display">
$$
\hat{\mathbf r}\cdot\hat{\boldsymbol\theta}=0,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta}=1,
\qquad
\hat{\mathbf z}\cdot\hat{\boldsymbol\theta}=0,
$$
</div>

得到

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\boldsymbol\theta})=-B_\theta.
$$
</div>

因此

<div class="math-display">
$$
\boxed{
d\Phi_{\theta,\mathrm{in}}
=
-B_\theta(r,\theta,z)\thinspace{}dr\thinspace{}dz
}.
$$
</div>

### 位于 $\theta+d\theta$ 处的外侧面

另一面位于 $\theta+d\theta$，外法向为 $+\hat{\boldsymbol\theta}$：

<div class="math-display">
$$
d\Phi_{\theta,\mathrm{out}}
=
\mathbf B(r,\theta+d\theta,z)\cdot\hat{\boldsymbol\theta}
\thinspace{}dr\thinspace{}dz.
$$
</div>

展开点乘：

<div class="math-display">
$$
\begin{aligned}
\mathbf B(r,\theta+d\theta,z)\cdot\hat{\boldsymbol\theta}
&=
\left[
B_r(r,\theta+d\theta,z)\hat{\mathbf r}
+
B_\theta(r,\theta+d\theta,z)\hat{\boldsymbol\theta}
+
B_z(r,\theta+d\theta,z)\hat{\mathbf z}
\right]\cdot\hat{\boldsymbol\theta}\\
&=
B_r(r,\theta+d\theta,z)(\hat{\mathbf r}\cdot\hat{\boldsymbol\theta})
+
B_\theta(r,\theta+d\theta,z)
(\hat{\boldsymbol\theta}\cdot\hat{\boldsymbol\theta})
+
B_z(r,\theta+d\theta,z)(\hat{\mathbf z}\cdot\hat{\boldsymbol\theta})\\
&=
B_\theta(r,\theta+d\theta,z).
\end{aligned}
$$
</div>

所以

<div class="math-display">
$$
\boxed{
d\Phi_{\theta,\mathrm{out}}
=
B_\theta(r,\theta+d\theta,z)\thinspace{}dr\thinspace{}dz
}.
$$
</div>

### 两个 $\theta$ 面的净流出

<div class="math-display">
$$
d\Phi_\theta
=
d\Phi_{\theta,\mathrm{out}}
+
d\Phi_{\theta,\mathrm{in}},
$$
</div>

所以

<div class="math-display">
$$
d\Phi_\theta
=
\left[
B_\theta(r,\theta+d\theta,z)
-
B_\theta(r,\theta,z)
\right]dr\thinspace{}dz.
$$
</div>

和前面一样，把其他变量固定，只考察 $\theta$ 的变化：

<div class="math-display">
$$
B_\theta(\theta+d\theta)-B_\theta(\theta)
\approx
\frac{\partial B_\theta}{\partial\theta}d\theta.
$$
</div>

因此

<div class="math-display">
$$
\boxed{
d\Phi_\theta
=
\frac{\partial B_\theta}{\partial\theta}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$
</div>

## $z$ 方向两个面的磁通

![上下表面与外法向](volume-element-normal-directions.png)

*图 3　上下表面及其外法向的示意。*

### 位于 $z$ 处的底面

底面的两条边分别为 $dr$ 和 $r\,d\theta$，所以

<div class="math-display">
$$
dA_z
=
r\thinspace{}dr\thinspace{}d\theta.
$$
</div>

底面的外法向是 $-\hat{\mathbf z}$，因此

<div class="math-display">
$$
d\Phi_{z,\mathrm{in}}
=
\mathbf B(r,\theta,z)\cdot(-\hat{\mathbf z})
\thinspace{}r\thinspace{}dr\thinspace{}d\theta.
$$
</div>

展开点乘：

<div class="math-display">
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
</div>

即

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\mathbf z})
=
-B_r(\hat{\mathbf r}\cdot\hat{\mathbf z})
-B_\theta(\hat{\boldsymbol\theta}\cdot\hat{\mathbf z})
-B_z(\hat{\mathbf z}\cdot\hat{\mathbf z}).
$$
</div>

由于

<div class="math-display">
$$
\hat{\mathbf r}\cdot\hat{\mathbf z}=0,
\qquad
\hat{\boldsymbol\theta}\cdot\hat{\mathbf z}=0,
\qquad
\hat{\mathbf z}\cdot\hat{\mathbf z}=1,
$$
</div>

所以

<div class="math-display">
$$
\mathbf B\cdot(-\hat{\mathbf z})=-B_z.
$$
</div>

因此

<div class="math-display">
$$
\boxed{
d\Phi_{z,\mathrm{in}}
=
-B_z(r,\theta,z)\thinspace{}r\thinspace{}dr\thinspace{}d\theta
}.
$$
</div>

### 位于 $z+dz$ 处的顶面

顶面的外法向是 $+\hat{\mathbf z}$：

<div class="math-display">
$$
d\Phi_{z,\mathrm{out}}
=
\mathbf B(r,\theta,z+dz)\cdot\hat{\mathbf z}
\thinspace{}r\thinspace{}dr\thinspace{}d\theta.
$$
</div>

展开点乘：

<div class="math-display">
$$
\begin{aligned}
\mathbf B(r,\theta,z+dz)\cdot\hat{\mathbf z}
&=
\left[
B_r(r,\theta,z+dz)\hat{\mathbf r}
+
B_\theta(r,\theta,z+dz)\hat{\boldsymbol\theta}
+
B_z(r,\theta,z+dz)\hat{\mathbf z}
\right]\cdot\hat{\mathbf z}\\
&=
B_r(r,\theta,z+dz)(\hat{\mathbf r}\cdot\hat{\mathbf z})
+
B_\theta(r,\theta,z+dz)(\hat{\boldsymbol\theta}\cdot\hat{\mathbf z})
+
B_z(r,\theta,z+dz)(\hat{\mathbf z}\cdot\hat{\mathbf z})\\
&=
B_z(r,\theta,z+dz).
\end{aligned}
$$
</div>

所以

<div class="math-display">
$$
\boxed{
d\Phi_{z,\mathrm{out}}
=
B_z(r,\theta,z+dz)\thinspace{}r\thinspace{}dr\thinspace{}d\theta
}.
$$
</div>

### 两个 $z$ 面的净流出

<div class="math-display">
$$
d\Phi_z
=
d\Phi_{z,\mathrm{out}}
+
d\Phi_{z,\mathrm{in}},
$$
</div>

所以

<div class="math-display">
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
</div>

根据前面相同的有限差分近似，

<div class="math-display">
$$
B_z(r,\theta,z+dz)-B_z(r,\theta,z)
\approx
\frac{\partial B_z}{\partial z}dz.
$$
</div>

因此

<div class="math-display">
$$
\boxed{
d\Phi_z
=
r\frac{\partial B_z}{\partial z}
\thinspace{}dr\thinspace{}d\theta\thinspace{}dz
}.
$$
</div>

## 从三个方向的磁通得到柱坐标散度

六个面的总净流出磁通为

<div class="math-display">
$$
d\Phi
=
d\Phi_r+d\Phi_\theta+d\Phi_z.
$$
</div>

代入三个方向的结果：

<div class="math-display">
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
</div>

把公共的体积微元部分提出来：

<div class="math-display">
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
</div>

散度的定义是

<div class="math-display">
$$
\nabla\cdot\mathbf B
=
\lim_{dV\to0}
\frac{\text{净流出磁通}}{\text{体积}}.
$$
</div>

对于当前微小体元，

<div class="math-display">
$$
dV=r\thinspace{}dr\thinspace{}d\theta\thinspace{}dz,
$$
</div>

因此

<div class="math-display">
$$
\nabla\cdot\mathbf B
=
\frac{d\Phi}{dV}.
$$
</div>

把 $d\Phi$ 和 $dV$ 都代进去：

<div class="math-display">
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
</div>

约去公共因子 $dr\,d\theta\,dz$：

<div class="math-display">
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
</div>

也就是熟悉的形式

<div class="math-display">
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
</div>

## 利用磁镜的轴对称性

磁镜绕 $z$ 轴旋转后不变，因此各物理量不依赖 $\theta$。于是

<div class="math-display">
$$
\frac{\partial B_\theta}{\partial\theta}=0.
$$
</div>

此外，这里采用“没有环向磁场”的设定：

<div class="math-display">
$$
B_\theta=0.
$$
</div>

需要区分这两个条件：轴对称性给出的是对 $\theta$ 的偏导为零；$B_\theta=0$ 是额外的磁场结构假设。

于是

<div class="math-display">
$$
\nabla\cdot\mathbf B
=
\frac1r\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_z}{\partial z}.
$$
</div>

Maxwell 方程又规定

<div class="math-display">
$$
\nabla\cdot\mathbf B=0,
$$
</div>

所以

<div class="math-display">
$$
\boxed{
\frac1r\frac{\partial(rB_r)}{\partial r}
+
\frac{\partial B_z}{\partial z}
=0
}.
$$
</div>

## 由 $\nabla\cdot\mathbf B=0$ 求轴线附近的 $B_r$

由上式，

<div class="math-display">
$$
\frac1r\frac{\partial(rB_r)}{\partial r}
=
-\frac{\partial B_z}{\partial z},
$$
</div>

即

<div class="math-display">
$$
\frac{\partial(rB_r)}{\partial r}
=
-r\frac{\partial B_z}{\partial z}.
$$
</div>

![磁镜磁力线](magnetic-mirror-field-lines.png)

*图 4　磁镜轴线附近的磁力线示意；红线表示靠近轴线的一条参考线。*

在靠近轴线的区域，如果 $B_z$ 随空间变化足够缓慢，可以在当前最低阶近似中把 $\partial B_z/\partial z$ 视为关于 $r$ 的近似常量。

更准确地说，这一步真正需要的是：**在轴线附近，对固定的 $z$，$\partial B_z/\partial z$ 对 $r$ 的变化可以忽略到当前的一阶近似。** 轴对称性下，轴线附近可以写成

<div class="math-display">
$$
B_z(r,z)=B_0(z)+O(r^2),
$$
</div>

因此

<div class="math-display">
$$
\frac{\partial B_z}{\partial z}
=
\frac{dB_0}{dz}
+
O(r^2).
$$
</div>

在保留最低阶项时，可以把 $\partial B_z/\partial z$ 从关于 $r$ 的积分中提出。

为避免积分变量混淆，把积分内部的 $r$ 写成 $r'$：

<div class="math-display">
$$
\int_0^r
\frac{\partial(r'B_r)}{\partial r'}dr'
\simeq
-\left[\frac{\partial B_z}{\partial z}\right]_{r=0}
\int_0^r r'\thinspace{}dr'.
$$
</div>

左边直接积分：

<div class="math-display">
$$
\int_0^r
\frac{\partial(r'B_r)}{\partial r'}dr'
=
rB_r(r)-\left.r'B_r(r')\right|_{r'=0}.
$$
</div>

在轴线上 $r'=0$，只要 $B_r$ 有限，就有

<div class="math-display">
$$
\left.r'B_r(r')\right|_{r'=0}=0.
$$
</div>

右边为

<div class="math-display">
$$
-\left[\frac{\partial B_z}{\partial z}\right]_{r=0}
\int_0^r r'\thinspace{}dr'
=
-\frac{r^2}{2}
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}.
$$
</div>

所以

<div class="math-display">
$$
rB_r(r,z)
\simeq
-\frac12r^2
\left[\frac{\partial B_z}{\partial z}\right]_{r=0},
$$
</div>

最终得到

<div class="math-display">
$$
\boxed{
B_r(r,z)
\simeq
-\frac r2
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}
}.
$$
</div>

更严格地说，这是轴线附近的最低阶结果：

<div class="math-display">
$$
B_r(r,z)
=
-\frac r2\frac{dB_0}{dz}
+
O(r^3).
$$
</div>

如果沿 $+z$ 方向运动时 $B_z$ 慢慢增大，

<div class="math-display">
$$
\frac{\partial B_z}{\partial z}>0,
$$
</div>

那么

<div class="math-display">
$$
B_r<0,
$$
</div>

即径向磁场分量指向 $-\hat{\mathbf r}$。

## 从径向磁场得到沿 $z$ 方向的力

粒子本身还在做回旋运动，回旋速度记为 $v_\theta$。

洛伦兹力仍然是

<div class="math-display">
$$
\mathbf F=q\mathbf v\times\mathbf B.
$$
</div>

在当前轴对称、$B_\theta=0$ 的情况下，

<div class="math-display">
$$
\mathbf B=B_r\hat{\mathbf r}+B_z\hat{\mathbf z}.
$$
</div>

把速度写成

<div class="math-display">
$$
\mathbf v
=
v_r\hat{\mathbf r}
+
v_\theta\hat{\boldsymbol\theta}
+
v_z\hat{\mathbf z}.
$$
</div>

我们只看洛伦兹力的 $z$ 分量。叉乘中能够产生 $\hat{\mathbf z}$ 分量的是

<div class="math-display">
$$
v_\theta\hat{\boldsymbol\theta}
\times
B_r\hat{\mathbf r}.
$$
</div>

因为

<div class="math-display">
$$
\hat{\boldsymbol\theta}\times\hat{\mathbf r}
=
-\hat{\mathbf z},
$$
</div>

所以

<div class="math-display">
$$
(\mathbf v\times\mathbf B)_z
=
-v_\theta B_r.
$$
</div>

于是

<div class="math-display">
$$
\boxed{
F_z=-qv_\theta B_r
}.
$$
</div>

代入

<div class="math-display">
$$
B_r
\simeq
-\frac r2
\left[\frac{\partial B_z}{\partial z}\right]_{r=0},
$$
</div>

得到

<div class="math-display">
$$
F_z
\simeq
qv_\theta\frac r2
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}.
$$
</div>

### 说明 $r$ 与 Larmor 半径的关系

接下来需要使用

<div class="math-display">
$$
qv_\theta r_L
=
-\frac{mv_\perp^2}{B}.
$$
</div>

要让它和上一式中的 $r$ 直接衔接，这里先考虑一个**导引中心恰好位于轴线上的特殊轨道**。在这个近轴局部模型中，粒子的回旋圆以轴线为中心，因此粒子到轴线的距离就是 Larmor 半径，

<div class="math-display">
$$
r=r_L,
$$
</div>

并且

<div class="math-display">
$$
|v_\theta|=v_\perp.
$$
</div>

这个有符号的 Larmor 关系也可以直接从径向洛伦兹力推出。

在局部把磁场近似看成

<div class="math-display">
$$
\mathbf B\simeq B\hat{\mathbf z},
$$
</div>

粒子的圆周运动需要向心加速度

<div class="math-display">
$$
a_r=-\frac{v_\theta^2}{r_L}.
$$
</div>

而径向洛伦兹力是

<div class="math-display">
$$
F_r
=
qv_\theta B.
$$
</div>

于是

<div class="math-display">
$$
qv_\theta B
=
-m\frac{v_\theta^2}{r_L}.
$$
</div>

当 $v_\theta\neq0$ 时，

<div class="math-display">
$$
qv_\theta r_L
=
-\frac{mv_\theta^2}{B}.
$$
</div>

又因为回旋速度的大小就是 $v_\perp$，

<div class="math-display">
$$
v_\theta^2=v_\perp^2,
$$
</div>

所以

<div class="math-display">
$$
\boxed{
qv_\theta r_L
=
-\frac{mv_\perp^2}{B}
}.
$$
</div>

代回 $F_z$：

<div class="math-display">
$$
\begin{aligned}
F_z
&\simeq
\frac12
(qv_\theta r_L)
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}\\
&=
-\frac{mv_\perp^2}{2B}
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}.
\end{aligned}
$$
</div>

定义磁矩

<div class="math-display">
$$
\boxed{
\mu=\frac{mv_\perp^2}{2B}
},
$$
</div>

于是

<div class="math-display">
$$
F_z
\simeq
-\mu
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}.
$$
</div>

### 从 $z$ 方向写成沿磁力线方向

从近轴结果

<div class="math-display">
$
-\mu
\left[\frac{\partial B_z}{\partial z}\right]_{r=0}
$
</div>

写到了

<div class="math-display">
$$
-\mu\frac{\partial B}{\partial z},
$$
</div>

又写成

<div class="math-display">
$$
-\mu\nabla_\parallel B.
$$
</div>

这中间实际上包含两个近似，需要明确写出来。

第一，在轴线附近，径向分量 $B_r$ 是小量，磁场主要沿 $z$ 方向，因此

<div class="math-display">
$$
B
=
|\mathbf B|
=
\sqrt{B_z^2+B_r^2}
\simeq
B_z,
$$
</div>

所以在当前最低阶近似下

<div class="math-display">
$$
\frac{\partial B}{\partial z}
\simeq
\frac{\partial B_z}{\partial z}.
$$
</div>

于是

<div class="math-display">
$$
F_z
\simeq
-\mu\frac{\partial B}{\partial z}.
$$
</div>

第二，沿磁力线方向的梯度定义为

<div class="math-display">
$$
\boxed{
\nabla_\parallel B
\equiv
\hat{\mathbf b}\cdot\nabla B
},
\qquad
\hat{\mathbf b}=\frac{\mathbf B}{B}.
$$
</div>

在轴线附近，

<div class="math-display">
$$
\hat{\mathbf b}\simeq\hat{\mathbf z},
$$
</div>

所以

<div class="math-display">
$$
\nabla_\parallel B
\simeq
\frac{\partial B}{\partial z}.
$$
</div>

同时此时 $z$ 方向也近似就是磁力线方向，因此

<div class="math-display">
$$
F_\parallel\simeq F_z.
$$
</div>

综合起来，在当前磁镜轴线附近、磁场缓慢变化的近似下，

<div class="math-display">
$$
\boxed{
F_\parallel
=
-\mu\nabla_\parallel B
}.
$$
</div>

这里得到的是标准磁镜力形式。上面的显式计算针对导引中心位于轴线的近轴特例；对于一般的导引中心位置，需要对快速回旋相位做平均。一阶导引中心理论得到同样的标准结果 $F_{\parallel,\mathrm{mirror}}=-\mu\nabla_\parallel B$。

### 这一推导还隐含了什么适用条件？

为了使用局部 Larmor 回旋和磁矩 $\mu$，还隐含了磁场在一个回旋半径尺度上变化缓慢，即典型地要求

<div class="math-display">
$$
\frac{r_L}{L_B}\ll1,
$$
</div>

其中 $L_B$ 是磁场显著变化的空间尺度。

在这个绝热条件下，粒子快速回旋，而导引中心只感受到缓慢变化的磁场，磁矩

<div class="math-display">
$
\mu=\frac{mv_\perp^2}{2B}
$
</div>

才可以在非相对论的一阶绝热近似下作为不变量使用。

## 结论

整个推导的逻辑链可以整理为：

1. 从 $\nabla\cdot\mathbf B=0$ 出发；
2. 在柱坐标中逐面计算微小体元的磁通，推导出散度公式；
3. 对轴对称、无环向磁场的磁镜，在轴线附近得到

<div class="math-display">
$$
B_r
\simeq
-\frac r2
\left[\frac{\partial B_z}{\partial z}\right]_{r=0};
$$
</div>

4. 粒子的回旋速度 $v_\theta$ 与这个小的径向磁场 $B_r$ 通过洛伦兹力耦合，产生 $z$ 方向的力；
5. 在导引中心近似和绝热近似下，对快速回旋运动取平均，得到标准磁镜力

<div class="math-display">
$$
\boxed{
F_\parallel=-\mu\nabla_\parallel B
}.
$$
</div>

因此，磁镜中的“沿磁力线反射力”并不是磁场直接沿磁力线对粒子施加了一个新的基本力，而是非均匀磁场、回旋运动以及 $\nabla\cdot\mathbf B=0$ 共同作用后，在导引中心尺度上表现出来的有效平行力。
