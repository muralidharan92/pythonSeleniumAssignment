import os
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_parent_keys(d, target_key, parent_key=None):
    for k, v in d.items():
        if k == target_key:
            yield [parent_key, v]
        if isinstance(v, dict):
            for res in get_parent_keys(v, target_key, k):
                yield res


def yaml_reader():
    cwd = os.getcwd()
    filepath = os.path.join(cwd, 'test.yaml')
    # print(filepath)
    with open(r"{}".format(filepath)) as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
        return config_list


output = yaml_reader()
print(output)
print(*get_parent_keys(output, 'test.test4'))


def get_element(driver, locator_list):
    by = locator_list[0]
    by_value = locator_list[1]
    try:
        if by.lower() == "id":
            return driver.find_element_by_id(by_value)
        elif by.lower() == "css_selector":
            return driver.find_element_by_css_selector(by_value)
        elif by.lower() == "class_name":
            return driver.find_element_by_class_name(by_value)
        elif by.lower() == "link_text":
            return driver.find_element_by_link_text(by_value)
        elif by.lower() == "name":
            return driver.find_element_by_name(by_value)
        elif by.lower() == "partial_link_text":
            return driver.find_element_by_partial_link_text(by_value)
        elif by.lower() == "tag_name":
            return driver.find_element_by_tag_name(by_value)
        else:
            raise Exception("Unable to find {} key in the dictionary. Please check spell or file".format(by))
    except NoSuchElementException:
        raise Exception("no such element: Unable to locate element: method: '{}', selector: '{}'".format(by, by_value))


# context = webdriver.Chrome()
print(*get_parent_keys(output, 'test.test4'))
