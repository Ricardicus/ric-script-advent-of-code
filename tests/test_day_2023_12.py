import os
from settings import *

def test_day_12():
  os.chdir("../2023")
  output_lines = [
          "Part 1: 21",
          "Part 2: 525152"
  ]

  lib_script = callSampleArgs('12.ric', ['small'])

  ric_result = os.popen(lib_script).read().splitlines()

  assert len(output_lines) == len(ric_result)

  for i in range(0,len(ric_result)):
    assert output_lines[i] == ric_result[i], "denna: " + output_lines[i] + ", verkligt: " + ric_result[i]

