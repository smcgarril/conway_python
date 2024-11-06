from collections import defaultdict

ALIVE = " ♥ "
DEAD = " ‧ "

class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern
    
    def evolve(self):
        neighbors = (
            (-1, -1),
            (-1, 0), 
            (-1, 1),
            (0, -1), 
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        )

        num_neighbors = defaultdict(int)

        for row, col in self.pattern.alive_cells:
            for dr, dc in neighbors:
                r, c = row + dr, col + dc
                num_neighbors[(r, c)] += 1
        
        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells

        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive


    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(''.join(display_row))
        return "\n".join(display)


    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"Alive cells -> {sorted(self.pattern.alive_cells)}"
        )