import os
import shutil
dirname = "/opt/webapp"
newdir = "/opt/test"
for flodername, subfolders, filenames in os.walk(dirname):
	for i in filenames:
		if i.endswith('.jpg'):
			shutil.copy(os.path.join(flodername, i), newdir)
