import random

class CelluarAutomata():
    def __init__(self):
        self.mapLength = 35
        self.mapWidth = 30
        self.map = [['■' if random.randint(0,100) < 40 else '□' for x in range(self.mapWidth)] for y in range(self.mapLength)]
        self.ShowMap()

    def AutoChange(self):
        for _ in range(4):       #循环次数
            for i in range(self.mapLength):  #遍历二维数组
                for j in range(self.mapWidth):
                    self.CheckThisTile1(i,j)
            self.ShowMap()
        
        # for _ in range(3):       #循环次数
        #     for i in range(self.mapLength):  #遍历二维数组
        #         for j in range(self.mapWidth):
        #             self.CheckThisTile2(i,j)
        #     self.ShowMap() 

    def CheckThisTile1(self,x,y):
        if self.CountRoundWall(1,x,y) >= 5 or self.CountRoundWall(2,x,y) <= 2: 
            self.map[x][y] = '■'

    def CheckThisTile2(self,x,y):
        if self.CountRoundWall(1,x,y) >= 5:
            self.map[x][y] = '■'

    def CountRoundWall(self,dis,x,y):
        wall = 0
        for j in range(-dis,dis+1):
            if y+j < 0 or y+j >= self.mapWidth:
                continue
            for i in range(-dis,dis+1):
                if x+i < 0 or x+i >= self.mapLength:
                    continue
                if self.map[x+i][y+j] == '■':
                    wall += 1
        if self.map[x][y] == '■':
            wall -= 1
        return wall

    def ShowMap(self):
        for i in range(self.mapLength):
            for j in range(self.mapWidth):
                print(self.map[i][j], end = '')
            print('')
        print('')

if __name__ == "__main__":
    cell = CelluarAutomata()
    cell.AutoChange()