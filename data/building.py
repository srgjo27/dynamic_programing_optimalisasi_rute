# import torch

# class Building:
#     def __init__(self):
#         self.buildings = ['Gedung 9', 'Gedung 8', 'Gedung 7', 'Gedung 5', 'Auditorium']
#         self.distance_matrix = torch.tensor([
#             [0, 3, 2, 5, 6],
#             [3, 0, 1, 4, 7],
#             [2, 1, 0, 3, 8],
#             [5, 4, 3, 0, 9],
#             [6, 7, 8, 9, 0]
#         ])

#     def get_buildings(self):
#         return self.buildings

#     def get_distance(self, from_building, to_building):
#         try:
#             from_index = self.buildings.index(from_building)
#             to_index = self.buildings.index(to_building)
#             return self.distance_matrix[from_index][to_index].item()
#         except ValueError:
#             return None

# class Building:
#     def __init__(self):
#         self.buildings = ['Gedung 9', 'Gedung 8', 'Gedung 7', 'Gedung 5', 'Auditorium']
#         self.edges = {
#             'Gedung 8': {'Gedung 9': 30},
#             'Gedung 8': {'KB': 60},
#             'KB': {'Gedung 9': 60},
#             'Gedung 9': {'Simpang Pohon Bau': 40},
#             'KB': {'Simpang Pohon Bau': 10},
#             'KB': {'Kantor Vokasi': 80},
#             'Simpang Pohon Bau': {'Simpang Gerbang': 325},
#             'Kantor Vokasi': {'OT': 110},
#             'Kantor Vokasi': {'Perpustakaan': 70},
#             'Simpang Gerbang': {'Simpang Bundaran': 45},
#             'Perpustakaan': {'Auditorium': 40},
#             'Perpustakaan': {'Gedung 5': 160},
#             'OT': {'Gedung 5': 90},
#             'Auditorium': {'Gedung 5': 130},
#             'Auditorium': {'Simpang Bundaran': 25},
#             'Auditorium': {'KL': 110},
#             'Simpang Bundaran': {'KL': 30},
#             'KL': {'Gedung 7': 230},
#             'Gedung 5': {'Gedung 7': 70},
#             'OT': {'Gedung 7': 120}
#         }

#     def get_buildings(self):
#         return self.buildings

#     def get_distance(self, from_building, to_building):
#         try:
#             from_index = self.buildings.index(from_building)
#             to_index = self.buildings.index(to_building)
#             return self.edges[from_building][to_building]
#         except ValueError:
#             return None

import torch

class Building:
    def __init__(self):
        self.buildings = ['Gedung 9', 'Gedung 8', 'Gedung 7', 'Gedung 5', 'Auditorium', 'KB', 'Simpang Pohon Bau', 'Kantor Vokasi', 'Simpang Gerbang', 'Perpustakaan', 'OT', 'KL']
        self.edges = {
            'Gedung 8': {'Gedung 9': 30, 'KB': 60},
            'KB': {'Gedung 9': 60, 'Simpang Pohon Bau': 10, 'Kantor Vokasi': 80},
            'Gedung 9': {'Simpang Pohon Bau': 40},
            'Simpang Pohon Bau': {'Simpang Gerbang': 325},
            'Kantor Vokasi': {'OT': 110, 'Perpustakaan': 70},
            'Simpang Gerbang': {'Simpang Bundaran': 45},
            'Perpustakaan': {'Auditorium': 40, 'Gedung 5': 160},
            'OT': {'Gedung 5': 90, 'Gedung 7': 120},
            'Auditorium': {'Gedung 5': 130, 'Simpang Bundaran': 25, 'KL': 110},
            'Simpang Bundaran': {'KL': 30},
            'KL': {'Gedung 7': 230},
            'Gedung 5': {'Gedung 7': 70},
        }

    def get_buildings(self):
        return self.buildings

    def get_distance(self, from_building, to_building):
        try:
            return torch.tensor(self.edges[from_building][to_building], dtype=torch.float32)
        except KeyError:
            return None