import torch

class Building:
    def __init__(self):
        self.graph = {
            'GD 8': {'GD 9': 30, 'KB': 60},
            'GD 9': {'GD 8': 30, 'KB': 60, 'Simpang Pohon Bau': 40},
            'KB': {'GD 8': 60, 'GD 9': 60, 'Simpang Pohon Bau': 10, 'Kantor Vokasi': 80},
            'Simpang Pohon Bau': {'Simpang Gerbang': 325, 'KB': 10, 'GD 9': 40},
            'Kantor Vokasi': {'OT': 110, 'Perpustakaan': 70, 'KB': 80},
            'Simpang Gerbang': {'Simpang Bundaran': 45, 'KL': 230},
            'Perpustakaan': {'Auditorium': 40, 'GD 5': 160, 'Kantor Vokasi': 70},
            'OT': {'GD 5': 90, 'GD 7': 120, 'Kantor Vokasi': 110},
            'Auditorium': {'GD 5': 130, 'Simpang Bundaran': 25, 'KL': 110, 'Perpustakaan': 40},
            'Simpang Bundaran': {'KL': 30, 'Auditorium': 25},
            'KL': {'GD 7': 230, 'Simpang Bundaran': 30},
            'GD 5': {'GD 7': 70, 'Auditorium': 130, 'OT': 90},
            'GD 7': {'GD 5': 70, 'OT': 120, 'KL': 230}
        }

        # Convert graph weights to PyTorch tensors
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.graph[node][neighbor] = torch.tensor(self.graph[node][neighbor], dtype=torch.float)
