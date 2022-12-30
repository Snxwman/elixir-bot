import tomllib as toml

class Config:
    def __init__(self, filepath):
        raw_config = self.load_config(filepath)

        self.discord_token = raw_config['accounts']['discord']['token']


    def load_config(self, filepath):
        with open(filepath, 'rb') as config_file:
            return toml.load(config_file)

