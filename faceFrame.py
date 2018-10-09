import engine as e
import numpy as np

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
            [6, 13, 0],  # mund l
            [14, 13, 0], # mund r
            [9,  20, 0], # kinn l
            [11, 20, 0],  # kinn r
            [9, -12, 0],  # kopf l
            [11, -12, 0],  # kopf r
            [9, -10, 0],  # haar l
            [11, -10, 0],  # haar r
            [10, 0, 0] #midpoint
        ]
        connections = [
            [0, 1], # stirn
            [2, 3], # linkes auge
            [4, 5], # rechtes auge
            [6, 7], # nase
            [8, 9], # mund
            [10, 11], # kinn
            [12, 13], # kopf
            [14, 15] # haar
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
    # 3.1: rotation around z axis
        xCornerRightEyeSupposed = self.points[5][0]
        xCornerRigthEye = coordinates[45][0]
        rate = float(xCornerRigthEye) / float(xCornerRightEyeSupposed)
        if rate < 1 and -1 < rate:
            above = (self.points[1][1] > self.points[0][1])
            if above: 
                angle = np.arccos(rate)
                self.rotateRoundZ(angle)
            else:
                angle = np.arccos(-rate)
                self.rotateRoundZ(angle)

        