# coding=utf-8
import pytest
import yaml

from code.clac_add import add


def get_data():
    with open("../test_data/add.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


class TestAdd:
    @pytest.mark.skip
    def test_get_data(self):
        print(get_data()["success"]["ids"])

    @pytest.mark.parametrize("expect,a,b", get_data()["success"]["data"], ids=get_data()["success"]["ids"])
    def test_add_success(self, expect, a, b):
        assert expect == add(a, b)

    @pytest.mark.parametrize("expect,a,b", get_data()["others"]["data"], ids=get_data()["others"]["ids"])
    def test_add_others(self, expect, a, b):
        try:
            add(a, b)
            raise Exception("没有提示输入数字")
        except Exception as e:
            assert expect in str(e)
