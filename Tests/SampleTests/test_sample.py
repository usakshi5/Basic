from Pages.SimpleFunction import Simple
import pytest


class SampleTests:

    def test_func(self):
        sam=Simple()
        assert sam.func(3)==3
