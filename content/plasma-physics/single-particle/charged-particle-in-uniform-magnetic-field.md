---
title: "均匀磁场中的带电粒子运动"
date: 2026-09-16T12:00:00+08:00
draft: false
description: "用洛伦兹力方程验证本站的 LaTeX、目录、分类与标签功能。"
categories:
  - "等离子体物理"
tags:
  - "单粒子运动"
  - "洛伦兹力"
  - "回旋运动"
math: true
showToc: true
---

## 问题

考虑质量为 $m$、电荷量为 $q$ 的粒子，在均匀磁场

$$
\mathbf{B}=B\hat{\mathbf{z}}
$$

中运动。暂不考虑电场和碰撞，粒子的轨迹是什么？

## 运动方程

洛伦兹力方程为

$$
m\frac{d\mathbf{v}}{dt}=q\mathbf{v}\times\mathbf{B}.
$$

把速度写成

$$
\mathbf{v}=v_x\hat{\mathbf{x}}+v_y\hat{\mathbf{y}}+v_z\hat{\mathbf{z}},
$$

代入后得到三个分量方程：

$$
\begin{aligned}
m\frac{dv_x}{dt} &= qBv_y,\\
m\frac{dv_y}{dt} &= -qBv_x,\\
m\frac{dv_z}{dt} &= 0.
\end{aligned}
$$

定义带符号的回旋频率

$$
\Omega_c=\frac{qB}{m},
$$

则垂直磁场方向的速度满足简谐形式，而平行速度 $v_z$ 保持不变。

## 轨迹

垂直速度的大小

$$
v_\perp=\sqrt{v_x^2+v_y^2}
$$

保持不变，对应的拉莫尔半径为

$$
\rho_L=\frac{v_\perp}{|\Omega_c|}=\frac{mv_\perp}{|q|B}.
$$

因此，粒子在垂直于磁场的平面内做圆周运动，同时沿磁场方向匀速运动；合成轨迹是一条螺旋线。电荷符号决定回旋方向，但不改变 $\rho_L$ 的大小。

## 能量检查

磁场不对粒子做功，因为

$$
\frac{d}{dt}\left(\frac12 mv^2\right)
=\mathbf{v}\cdot q(\mathbf{v}\times\mathbf{B})=0.
$$

这里使用了叉乘结果与原向量垂直这一性质。动能守恒与上面的圆周—螺旋运动图像一致。

## 结论

这个最简单的模型同时验证了本站需要长期使用的三类表达：行内公式、独立公式和多行对齐公式。后续文章将在此基础上讨论电场漂移、非均匀磁场漂移与磁矩守恒。

