#!/usr/bin/python3
import platform,os,sys

def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"


from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
   print("linux")
elif _platform == "darwin":
   print("MAC OS X")
elif _platform == "win32":
   print("Windows")
elif _platform == "win64":
    print("Windows 64-bit")

print("""Python version: %s
dist: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
""" % (
sys.version.split('\n'),
str(platform.dist()),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
))
