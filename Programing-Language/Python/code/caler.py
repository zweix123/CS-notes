from math import cos, sin, pi
from operator import attrgetter

INF = 1e18
eps = 1e-12  # 精度, 代码中只在比较两浮点数是否相等时使用


def dcmp(a, b):  # 用于比较两浮点数是否相同(实际上也能比较两浮点数大小)
    if abs(a - b) < eps:
        return 0
    return -1 if a < b else 1


class Point():  # 也同Vetor, 可以理解为二维平面的点, 同样可以用来表示一个向量(该向量起点在远点), 类中重载的运算针对向量
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, t):  # 向量加法
        return Point(self.x + t.x, self.y + t.y)

    def __sub__(self, t):  # 向量减法
        return Point(self.x - t.x, self.y - t.y)

    def __truediv__(self, k):  # 向量数乘
        return Point(self.x / k, self.y / k)

    def __mul__(self, k):  # 向量数除
        return Point(self.x * k, self.y * k)

    def dot(a, b):  # 向量点积
        return a.x * b.x + a.y * b.y

    def cross(a, b):  # 向量叉积
        return a.x * b.y - b.x * a.y

    def len(self):  # 如果表示点, 表示点到原点的距离, 如果表示向量, 则是向量的模
        return Point.dot(self, self) ** 0.5

    def dist(a, b):  # 两个点的距离
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def norm(self):  # 返回该向量的法向量
        return self / self.len()

    def rotate(self, angle):  # 向量逆时针旋转angle度数(弧度)
        return Point(self.x * cos(angle) + self.y * sin(angle), -self.x * sin(angle) + self.y * cos(angle))

    def __str__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)


def area(a: Point, b: Point, c: Point):  # 向量ab和ac围城的三角形的有向面积
    return Point.cross(b - a, c - a)


def project(a: Point, b: Point, c: Point):  # 向量ab在ac上的投影长度
    return Point.dot(b - a, c - a) / Point.dist(a, b)


def get_convex_by_andrew(points):  # 利用andres算法求出点集points的凸包(逆时针存储)
    points.sort(key=attrgetter("x", "y"))

    st, top = [None] * (len(points) + 1), 0
    vis = [False] * len(points)

    for i, point in enumerate(points):
        while top >= 2 and area(points[st[top - 2]], points[st[top - 1]], point) <= 0:
            if area(points[st[top - 2]], points[st[top - 1]], point) < 0:
                top = top - 1
                vis[st[top]] = False
            else:
                top = top - 1
        vis[i] = True
        st[top] = i
        top = top + 1

    vis[0] = False
    for i, point in reversed(list(enumerate(points))):
        if vis[i] is True:
            continue
        while top >= 2 and area(points[st[top - 2]], points[st[top - 1]], point) <= 0:
            top = top - 1

        st[top] = i
        top = top + 1

    top = top - 1  # 起始点保存两次
    res = list()
    for i in range(top):
        res.append(points[st[i]])
    return res


def cal_convex_len(points):
    res = 0
    points.append(points[0])
    for i in range(1, len(points)):
        res += Point.dist(points[i], points[i - 1])
    return res


def rotating_calipers(points):
    min_area = INF
    ans = [None] * 4

    n = len(points)
    points.append(points[0])

    a, b, c = 2, 1, 2
    for i in range(len(points[:-1])):
        d, e = points[i], points[i + 1]
        while area(d, e, points[a]) < area(d, e, points[a + 1]):
            a = (a + 1) % n
        while project(d, e, points[b]) < project(d, e, points[b + 1]):
            b = (b + 1) % n
        if i == 0:
            c = a
        while project(d, e, points[c]) > project(d, e, points[c + 1]):
            c = (c + 1) % n

        x, y, z = points[a], points[b], points[c]
        h = area(d, e, x) / Point.dist(e, d)
        w = Point.dot(y - z, e - d) / Point.dist(e, d)
        if h * w < min_area:
            min_area = h * w
            ans[0] = d + (e - d).norm() * project(d, e, y)
            ans[3] = d + (e - d).norm() * project(d, e, z)
            u = (e - d).rotate(-pi / 2).norm()
            ans[1] = ans[0] + u * h
            ans[2] = ans[3] + u * h
    return min_area, ans


def get_line_intersection(p: Point, v: Point, q: Point, w: Point):  # v and w is Vector
    u = p - q
    t = Point.cross(w, u) / Point.cross(v, w)
    return p + v * t


class Line():
    def __init__(self, p: Point, v: Point) -> None:
        self.p = p
        self.v = v


def get_midline(a: Point, b: Point):  # 中垂线
    return Line((a + b) / 2, (b - a).rotate(pi / 2))


class Circle:
    def __init__(self, p: Point, r: float) -> None:
        self.p = p
        self.r = r


def get_circle(a: Point, b: Point, c: Point):  # 三点确定一个圆
    u, v = get_midline(a, b), get_midline(a, c)
    p = get_line_intersection(u.p, u.v, v.p, v.v)
    return Circle(p, Point.dist(p, a))


def get_min_circle_of_points(points):
    from random import shuffle
    shuffle(points)
    c = Circle(points[0], 0)
    for i in range(1, len(points)):
        # if c.r < Point.dist(c.p, points[i]):
        if dcmp(c.r, Point.dist(c.p, points[i])) < 0:
            c = Circle(points[i], 0)
            for j in range(1, i):
                # if c.r < Point.dist(c.p, points[j]):
                if dcmp(c.r, Point.dist(c.p, points[j])) < 0:
                    c = Circle((points[i] + points[j]) / 2,
                               Point.dist(points[i], points[j]) / 2)
                    for k in range(1, j):
                        # if c.r < Point.dist(c.p, points[k]):
                        if dcmp(c.r, Point.dist(c.p, points[k])) < 0:
                            c = get_circle(points[i], points[j], points[k])
    return c


if __name__ == "__main__":
    points = list()
    n = int(input())
    for _ in range(n):
        x, y = tuple(map(float, input().split()))
        points.append(Point(x, y))

    def acwing_1401():
        print("%.2f" % cal_convex_len(get_convex_by_andrew(points)))

    def acwing_2142():
        min_area, ans = rotating_calipers(get_convex_by_andrew(points))

        k = 0
        for i in range(1, 4):
            if dcmp(ans[i].y, ans[k].y) < 0 or dcmp(ans[i].y, ans[k].y) == 0 and dcmp(ans[i].x, ans[k].x) < 0:
                k = i

        print("%.5f" % min_area)
        for _ in range(4):
            print("%.5f %.5f" % (ans[k].x, ans[k].y))
            k = (k + 1) % 4

    def acwing_3028():
        c = get_min_circle_of_points(points)
        print("%.10lf" % c.r)
        print("%.10lf %.10lf" % (c.p.x, c.p.y))

    # acwing_1401()
    # acwing_2142()
    # acwing_3028()
