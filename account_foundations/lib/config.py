from yaml import load, FullLoader


class Config:
    @staticmethod
    def load_config(path):
        config_content = ""
        with open(path, "r") as f:
            config_content = f.read()

        config_yaml = load(config_content, Loader=FullLoader)
        return config_yaml