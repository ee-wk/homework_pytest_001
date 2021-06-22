# coding=utf-8
import logging

import allure
import pytest
import yaml


def get_data():
    with open("./test_data/div.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data

@allure.feature("除法运算测试类")
class TestDiv:
    @allure.story("除法运算正常场景")
    @pytest.mark.parametrize("expect,a,b,title", get_data()["success"]["data"], ids=get_data()["success"]["ids"])
    def test_div_success(self, get_calc_object, expect, a, b, title):
        allure.dynamic.title(title)
        logging.info(f"执行用例：{a}/{b}，预期：{expect}")
        assert expect == get_calc_object.div(a, b)

    @allure.story("出发运算异常场景")
    @pytest.mark.parametrize("expect,a,b,title", get_data()["others"]["data"], ids=get_data()["others"]["ids"])
    def test_div_others(self, get_calc_object, expect, a, b, title):
        allure.dynamic.title(title)
        logging.info(f"执行用例：{a}/{b}，预期：{expect}")
        try:
            get_calc_object.div(a, b)
            raise Exception("没有提示输入数字")
        except Exception as e:
            assert expect in str(e)
