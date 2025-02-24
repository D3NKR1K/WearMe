class RBCloth:
    def __init__(self, cloth_id: int | None = None,
                 height: int | None = None,
                 chest: int | None = None,
                 waist: int | None = None,
                 hips: int | None = None):
        self.id = cloth_id
        self.height = height
        self.chest = chest
        self.waist = waist
        self.hips = hips


    def to_dict(self) -> dict:
        data = {'id': self.id, 'height': self.height, 'chest': self.chest, 'waist': self.waist,
                'hips': self.hips}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data