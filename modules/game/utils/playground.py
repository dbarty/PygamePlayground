from game.utils.camera import Camera

class Playground:
    def __init__(self, *, camera=None):
        self._camera = camera if camera else Camera(self)

    def __str__(self):
        return f"[Playground camera={self.camera}]"
    def __contains__(self, other):
        ...

    @property
    def camera(self):
        return self._camera