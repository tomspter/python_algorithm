"""
Name:
Project 2 - Hybrid Sorting - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Any, Dict

def hybrid_sort( data: List[Any], threshold: int ) -> None:
    """
    Fill out docstring here.
    """
    merge_sort( data, threshold )

def inversions_count( data: List[Any] ) -> int:
    """
    Fill out docstring here.
    """

    def merge( arr, left_half, right_half ):
        i, j, k = 0, 0, 0
        inversions = 0
        left_len, right_len = len( left_half ), len( right_half )
        while i < left_len and j < right_len:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                inversions += left_len - i
            k += 1

        while i < left_len:
            arr[k] = left_half[i]
            i, k = i + 1, k + 1

        while j < right_len:
            arr[k] = right_half[j]
            j, k = j + 1, k + 1

        return inversions

    if len( data ) > 1:
        mid = len( data ) // 2
        left_half, right_half = data[:mid], data[mid:]
        inversions = merge_sort( left_half ) + merge_sort( right_half ) + merge( data, left_half, right_half )
        return inversions
    return 0

def merge_sort( data: List[Any], threshold: int = 0 ) -> int:
    """
    Fill out docstring here.
    """
    if (len( data ) > threshold):
        return inversions_count( data )
    return insertion_sort( data )

def insertion_sort( data: List[Any] ) -> None:
    """
    Fill out docstring here.
    """
    if len( data ) == 0:
        return
    for d in range( 1, len( data ) ):
        pointer = data[d]
        counter = d - 1
        while counter >= 0 and pointer < data[counter]:
            data[counter + 1] = data[counter]
            counter = counter - 1
        data[counter + 1] = pointer

def find_match( user_interests: List[str], candidate_interests: Dict[str, List] ) -> str:
    """
    Fill out docstring here.
    """

    def get_key( dict, value ):
        return [k for k, v in dict.items() if v == value][0]

    index_list = list( range( len( user_interests ) ) )
    interests_dict = dict( zip( index_list, user_interests ) )
    new_candidate_interests = { }
    for key, value in candidate_interests.items():
        new_interests_list = []
        for v in value:
            new_interests_list.append( get_key( interests_dict, v ) )
        new_candidate_interests[key] = merge_sort( new_interests_list )
    return min( new_candidate_interests, key=new_candidate_interests.get )
