import random

import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=1)
def test_rerun():
    assert random.choice([True, False])