# -*- coding: utf-8 -*-
import os
import shutil
import time
import pytest

now = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 获取实时时间
file_name = f'report_{now}'

pytest.main(['-vs', '--alluredir', './temp'])
os.system(f'allure generate ./temp -o ./report/{file_name} --clean')
f = os.getcwd()
path = f + '\\temp'
shutil.rmtree(path)
