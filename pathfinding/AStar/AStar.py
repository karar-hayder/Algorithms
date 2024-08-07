import math


class Point:
    def __init__(self,x,y,blocked=False) -> None:
        self.x : int = x
        self.y : int = y
        self.blocked : bool = blocked
        self.nearby_points : list[Point] = list()
        self.perv : Point | None = None
        self.visited = False
        self.g : int = float('inf')
        self.f : int = float('inf')
    def __repr__(self) -> str:
        return f"({self.x},{self.y})"
    def get_cord(self):
        return (self.x,self.y)

def create_grid(rows=10,columns=10) -> list[list[Point]]:
    grid : list[list[Point]] = list()
    for y in range(rows):
        grid.append(list())
        for x in range(columns):
            grid[y].append(Point(x,y))
    return grid

class A_Star:
    def __init__(self,grid) -> None:
        self.grid : list[list[Point]] = grid
        self.__find_nearby()
        

    def find_path(self, start_cord : tuple[int,int], end_cord: tuple[int,int]):

        self.start_point = self.grid[start_cord[1]][start_cord[0]]
        self.end_point = self.grid[end_cord[1]][end_cord[0]]
        self.start_point.f = self.__clac_heuristic(self.start_point)
        searchable = [self.start_point]
        while len(searchable) > 0:
            searchable.sort(key=lambda p: p.f)
            current_point : Point = searchable.pop(0)
            if current_point == self.end_point:
                return self.__return_path()
                
            best_f_score = 99999
            for point in current_point.nearby_points:
                if point.blocked or point.visited:
                    continue
                g_score = current_point.g + self.__cost_from_start_to_n(point)
                if g_score < point.g or point not in searchable:
                    point.f =  g_score + self.__clac_heuristic(point)
                    point.perv = current_point
                    point.visited = True
                    if point not in searchable:
                        searchable.append(point)

        return list()

    def __cost_from_start_to_n(self,n : Point):
        return math.dist(
                        self.start_point.get_cord()
                        ,n.get_cord())

    def __clac_heuristic(self,n : Point):
        return math.dist(
                        n.get_cord()
                        ,self.end_point.get_cord())

    def __find_nearby(self):
        for y,row in enumerate(self.grid):
            for x,point in enumerate(row):
                for y2 in range(-1,2):
                    for x2 in range(-1,2):
                        try:
                            if x2==0 and y2==0:continue
                            if not self.__check_bounds(x, y, x2, y2):
                                near_point = self.grid[y + y2][x + x2]
                                point.nearby_points.append(near_point)

                        except:pass
    def __check_bounds(self, x, y, x2, y2):
        return y + y2 < 0 or y + y2 >= len(self.grid) or x + x2 < 0 or x + x2 >= len(self.grid[0])

    def __return_path(self):
        path = list()
        current : Point = self.end_point
        while current != self.start_point:
            path.append(current)
            current.visited = True
            current = current.perv
        return path[::-1]


if __name__ == "__main__":
    astar = A_Star(create_grid(50,50))
    print(astar.find_path((2,4),(48,43)))
    