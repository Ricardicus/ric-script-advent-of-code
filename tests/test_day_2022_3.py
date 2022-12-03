import os
from settings import *

def test_day_1():
  os.chdir("../2022")
  output_lines = [
"Part 1: 7701",
"Part 2: 2644"
]

  lib_script = callSample('3.ric')

  ric_result = os.popen(lib_script).read().splitlines()

  assert len(output_lines) == len(ric_result)

  for i in range(0,len(ric_result)):
    assert output_lines[i] == ric_result[i], "denna: " + output_lines[i] + ", verkligt: " + ric_result[i]
