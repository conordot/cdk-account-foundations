from yaml import load


class Config:
    @staticmethod
    def load_config(path):
        config_content = ""
        with open(path, "r") as f:
            config_content = f.read()

        config_yaml = load(config_content)
        return config_yaml