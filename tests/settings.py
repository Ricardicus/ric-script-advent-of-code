import os

EXECUTABLE = "../ric-script/ric"

def callSample(sample):
  os.chdir("../2021")

  if (os.name == 'nt'):
    # Windows
    binaryPath = os.path.join('..', 'ric-script', 'ric.exe')
    samplePath = os.path.join(sample)
    return '{0} {1} '.format(binaryPath, samplePath)
  else:
    # Not windows
    return "./{0} {1} ".format(EXECUTABLE, sample)

def callSampleArgs(sample, args):
  os.chdir("../2021")

  if (os.name == 'nt'):
    # Windows
    binaryPath = os.path.join('..', 'ric-script', 'ric.exe')
    samplePath = os.path.join(sample)
    return '{0} {1} {2}'.format(binaryPath, samplePath, ' '.join(str(a) for a in args))
  else:
    # Not windows
    return './{0} {1} {2}'.format(EXECUTABLE, sample, ' '.join(str(a) for a in args))
