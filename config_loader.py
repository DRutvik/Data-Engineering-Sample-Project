import yaml


class ConfigLoader:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            self.data = yaml.safe_load(f)

    def get(self, key):
        return self.data.get(key)
