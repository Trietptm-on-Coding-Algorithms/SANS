from ctypes import *
import sys
import string
import glob
minloadaddr = 0x6c000000
maxloadaddr = 0x6d000000
kernel32 = windll.kernel32

if len(sys.argv) == 1:
    print "Usage: dll.py <DLLs to resolve>"
    sys.exit(0)

results = []
for arg in sys.argv[1:]:
    for dllfile in glob.glob(arg):
        try:
            windll.LoadLibrary(dllfile)
        except:
            continue
        loadAddr = kernel32.GetModuleHandleA(dllfile)
        if loadAddr > minloadaddr and loadAddr < maxloadaddr:
            print "\n" + string.upper(dllfile)
            print hex(loadAddr) + " Load Address"
            print hex(loadAddr + 0x1000) + " Text Segment"
            results.append([string.upper(dllfile), loadAddr, loadAddr + 0x1000])
if results != []:
    f = open('dllreport.csv', 'w')
    for dll in results:
        f.write("%s,0x%08x,0x%08x\n" % (dll[0], dll[1], dll[2]))
    f.close()
    print "Report results written to dllreport.csv"
else:
    print "No DLLs match the loadAddr conditions."
