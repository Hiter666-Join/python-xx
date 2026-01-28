import math

print("math 库常用函数演示\n")

# 一、数值处理
print("数值处理")
print(f"math.ceil(4.3)           : 向上取整 = {math.ceil(4.3)}")
print(f"math.floor(4.8)          : 向下取整 = {math.floor(4.8)}")
print(f"math.trunc(4.8)          : 截断小数 = {math.trunc(4.8)}")
print(f"math.modf(4.75)          : 拆成小数和整数部分 = {math.modf(4.75)}")
print(f"math.fabs(-5)            : 绝对值 = {math.fabs(-5)}")
print(f"math.pow(2, 3)           : 幂运算 = {math.pow(2, 3)}")
print(f"math.sqrt(16)            : 平方根 = {math.sqrt(16)}")
print(f"math.isfinite(1e308)     : 是否有限 = {math.isfinite(1e308)}")
print(f"math.isinf(float('inf')) : 是否无穷 = {math.isinf(float('inf'))}")
print(f"math.isnan(float('nan')) : 是否NaN  = {math.isnan(float('nan'))}")

# 二、对数与指数
print("\n对数与指数")
print(f"math.exp(2)              : e 的 2 次方 = {math.exp(2)}")
print(f"math.log(100)            : 自然对数 = {math.log(100)}")
print(f"math.log10(100)          : 以 10 为底 = {math.log10(100)}")
print(f"math.log2(8)             : 以 2 为底  = {math.log2(8)}")
print(f"math.log(100, 10)        : 自定义底数 = {math.log(100, 10)}")

# 三、三角函数（角度单位用**弧度**）
print("\n三角函数")
angle_rad = math.pi / 4  # 45°
print(f"math.sin(π/4)            : 正弦 = {math.sin(angle_rad)}")
print(f"math.cos(π/4)            : 余弦 = {math.cos(angle_rad)}")
print(f"math.tan(π/4)            : 正切 = {math.tan(angle_rad)}")
print(f"math.degrees(π/4)        : 弧度转角度 = {math.degrees(angle_rad)}")
print(f"math.radians(45)         : 角度转弧度 = {math.radians(45)}")

# 四、反三角函数
print("\n反三角函数")
print(f"math.asin(0.5)           : 反正弦 = {math.asin(0.5)}")
print(f"math.acos(0.5)           : 反余弦 = {math.acos(0.5)}")
print(f"math.atan(1)             : 反正切 = {math.atan(1)}")
print(f"math.atan2(1, 1)         : 双参反正切 = {math.atan2(1, 1)}")

# 五、双曲函数
print("\n双曲函数")
print(f"math.sinh(1)             : 双曲正弦 = {math.sinh(1)}")
print(f"math.cosh(1)             : 双曲余弦 = {math.cosh(1)}")
print(f"math.tanh(1)             : 双曲正切 = {math.tanh(1)}")

# 六、实用函数
print("\n实用函数")
print(f"math.isclose(1.0001, 1.0, rel_tol=1e-3) : 是否近似 = {math.isclose(1.0001, 1.0, rel_tol=1e-3)}")
print(f"math.factorial(5)        : 阶乘 = {math.factorial(5)}")
print(f"math.gcd(18, 24)         : 最大公约 = {math.gcd(18, 24)}")
print(f"math.lcm(4, 6)           : 最小公倍 = {math.lcm(4, 6)}")
print(f"math.fmod(7, 3)          : 浮点取模 = {math.fmod(7, 3)}")
print(f"math.fsum([0.1]*10)      : 精确求和 = {math.fsum([0.1]*10)}")

# 七、数学常量
print("\n数学常量")
print(f"math.pi                  : 圆周率 π = {math.pi}")
print(f"math.e                   : 自然常数 e = {math.e}")
print(f"math.tau                 : 2π = {math.tau}")