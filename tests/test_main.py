import pytest
import exercise

def test_exercise(capsys):
  # include below only if testing with inputs
  # input_values = ['some value', 'more values']
  # def mock_input(s):
  #   return input_values.pop(0)
  # exercise.input = mock_input
  # end input testing

  exercise.main()
  out, err = capsys.readouterr()
  
  assert out == "what output should be", "error message"
  assert err == ''