import engine as e


class Reader:

    def __init__(self, fileName):
        self.fileName = fileName

    def parse(self, scaleFactor = 1, translation = None):
        points = []
        connections = []

        for line in open(self.fileName, "r"):
            
            if line.startswith('#'): 
                continue
            
            values = line.split()
            
            if not values:
                continue

            if values[0] == "v": 
                point = []
                for v in values[1:]:
                    point.append(int(float(v) * scaleFactor))
                points.append(point)

            elif values[0] == "f":
                for connection in values[1:]:
                    a,b = connection.split("/")
                    a = int(a) - 1
                    b = int(b) - 1
                    if a == b: 
                        continue
                    elif [a,b] in connections:
                        continue
                    else:
                        connections.append([a,b])

            else:
                continue

        cleanedConnections = []
        l = len(points)
        for conn in connections:
            (a,b) = conn
            if a < l and b < l:
                cleanedConnections.append([a,b])

        return e.Graph(points, cleanedConnections)