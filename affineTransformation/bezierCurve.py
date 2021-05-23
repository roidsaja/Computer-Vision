from matplotlib import pyplot
import numpy, bezier, seaborn

# Cubic Bezier
(x1, y1) = (0.0, 0.0)
(x2, y2) = (0.3, 0.8)
(x3, y3) = (0.7, 0.7)
(x4, y4) = (0.9, 0.9)
nodes1 = numpy.asfortranarray([
    [x1, x2, x3, x4],
    [y1, y2, y3, x4],
])
# 4 points regression by
curve1 = bezier.Curve(nodes1, degree=3)
ax = curve1.plot(num_pts=256, color=(1, 0, 0, 1))
pyplot.scatter(x1, y1, s=10, color='blue')
pyplot.scatter(x2, y2, s=10, color='blue')
pyplot.scatter(x3, y3, s=10, color='blue')
pyplot.scatter(x4, y4, s=10, color='blue')
pyplot.title("Cubic")
pyplot.savefig("cubic_bezier.png")

# Quadratic Bezier
(x1, y1) = (0.0, 1.0)
(x2, y2) = (0.0, 0.0)
(x3, y3) = (1.0, 0.0)
nodes2 = numpy.asfortranarray([
    [x1, x2, x3],
    [y1, y2, y3],
])
# 3 points regression by
curve2 = bezier.Curve(nodes2, degree=2)
ax = curve2.plot(num_pts=256, color=(1, 0, 0, 1))
pyplot.scatter(x1, y1, s=10, color='green')
pyplot.scatter(x2, y2, s=10, color='green')
pyplot.scatter(x3, y3, s=10, color='green')
pyplot.title("Quadratic")
pyplot.savefig("quadratic_bezier.png")

pyplot.show()