# SHA-1 算法
<python-script>{state}</python-script>
有关SHA的文档可以参阅[NIST.FIPS.180-4.pdf](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)

----------------------------------------------------------------
## 输入和输出
输入: 长度为<code><2<sup>64</sup>bit</code>的2进制消息  
输出: 长度为`160bit`的二进制消息摘要(哈希值)  通常使用40位的16进制表示

----------------------------------------------------------------
## 计算过程
<iframe src="/SHA-1流程图.html" height="292px" width="392px" frameborder="0" scrolling="no"></iframe>

----------------------------------------------------------------
### 预处理
#### 补位
补位需要把消息补位至能够被`512bit`整除  
步骤1: 在消息末尾补`1bit`的`1`  
步骤2: 在消息末尾补`448 - ((L+1) mod 512) bit`的`0` (`L`为消息的长度, 单位是bit)  
步骤3: 在消息末尾补上`64bit`的消息长度, **注意单位是bit不是byte并且使用大端序(Big Endian)**  

#### 512bit分组
将补位后的消息按`512bit`的长度进行分组，然后依次进行32bit分组

#### 32bit分组
将按`512bit`分组后的消息按`32bit`分组成16组, 使用一个名为`M`的数组表示, 下标为`0-15`

#### 设置初始值
<pre><code>H<sub>0</sub> = 0x67452301
H<sub>1</sub> = 0xefcdab89
H<sub>2</sub> = 0x98badcfe
H<sub>3</sub> = 0x10325476
H<sub>4</sub> = 0xc3d2e1f0</code></pre>  

----------------------------------------------------------------
### 计算
对每个32bit分组后的M数组依次进行计算

#### ROTL(rotate left)操作
ROTL操作需要将x左移n位的同时让左移位溢出的bit回到数组的起始位  
SHA-1 的 `w = 32bit`, 不同的SHA算法w的值会有所不同  
公式: <code>ROTL<sup>n</sup>(x) = (x << n) or (x >> (w-n))</code>  

例如 <code>w=8; ROTL<sup>1</sup>(0b10010101) = 00101011</code>  
<iframe src="/ROTL.html" height="39px" width="116px" frameborder="0" scrolling="no"></iframe>  
<p></p>
ps1: 几乎所有的SHA算法都会使用ROTL或者ROTR(rotate right), ROTL和ROTR区别是移位的方向相反  
ps2: `<<`和`>>`分别是左移位和右移位运算, `or`则是或运算

#### 32bit扩充
创建一个名为`W`的`32bit`数组下标为`0-79`  
W<sub>0-15</sub>直接复制M<sub>0-15</sub>即可
<pre><code>W<sub>0</sub> = M<sub>0</sub>
W<sub>1</sub> = M<sub>1</sub>
.....
W<sub>15</sub> = M<sub>15</sub></code></pre>  
W<sub>16-79</sub>的计算  
<code>W<sub>t</sub> = ROTL<sup>1</sup>(W<sub>t-3</sub>⊕W<sub>t-8</sub>⊕W<sub>t-14</sub>⊕W<sub>t-16</sub>)</code>  

例如
<pre>W<sub>16</sub> = ROTL<sup>1</sup>(W<sub>13</sub>⊕W<sub>8</sub>⊕W<sub>2</sub>⊕W<sub>0</sub>)
W<sub>17</sub> = ROTL<sup>1</sup>(W<sub>14</sub>⊕W<sub>9</sub>⊕W<sub>3</sub>⊕W<sub>1</sub>)
.....
W<sub>79</sub> = ROTL<sup>1</sup>(W<sub>76</sub>⊕W<sub>71</sub>⊕W<sub>65</sub>⊕W<sub>63</sub>)</code></pre>  

ps: ⊕是异或运算(xor)



