from pygame import Vector2

class GridHelper:
    def __init__(self, step=32):
        self._step = step
    
    @property
    def step(self):
        return self._step
    
    @gridstep.setter
    def gridstep(self, step):
        self._step = step

    def posToIndex(self, x, y=None, *, forceVector=False):
        return self._convertIndexPos(x, y, forceVector=forceVector, target="index")

    def indexToPos(self, x, y=None, *, forceVector=False):
        return self._convertIndexPos(x, y, forceVector=forceVector, target="pos")
    
    def _convertIndexPos(self, x, y=None, *, forceVector=False, target="index"):
        if isinstance(x, Vector2):
            print("Its a vector!")
            forceVector = True
            y = x.y
            x = x.x

        if target == "index":
            x //= self._step
            y //= self._step
        elif target == "pos":
            x *= self._step
            y *= self._step
        else:
            raise ValueError("The argument target can only be 'index' or 'pos'.")

        return Vector2(x, y) if forceVector else (x, y)