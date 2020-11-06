import pytest

from sgs.expectations import expectations


@pytest.mark.expectations
def test_expectations_monthly():
    actual = expectations("monthly", "01/01/2020", "01/02/2020").shape
    expected = (4668, 11)

    assert actual == expected


@pytest.mark.expectations
def test_expectations_invalid_resource():
    with pytest.raises(ValueError):
        expectations("foobar", "01/01/2020", "01/02/2020")
