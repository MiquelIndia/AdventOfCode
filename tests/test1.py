
import sys
sys.path.append('./days/')
import pytest

from exercise1 import calculate_distance_id, calculate_lists_similarity_score


@pytest.mark.parametrize("list1, list2, ids_distance_list", [
    ([3,4,2,1,3,3], [4,3,5,3,9,3], 11),
    ([3,4,2], [4,9,1], 7),
])
def test_calculate_id_lists_distances(list1, list2, ids_distance_list):
    assert calculate_distance_id(list1, list2) == ids_distance_list

@pytest.mark.parametrize("list1, list2, similarity_score", [
    ([3,4,2,1,3,3], [4,3,5,3,9,3], 31),
    ([3,4,2], [4,9,1], 4),
    ([4,9,1], [3,4,2], 4),

])
def test_calculate_lists_similarity_score(list1, list2, similarity_score):
    assert calculate_lists_similarity_score(list1, list2) == similarity_score

