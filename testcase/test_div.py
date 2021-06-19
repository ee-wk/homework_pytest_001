# coding=utf-8
import pytest
import yaml

from code.calc_div import div


def get_data():
    with open("../test_data/div.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


class TestAdd:
    @pytest.mark.skip
    def test_get_data(self):
        print(get_data()["success"]["ids"])

    @pytest.mark.parametrize("expect,a,b", get_data()["success"]["data"], ids=get_data()["success"]["ids"])
    def test_div_success(self, expect, a, b):
        assert expect == div(a, b)

    @pytest.mark.parametrize("expect,a,b", get_data()["others"]["data"], ids=get_data()["others"]["ids"])
    def test_div_others(self, expect, a, b):
        try:
            div(a, b)
            raise Exception("没有提示输入数字")
        except Exception as e:
            assert expect in str(e)
