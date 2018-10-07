import engine as e

class FaceFrame(e.Graph):

    def __init__(self):
        points = [
            [0,  0, 0],  # linke stirn
            [20, 0, 0],  # rechte stirn
            [4,  3, 0],  # linkes auge l
            [8,  3, 0],  # linkes auge r
            [12, 3, 0],  # rechtes auge l
            [16, 3, 0],  # rechtes auge r
            [8,  9, 0],  # nasenspitze l 
            [12, 9, 0],  # nasenspitze r
            [6, 12, 0],  # mund l
            [14, 12, 0], # mund r
            [9,  18, 0], # kinn l
            [11, 18, 0]  # kinn r
        ]
        connections = [
            [0, 1], # stirn
            [2, 3], # linkes auge
            [4, 5], # rechtes auge
            [6, 7], # nase
            [8, 9], # mund
            [10, 11] # kinn
        ]
        e.Graph.__init__(self, points, connections)

    def align(self, coordinates):
        # step 1: position
        stirnLinksX = coordinates[0][0]
        stirnY = coordinates[20][1]
        self.translate([stirnLinksX - self.points[0][0], stirnY - self.points[0][1], 0])
        # step 2: scale
        width = coordinates[16][0] - coordinates[0][0] 
        ownWidth = self.points[1][0] - self.points[0][0]
        self.scale(float(width) / float(ownWidth))
        # step 3: rotation
        # 3.1: rotation around y axis
        widthLeftEye = coordinates[39][0] - coordinates[36][0]
        widthRigthEye = coordinates[45][0] - coordinates[42][0]
        #self.rotateRoundY(10.0*(1.0 - float(widthLeftEye) / float(widthRigthEye)))
        # 3.2 rotation around x axis
        heightLeftEye = coordinates[39][1]
        heightRightEye = coordinates[42][1]
        #self.rotateRoundY(10.0*(1.0 - float(heightLeftEye) / float(heightRightEye)))
        