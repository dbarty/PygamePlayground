from game.utils.direction import Directions
from games.pacman.entity.pill import Pill
from games.pacman.entity.wall import Wall

class Grid:
    def __init__(self, step:int=32, infinity=False):
        self._grid = {}
        self._step = step
        self._infinity = infinity
        self._width = 0
        self._height = 0

    def __str__(self):
        return f"[Grid ({self._width}, {self._height})]"

    @property
    def step(self):
        return self._step

    def addXY(self, x, y, entity):
        self._grid[y] = self._grid.get(y, {})  # make sure the row is a dict
        ##self._grid[y][x] = self._grid[y].get(x, {})  # make sure the column exists
        self._grid[y][x] = entity
        self._width = max(self._width, x)
        self._height = max(self._height, y)

    def get(self, x, y):
        try:
            return self._grid[y][x]
        except:
            return None

    def pos_to_index(self, x, y=None) -> tuple:
        if y == None:
            x, y = x

        return (x // self._step, y // self._step)

    def clean_position(self, x, y=None) -> tuple:
        index = self.pos_to_index(x, y)
        return self.index_to_pos(index)

    def index_to_pos(self, x, y=None) -> tuple:
        if y == None:
            x, y = x

        return (x * self._step, y * self._step)

    def update(self) -> None:
        for y in range(self._height + 1):
            for x in range(self._width + 1):
                item = self.get(x, y)

                if not isinstance(item, Pill):
                    continue

                #print("Its a Pill")
                d = Directions.NEUTRAL

                if self._can_move_to(x, y-1):  # check, if UP is possible
                    #print("UP geht")
                    d =  d | Directions.UP

                if self._can_move_to(x, y+1):  # check, if DOWN is possible
                    #print("DOWN geht")
                    d =  d | Directions.DOWN

                if self._can_move_to(x-1, y):  # check, if LEFT is possible
                    #print("LEFT geht")
                    d = d | Directions.LEFT

                if self._can_move_to(x+1, y):  # check, if RIGHT is possible
                    #print("RIGHT geht")
                    d = d | Directions.RIGHT

                #print("d=", d)

                self.addXY(x, y, d) 

    def _can_move_to(self, x, y) -> bool:
        item = self.get(x, y)

        #print("_can_move_to", item)

        if isinstance(item, Wall):
            return False
        
        if (x < 0 or x > self._width) and not self._infinity:
            return False
        
        if (y < 0 or y > self._height) and not self._infinity:
            return False 

        return True       