from src.utilities.helpers import Helpers
from conftest import BaseDriver
import pytest

class TestPercyUI(BaseDriver):
    
    @pytest.mark.parametrize('percy_snapshot', Helpers.get_data())
    def test_percy_static_snapshots(self, percy_snapshot):
        h = Helpers
        h.gotoURL(self, percy_snapshot['URL'])
        h.page_scroller(self)
        h.percy_take_snapshot(self, percy_snapshot['SnapTitle'])
