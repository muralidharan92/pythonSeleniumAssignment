import requests
from utils.yaml_reader_utils import YamlReaderUtils


class DecryptUtils:
    @staticmethod
    def decrypter(encrypt):
        """
        Function to decrypt data
        :param encrypt: YAML key
        :return: string: decrypted string
        """
        config = YamlReaderUtils.yaml_reader()
        response = requests.get(url=config["decrypt_base_url"] + "{}".format(encrypt))
        data = response.json()
        return data[encrypt]

