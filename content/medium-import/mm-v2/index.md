---
title: "From ∇·B = 0 to the Magnetic Mirror Force: A Complete Near-Axis Derivation"
date: 2026-09-17T08:44:00+08:00
draft: false
description: "A complete near-axis derivation of the magnetic mirror force, starting from ∇·B = 0 in cylindrical coordinates."
math: false
showToc: false
robotsNoIndex: true
sitemap:
  exclude: true
_build:
  list: never
---



> This note starts from magnetic-flux conservation in cylindrical coordinates. It keeps the intermediate derivation as complete as possible and adds the necessary mathematical steps and conditions of validity where a shortcut would otherwise be easy to miss.

<h2>The problem</h2>

How can a magnetic mirror produce a reflection force along a magnetic field line?

We consider only the **static, non-relativistic case with no electric field**. The ![](eq/inline-001.png) direction is chosen to coincide with the dominant magnetic-field direction near the axis, so ![](eq/inline-002.png) in the region under consideration.

The Lorentz force is


![equation](eq/display-001.png)


Write the magnetic field in cylindrical coordinates as


![equation](eq/display-002.png)


and Maxwell's equation gives


![equation](eq/display-003.png)


We begin with a small cylindrical volume element.

![Differential cylindrical volume element](fig-1-fixed.png)

*Figure 1. A differential sector-shaped cylindrical volume element, showing dθ, dr, and dz.*

The ranges of the volume element are


![equation](eq/display-004.png)


The corresponding differential lengths in the three directions are


![equation](eq/display-005.png)


Therefore, the volume is approximately


![equation](eq/display-006.png)


We now calculate the net outward magnetic flux through the six faces of this volume element.

<h2>The basic form of magnetic flux</h2>

The differential magnetic flux is


![equation](eq/display-007.png)


where ![](eq/inline-003.png) is the area of the surface element and ![](eq/inline-004.png) is the outward unit normal of that surface.

<h2>Magnetic flux through the two radial faces</h2>

![Radial-face geometry](fig-2.webp)

*Figure 2. Geometry and outward normal directions of the radial faces.*

<h3>Inner face at <img alt="equation" src="eq/inline-005.png"></h3>

The area of this face is


![equation](eq/display-008.png)


The outward normal of the inner face is ![](eq/inline-006.png), so


![equation](eq/display-009.png)


Expand the magnetic field completely:


![equation](eq/display-010.png)


Taking the dot product term by term:


![equation](eq/display-011.png)


Because the three cylindrical-coordinate unit basis vectors are mutually orthogonal,


![equation](eq/display-012.png)


Therefore,


![equation](eq/display-013.png)


Hence,


![equation](eq/display-014.png)


<h3>Outer face at <img alt="equation" src="eq/inline-007.png"></h3>

The area of this face is


![equation](eq/display-015.png)


At ![](eq/inline-008.png), the magnetic field is


![equation](eq/display-016.png)


The outward normal is ![](eq/inline-009.png), so


![equation](eq/display-017.png)


Again, expand the dot product completely:


![equation](eq/display-018.png)


Therefore,


![equation](eq/display-019.png)


<h3>Net outward flux through the two radial faces</h3>


![equation](eq/display-020.png)


Substituting the fluxes through the two faces gives


![equation](eq/display-021.png)


Define


![equation](eq/display-022.png)


Then


![equation](eq/display-023.png)


From the definition of the derivative,


![equation](eq/display-024.png)


Because ![](eq/inline-010.png) is infinitesimal, we can write the first-order approximation


![equation](eq/display-025.png)


Thus,


![equation](eq/display-026.png)


Here ![](eq/inline-011.png) actually comes from the multivariable function ![](eq/inline-012.png). When varying ![](eq/inline-013.png), ![](eq/inline-014.png) are held fixed, so a partial derivative should be used:


![equation](eq/display-027.png)


Therefore,


![equation](eq/display-028.png)


<h2>Magnetic flux through the two <img alt="equation" src="eq/inline-015.png">-direction faces</h2>

![Theta-direction side faces](fig-3-fixed.png)

*Figure 3. The θ-direction side faces and their outward normal directions.*

We repeat the same projection procedure for the two ![](eq/inline-016.png)-direction faces. Although the form is similar to that for the radial faces, writing it out explicitly makes each normal projection clear.

<h3>Inner face at <img alt="equation" src="eq/inline-017.png"></h3>

The two edges of this face are ![](eq/inline-018.png) and ![](eq/inline-019.png), so


![equation](eq/display-029.png)


The outward normal of this face is ![](eq/inline-020.png), therefore


![equation](eq/display-030.png)


Expand the magnetic field:


![equation](eq/display-031.png)


Taking the dot product term by term:


![equation](eq/display-032.png)


Using


![equation](eq/display-033.png)


we obtain


![equation](eq/display-034.png)


Therefore,


![equation](eq/display-035.png)


<h3>Outer face at <img alt="equation" src="eq/inline-021.png"></h3>

The other face is at ![](eq/inline-022.png), with outward normal ![](eq/inline-023.png):


![equation](eq/display-036.png)


Expand the dot product:


![equation](eq/display-037.png)


Thus,


![equation](eq/display-038.png)


<h3>Net outward flux through the two <img alt="equation" src="eq/inline-024.png"> faces</h3>


![equation](eq/display-039.png)


Therefore,


![equation](eq/display-040.png)


As before, hold the other variables fixed and consider only the variation in ![](eq/inline-025.png):


![equation](eq/display-041.png)


Therefore,


![equation](eq/display-042.png)


<h2>Magnetic flux through the two <img alt="equation" src="eq/inline-026.png">-direction faces</h2>

![Upper and lower faces with outward normals](fig-4.webp)

*Figure 4. The upper and lower z-faces and their outward normal directions.*

<h3>Lower face at <img alt="equation" src="eq/inline-027.png"></h3>

The two edges of the lower face are ![](eq/inline-028.png) and ![](eq/inline-029.png), so


![equation](eq/display-043.png)


The outward normal of the lower face is ![](eq/inline-030.png), therefore


![equation](eq/display-044.png)


Expand the dot product:


![equation](eq/display-045.png)


That is,


![equation](eq/display-046.png)


Since


![equation](eq/display-047.png)


we have


![equation](eq/display-048.png)


Therefore,


![equation](eq/display-049.png)


<h3>Upper face at <img alt="equation" src="eq/inline-031.png"></h3>

The outward normal of the upper face is ![](eq/inline-032.png):


![equation](eq/display-050.png)


Expand the dot product:


![equation](eq/display-051.png)


Therefore,


![equation](eq/display-052.png)


<h3>Net outward flux through the two <img alt="equation" src="eq/inline-033.png"> faces</h3>


![equation](eq/display-053.png)


Thus,


![equation](eq/display-054.png)


Using the same finite-difference approximation as above,


![equation](eq/display-055.png)


Therefore,


![equation](eq/display-056.png)


<h2>Obtaining the cylindrical-coordinate divergence from the fluxes in the three directions</h2>

The total net outward magnetic flux through the six faces is


![equation](eq/display-057.png)


Substituting the results from the three directions gives


![equation](eq/display-058.png)


Factor out the common differential-volume factor:


![equation](eq/display-059.png)


The divergence is defined as


![equation](eq/display-060.png)


For the present differential volume element,


![equation](eq/display-061.png)


Therefore,


![equation](eq/display-062.png)


Substitute both ![](eq/inline-034.png) and ![](eq/inline-035.png):


![equation](eq/display-063.png)


Cancel the common factor ![](eq/inline-036.png):


![equation](eq/display-064.png)


which is the familiar form


![equation](eq/display-065.png)


<h2>Using the axisymmetry of the magnetic mirror</h2>

The magnetic mirror is invariant under rotation about the ![](eq/inline-037.png) axis, so physical quantities do not depend on ![](eq/inline-038.png). Hence,


![equation](eq/display-066.png)


In addition, we assume here that there is no azimuthal magnetic field:


![equation](eq/display-067.png)


These two conditions must be distinguished: axisymmetry gives a zero partial derivative with respect to ![](eq/inline-039.png), whereas ![](eq/inline-040.png) is an additional assumption about the magnetic-field structure.

Thus,


![equation](eq/display-068.png)


Maxwell's equation also requires


![equation](eq/display-069.png)


Therefore,


![equation](eq/display-070.png)


<h2>Using <img alt="equation" src="eq/inline-041.png"> to obtain <img alt="equation" src="eq/inline-042.png"> near the axis</h2>

From the equation above,


![equation](eq/display-071.png)


that is,


![equation](eq/display-072.png)


![Magnetic mirror field lines](fig-5.webp)

*Figure 5. Magnetic field lines near the axis of a magnetic mirror; the red line marks a reference line close to the axis.*

Near the axis, if ![](eq/inline-043.png) varies sufficiently slowly in space, then in the present lowest-order approximation ![](eq/inline-044.png) can be treated as approximately constant with respect to ![](eq/inline-045.png).

More precisely, what is required here is that **near the axis, at fixed ![](eq/inline-046.png), the variation of ![](eq/inline-047.png) with ![](eq/inline-048.png) can be neglected at the order being retained.** Under axisymmetry, near the axis we can write


![equation](eq/display-073.png)


Therefore,


![equation](eq/display-074.png)


At the lowest retained order, ![](eq/inline-049.png) can be taken outside the integral with respect to ![](eq/inline-050.png).

To avoid confusing the integration variable with the upper limit, write the ![](eq/inline-051.png) inside the integral as ![](eq/inline-052.png):


![equation](eq/display-075.png)


The left-hand side integrates directly:


![equation](eq/display-076.png)


On the axis, ![](eq/inline-053.png); provided ![](eq/inline-054.png) remains finite, we have


![equation](eq/display-077.png)


The right-hand side is


![equation](eq/display-078.png)


Therefore,


![equation](eq/display-079.png)


We finally obtain


![equation](eq/display-080.png)


More rigorously, this is the lowest-order result near the axis:


![equation](eq/display-081.png)


If moving in the ![](eq/inline-055.png) direction, ![](eq/inline-056.png) slowly increases,


![equation](eq/display-082.png)


then


![equation](eq/display-083.png)


That is, the radial magnetic-field component points in the ![](eq/inline-057.png) direction.

<h2>Obtaining a force in the <img alt="equation" src="eq/inline-058.png"> direction from the radial magnetic field</h2>

The particle is also undergoing gyromotion; denote its azimuthal velocity by ![](eq/inline-059.png).

The Lorentz force remains


![equation](eq/display-084.png)


Under the present axisymmetric, ![](eq/inline-060.png) condition,


![equation](eq/display-085.png)


Write the velocity as


![equation](eq/display-086.png)


We consider only the ![](eq/inline-061.png) component of the Lorentz force. The term in the cross product that can produce a ![](eq/inline-062.png) component is


![equation](eq/display-087.png)


Because


![equation](eq/display-088.png)


we have


![equation](eq/display-089.png)


Hence,


![equation](eq/display-090.png)


Substituting


![equation](eq/display-091.png)


gives


![equation](eq/display-092.png)


<h3>Relating <img alt="equation" src="eq/inline-063.png"> to the Larmor radius</h3>

We next use


![equation](eq/display-093.png)


To connect this directly to the ![](eq/inline-064.png) in the preceding equation, first consider a **special orbit whose guiding center lies exactly on the axis**. In this near-axis local model, the particle's gyro-orbit is centered on the axis, so the particle's distance from the axis is the Larmor radius,


![equation](eq/display-094.png)


and


![equation](eq/display-095.png)


This signed Larmor relation can also be obtained directly from the radial Lorentz force.

Locally approximate the magnetic field as


![equation](eq/display-096.png)


The circular motion of the particle requires the centripetal acceleration


![equation](eq/display-097.png)


The radial Lorentz force is


![equation](eq/display-098.png)


Thus,


![equation](eq/display-099.png)


When ![](eq/inline-065.png),


![equation](eq/display-100.png)


Because the magnitude of the gyromotion velocity is ![](eq/inline-066.png),


![equation](eq/display-101.png)


we have


![equation](eq/display-102.png)


Substitute this back into ![](eq/inline-067.png):


![equation](eq/display-103.png)


Define the magnetic moment


![equation](eq/display-104.png)


Then


![equation](eq/display-105.png)


<h3>Rewriting the <img alt="equation" src="eq/inline-068.png">-direction result as a force along the magnetic field</h3>

Starting from the near-axis result


![equation](eq/display-106.png)


we write it as


![equation](eq/display-107.png)


and then as


![equation](eq/display-108.png)


Two approximations are implicit in these steps and should be stated explicitly.

First, near the axis the radial component ![](eq/inline-069.png) is small and the magnetic field is mainly in the ![](eq/inline-070.png) direction, so


![equation](eq/display-109.png)


Thus, at the current lowest order,


![equation](eq/display-110.png)


Therefore,


![equation](eq/display-111.png)


Second, define the gradient along the magnetic field line by


![equation](eq/display-112.png)


Near the axis,


![equation](eq/display-113.png)


so


![equation](eq/display-114.png)


At the same time, the ![](eq/inline-071.png) direction is approximately the magnetic-field-line direction, so


![equation](eq/display-115.png)


Combining these results, under the near-axis and slowly varying-field approximations for the magnetic mirror,


![equation](eq/display-116.png)


This is the standard magnetic mirror-force form. The explicit calculation above treats the near-axis special case in which the guiding center lies on the axis; for a general guiding-center position, the fast gyro-phase must be averaged. First-order guiding-center theory gives the same standard result ![](eq/inline-072.png).

<h3>What conditions of validity are implicit in this derivation?</h3>

Using local Larmor gyromotion and the magnetic moment ![](eq/inline-073.png) also assumes that the magnetic field varies slowly over one Larmor-radius scale; typically,


![equation](eq/display-117.png)


where ![](eq/inline-074.png) is the spatial scale over which the magnetic field changes significantly.

Under this adiabatic condition, the particle gyros rapidly while the guiding center experiences a slowly varying magnetic field, and the magnetic moment


![equation](eq/display-118.png)


can be used as an invariant at first adiabatic order in the non-relativistic approximation.

<h2>Conclusion</h2>

The logic of the derivation can be summarized as follows:

1. Start from ![](eq/inline-075.png);
2. Compute the magnetic flux through each face of a differential cylindrical volume element and derive the divergence formula;
3. For an axisymmetric magnetic mirror with no azimuthal magnetic field, obtain near the axis


![equation](eq/display-119.png)


4. The particle's gyromotion velocity ![](eq/inline-076.png) couples to the small radial magnetic field ![](eq/inline-077.png) through the Lorentz force and produces a force in the ![](eq/inline-078.png) direction;
5. Under the guiding-center and adiabatic approximations, average over the fast gyromotion to obtain the standard magnetic mirror force


![equation](eq/display-120.png)


Therefore, the “reflection force along the magnetic field line” in a magnetic mirror is not a new fundamental force applied directly along the field line. It is an effective parallel force that emerges on the guiding-center scale from the combined action of the nonuniform magnetic field, gyromotion, and ![](eq/inline-079.png).
