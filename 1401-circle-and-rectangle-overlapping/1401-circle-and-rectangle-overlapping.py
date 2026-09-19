class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x_close=max(x1,min(xCenter,x2))
        y_close=max(y1,min(yCenter,y2))
        dis_x=xCenter-x_close
        dis_y=yCenter-y_close
        return (dis_x**2+dis_y**2)<=radius**2