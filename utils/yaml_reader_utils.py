import os

import yaml


class YamlReaderUtils:
    @staticmethod
    def yaml_reader():
        cwd = os.getcwd()
        filepath = os.path.join(cwd, 'configs\\config.yaml')
        print(filepath)
        with open(r"{}".format(filepath)) as file:
            config_list = yaml.load(file, Loader=yaml.FullLoader)
            return config_list



