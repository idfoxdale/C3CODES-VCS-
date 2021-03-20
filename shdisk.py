# test of shutils.diskusage module
import shutil
import os
BytesPerGB = 1024 * 1024 * 1024
# Define enquired directory variable prompting input
dsetdir = print(input("Prompt: Define the directory"))

(total, used, free) = shutil.disk_usage(dsetdir)

print ("Total: %.2fGB" % (float(total)/BytesPerGB))
print ("Used:  %.2fGB" % (float(used)/BytesPerGB))

(total1, used1, free1) = shutil.disk_usage(dsetdir)
print ("Total: %.2fGB" % (float(total1)/BytesPerGB))
print ("Used:  %.2fGB" % (float(used1)/BytesPerGB))