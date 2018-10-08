import numpy as np
import cv2


class Graph:

    def __init__(self, points, connections, centerPoint = 0):
        self.centerPoint = centerPoint
        self.points = points
        self.connections = connections

    def getCurrentPos(self):
        return self.points[self.centerPoint]

    def scale(self, factor):
        for (i, point) in enumerate(self.points):
            self.points[i] = np.multiply(factor, point)

    def translate(self, translation):
        for (i, point) in enumerate(self.points):
            self.points[i] = np.add(point, translation)

    def rotate(self, rotationMatrix):
        currentPos = self.getCurrentPos()
        self.translate(map(lambda v: -v, currentPos))
        for (i, point) in enumerate(self.points):
            self.points[i] = np.dot(rotationMatrix, point)
        self.translate(currentPos)

    def rotateRoundX(self, degrees):
        rotationMatrix = np.asarray([
            [1, 0,               0                ],
            [0, np.cos(degrees), -np.sin(degrees) ],
            [0, np.sin(degrees), np.cos(degrees)  ]
        ])
        self.rotate(rotationMatrix)

    def rotateRoundY(self, degrees):
        rotationMatrix = np.asarray([
            [np.cos(degrees),  0, np.sin(degrees) ],
            [0,                1, 0               ],
            [-np.sin(degrees), 0, np.cos(degrees) ]
        ])
        self.rotate(rotationMatrix)

    def rotateRoundZ(self, degrees):
        rotationMatrix = np.asarray([
            [np.cos(degrees), -np.sin(degrees), 0 ],
            [np.sin(degrees), np.cos(degrees),  0 ],
            [0,               0,                1 ]
        ])
        self.rotate(rotationMatrix)

    def project(self):
        newPoints = []
        for (i, point) in enumerate(self.points):
            newPoints.append([point[0], point[1]])
        newConnections = self.connections
        newGraph = Graph(newPoints, newConnections)
        return newGraph



class Cube(Graph):

    def __init__(self, pos):
        (x,y,z) = pos
        w = 10
        points = []
        points.append([x,y,z])
        points.append([x+w,y,z])
        points.append([x,y+w,z])
        points.append([x,y,z+w])
        points.append([x+w,y+w,z])
        points.append([x+w,y,z+w])
        points.append([x,y+w,z+w])
        points.append([x+w,y+w,z+w])
        connections = []
        connections.append([0,1])
        connections.append([0,2])
        connections.append([0,3])
        connections.append([1,4])
        connections.append([2,4])
        connections.append([2,6])
        connections.append([1,5])
        connections.append([4,7])
        connections.append([3,5])
        connections.append([3,6])
        connections.append([6,7])
        connections.append([5,7])
        Graph.__init__(self, points, connections)




def draw(shape, image):
    flatShape = shape.project()
    for line in flatShape.connections:
        (x1, y1) = flatShape.points[line[0]]
        (x2, y2) = flatShape.points[line[1]]
        point1 = (int(x1), int(y1))
        point2 = (int(x2), int(y2))
        cv2.line(image, point1, point2, (0, 0, 255))

