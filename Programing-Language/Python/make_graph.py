from caler import *
import random
import numpy as np
import matplotlib.pyplot as plt

num, down, up, d = 100, -100, 100, 100


def make_points(num, down, up):
    points = list()
    for _ in range(num):
        points.append(Point(random.randint(down, up),
                      random.randint(down, up)))
    return points


def make_point(points):
    for point in points:
        plt.scatter(point.x, point.y)


def make_rectangle(rectangle):
    k = 0
    for _ in range(4):
        a = [rectangle[k].x, rectangle[(k + 1) % 4].x]
        b = [rectangle[k].y, rectangle[(k + 1) % 4].y]
        plt.plot(a, b)
        k = (k + 1) % 4


def make_circle(circle):
    xs = np.arange(min(circle.p.x, circle.p.y) - circle.r,
                   max(circle.p.x, circle.p.y) + circle.r, (up - down) / 10000)
    a = circle.p.x + circle.r * np.cos(xs)
    b = circle.p.y + circle.r * np.sin(xs)
    plt.plot(a, b, linestyle='-')


if __name__ == "__main__":
    plt.xlim(down - d, up + d)
    plt.ylim(down - d, up + d)
    plt.axis('equal')

    points = make_points(num, down, up)
    t, rectangle = rotating_calipers(get_convex_by_andrew(points))
    circle = get_min_circle_of_points(points)

    make_point(points)
    make_rectangle(rectangle)
    make_circle(circle)

    plt.show()
