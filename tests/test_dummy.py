import time

import pytest
import pdb


class TestDummy():

    @pytest.mark.skip
    def test_dummy(self):
        print("dummy 1")
        print("dummy 2")
        self.driver.get("https://www.supersqa.com/")

    @pytest.mark.skip
    def test_page(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(2)

