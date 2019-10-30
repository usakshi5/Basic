
class SampleTests:
    def test_func(self):
        from Pages.SimpleFunction import Simple
        sim =Simple()
        assert sim.func(3)==3
