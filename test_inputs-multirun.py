import pytest
import exercise

@pytest.mark.parametrize(
    'input1, input2, result',
    [   # enter your inputs and output tests into tuple below
        (2, 3, '5\n'),
    ]
)

def test_case(capsys, input1, input2, result):
  
    input_values = [input1, input2]

    exercise.input = lambda prompt: input_values.pop(0)
  
    exercise.main()

    out, err = capsys.readouterr()

    assert out == result, f'for input(s) of {input_values}, the output should be {result} instead of your {out}'
    assert err == ''