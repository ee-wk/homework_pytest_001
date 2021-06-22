# coding=utf-8
import logging

import allure
import pytest
import yaml




def get_data():
    with open("./test_data/add.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data

@allure.feature("加法运算测试类")
class TestAdd:
    @allure.story("加法运算正常场景")
    @pytest.mark.parametrize("expect,a,b", get_data()["success"]["data"], ids=get_data()["success"]["ids"])
    def test_add_success(self, get_calc_object, expect, a, b):
        allure.dynamic.title("title")
        logging.info(f"执行用例：{a}+{b}={expect}")
        assert expect == get_calc_object.add(a, b)

    @allure.story("加法运算异常场景")
    @pytest.mark.parametrize("expect,a,b", get_data()["others"]["data"], ids=get_data()["others"]["ids"])
    def test_add_others(self, get_calc_object, expect, a, b):
        logging.info(f"执行用例：{a}+{b}={expect}")
        try:
            get_calc_object.add(a, b)
            raise Exception("没有提示输入数字")
        except Exception as e:
            assert expect in str(e)
