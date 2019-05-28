class Eut:
    def __init__(self):
        self.name = "Empty"
        self.project_num = "Empty"
        self.height = 0.0
        self.width = 0.0
        self.depth = 0.0
        self.client = "Empty"
        self.antennas = 0
        self.radios = 0
        self.regions = "Empty"

    def __init__(self, in_name, in_antennas, in_radios, in_regions):
        self.name = in_name
        self.antennas = in_antennas
        self.radios = in_radios
        self.in_region = in_regions
        self.height = 0.0
        self.width = 0.0
        self.depth = 0.0
        self.project_num = "Empty"
        self.client = "Empty"
        self.regions = "Empty"
