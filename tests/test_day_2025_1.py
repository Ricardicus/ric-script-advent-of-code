import os
from settings import *

def test_day_17():
  os.chdir("../2025")
  output_lines = [
    "Part 1",
    "984",
    "Part 2",
    "5657"
  ]

  lib_script = callSample('1.ric')

  ric_result = os.popen(lib_script).read().splitlines()

  assert len(output_lines) == len(ric_result)

  for i in range(0,len(ric_result)):
    assert output_lines[i] == ric_result[i], "denna: " + output_lines[i] + ", verkligt: " + ric_result[i]

