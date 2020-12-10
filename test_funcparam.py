import pytest
import exercise

def test_case():
    
    out = exercise.main('') # enter parameter(s) to test
    result = '' # enter what should be returned

    assert out == result, f'the function should return {result} instead of {out}'