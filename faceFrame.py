import engine as e

class FaceFrame(Graph):

    def __init__(self):
        points = []
        connections = []
        Graph.__init__(self, points, connections)

    def align(self, coordinates):
        pass