# 10-曲线积分和曲面积分

## 第一类曲线积分


### 概念

曲线积分

$$\int_C{f(x,y)ds}$$

环路积分

$$\oint_C{f(x,y)ds}$$

### 计算



## 第一类曲面积分


### 概念

$$\iint_{\Sigma}{f(x,y,z)dS}$$

### 计算

$$
\begin{cases}
x=x(u,v) \\
y=y(u,v) \\ 
z=z(u,v) \\
\end{cases}
$$

$$\iint_{\Sigma}{f(x,y,z)dS}=\iint_{D_{uv}}{f(x(u,v),y(u,v),z(u,v))\sqrt{A^2+B^2+C^2}dudv}$$

其中

$$
A= \frac{\partial(y,z)}{\partial(u,v)} \quad
B=\frac{\partial(z,x)}{\partial(u,v)} \quad
C=\frac{\partial(x,y)}{\partial(u,v)}
$$

## 第二类曲线积分

### 概念

$$\int_C{\mathbf{F}(x,y) \cdot d\mathbf{r}}$$

$$\int_C{P(x,y)dx+Q(x,y)dy}$$

### 计算


## 第二类曲面积分

### 概念

$$d\mathbf{S}=\mathbf{n}^0dS$$

$$\iint_{\Sigma^+}{\mathbf{F}(x,y,z) \cdot d\mathbf{S}}$$

$$\iint_{\Sigma^+}{Pdydz+Qdxdz+Rdxdy}$$

### 计算

可以化为第一类曲面积分：

$$\iint_{\Sigma^+}{\mathbf{F}(x,y,z) \cdot d\mathbf{S}}=\iint_{\Sigma^+}{\mathbf{F} \cdot \mathbf{n}^0 dS}$$

由第一类曲面积分可得：

$$\iint_{\Sigma^+}{\mathbf{F}(x,y,z) \cdot d\mathbf{S}}=\iint_{\Sigma^+}{\frac{PA+QB+RC}{\sqrt{ A^2+B^2+C^2 }}dS}=\iint_{\Sigma^+}{(PA+QB+RC)dudv}$$

当曲面可以写成 $z(x,y)$ 的形式时，可视为特殊情况：

$$\iint_{\Sigma^+}{\mathbf{F}(x,y,z) \cdot d\mathbf{S}}=\iint_{\Sigma^+}{(Pz_{x}+Qz_{y}-R)dxdy}$$

## Green 公式及其应用

### Green 公式

$$\oint_C{Pdx+Qdy}=\iint_{D}({\frac{\partial{Q}}{\partial{x}}-\frac{\partial{P}}{\partial{y}}})dxdy$$

$$\oint_C{Pdx}=-\iint_{D}{\frac{\partial{P}}{\partial{y}}}dxdy$$

$$\oint_C{Qdy}=\iint_{D}{\frac{\partial{Q}}{\partial{x}}}dxdy$$

### 路径无关/解析函数

$$\oint_C{Pdx+Qdy}=0$$

### 全微分求积与全微分方程
积分因子：

$$\frac{1}{x} \quad \frac{1}{y} \quad \frac{1}{xy} \quad \frac{1}{x^2+y^2} \quad \frac{1}{\sqrt{ x^2+y^2 }}$$

## Gauss 公式

$$\iint_{\Sigma^+}{\mathbf{F}(x,y,z) \cdot d\mathbf{S}}=\iiint_{\Omega}{\nabla \cdot \mathbf{F} dV}$$

## Stokes 公式

疑似不考

