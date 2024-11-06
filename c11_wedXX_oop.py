class Roll:
    def __init__(self, value: tuple):  # receive tuple
        self._content = value  # save to internal;

    @property
    def content(self):
        return self._content

    def __repr__(self) -> str:
        out = "Roll("
        for i in self._content:
            out = f"{out} {i}"
        return out + " )"

    def size(self):
        return len(self._content)


    def get(self, i: int):
        if i < 0 or i >= len(self._content):
            return None
        return self._content[i]
    def sub(self, i: int, j: int):
        return Roll(self._content[i:j + 1])

    def minimum(self):
        size = self.size()
        if size == 0:
            return None
        minimum = self.get(0)
        next_index = 1
        while next_index < size:
            next_value = self.get(next_index)
            if next_value < minimum:
                minimum = next_value
            next_index = next_index + 1
        return minimum


r = Roll((299, 445, 42345, 2345, 345))
print(r)
