from typing import Dict, List

import pytest
from filter.filter import make_filter


@pytest.mark.parametrize(
    ["keywords", "data", "expected_result"],
    [
        (
            {"name": "polly", "type": "bird"},
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                },
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            ],
            [{"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}],
        ),
        (
            {"name": "poll", "type": "birdy"},
            [
                {
                    "name": "Bill",
                    "last_name": "Gilbert",
                    "occupation": "was here",
                    "type": "person",
                },
                {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
            ],
            [],
        ),
    ],
)
def test_is_armstrong(keywords: Dict, data: List, expected_result: List):
    actual_result = make_filter(**keywords).apply(data)

    assert actual_result == expected_result
