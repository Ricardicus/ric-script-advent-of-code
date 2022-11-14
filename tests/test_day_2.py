import os
from settings import *

def test_day():
  os.chdir("../2021")
  output_lines = [
"Part 1: 1692075",
"Part 2: 1749524700"
  ]

  lib_script = callSample('2.ric')

  ric_result = os.popen(lib_script).read().splitlines()

  assert len(output_lines) == len(ric_result)

  for i in range(0,len(ric_result)):
    assert output_lines[i] == ric_result[i], "denna: " + output_lines[i] + ", verkligt: " + ric_result[i]

