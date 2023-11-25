import torch

class Building:
    def __init__(self):
        self.buildings = ['Gedung 9', 'Gedung 8', 'Gedung 7', 'Gedung 5', 'Auditorium']
        self.distance_matrix = torch.tensor([
            [0, 3, 2, 5, 6],
            [3, 0, 1, 4, 7],
            [2, 1, 0, 3, 8],
            [5, 4, 3, 0, 9],
            [6, 7, 8, 9, 0]
        ])

    def get_buildings(self):
        return self.buildings

    def get_distance(self, from_building, to_building):
        try:
            from_index = self.buildings.index(from_building)
            to_index = self.buildings.index(to_building)
            return self.distance_matrix[from_index][to_index].item()
        except ValueError:
            return None