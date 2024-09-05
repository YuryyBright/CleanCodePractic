# common problem

# def mark_coordinate(grid, coord):
#     if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
#         grid[coord] = MARKED


# Solution

class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)
        self.cells = {}

    def __contains__(self, coord):
        return coord in self.limits

    def __setitem__(self, coord, value):
        if coord in self:
            self.cells[coord] = value
        else:
            raise ValueError("Координата виходить за межі")

    def __getitem__(self, coord):
        return self.cells.get(coord, None)  # Повертає None, якщо координата не помічена


def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = 'MARKED'
    else:
        raise ValueError("Координата виходить за межі")


grid_ = Grid(3, 5)

mark_coordinate(grid_, (2, 4))

# print(grid_.cells)


from collections import defaultdict

class CallCount:
    def __init__(self):
        """Ініціалізує об'єкт CallCount з нульовими лічильниками для кожного аргументу."""
        self._counts = defaultdict(int)

    def __call__(self, argument):
        """Збільшує лічильник для переданого аргументу та повертає його значення."""
        self._counts[argument] += 1
        return self._counts[argument]

    def get_count(self, argument):
        """Повертає кількість викликів для переданого аргументу."""
        return self._counts[argument]

# Приклад використання
call_counter = CallCount()
