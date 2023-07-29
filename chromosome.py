
class Chromosome:
    def __init__(self, size):
        self._chromosomes = [0] * size

    def check_index(self, ind: int) -> bool:
        if (ind < 0) or (ind >= len(self._chromosomes)):
            return False
        return True
    
    def get(self, ind: int) -> int:
        assert self.check_index(ind), f"Given {ind} but the length is {len(self._chromosomes)}"
        return self._chromosomes[ind]

    def set(self, ind: int, val: int) -> None:
        assert self.check_index(ind), f"Given {ind} but the length is {len(self._chromosomes)}"
        self._chromosomes[ind] = val
        return None

    def __str__(self):
        return f"Chromosomes : {self._chromosomes}"

    def __len__(self):
        return len(self._chromosomes)

if __name__ == "__main__":

    c = Chromosome()
    c.set(0, 1)
    c.set(1, 1)
    c.set(2, 1)
    c.set(3, 1)

    print(len(c))
    print(c)
    print(c.get(2))
