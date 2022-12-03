import os
from settings import *

def test_day_1():
  os.chdir("../2021")
  output_lines = [
"Part 1: 655",
"Part 2: ",
"..xx.xxx..xxxx..xx..x..x..xx..x..x.xxx..",
"...x.x..x....x.x..x.x..x.x..x.x..x.x..x.",
"...x.x..x...x..x....x..x.x..x.x..x.x..x.",
"...x.xxx...x...x....x..x.xxxx.x..x.xxx..",
"x..x.x....x....x..x.x..x.x..x.x..x.x.x..",
".xx..x....xxxx..xx...xx..x..x..xx..x..x."
]

  lib_script = callSample('13.ric')

  ric_result = os.popen(lib_script).read().splitlines()

  assert len(output_lines) == len(ric_result)

  for i in range(0,len(ric_result)):
    assert output_lines[i] == ric_result[i], "denna: " + output_lines[i] + ", verkligt: " + ric_result[i]

