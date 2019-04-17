# change_project_name.py

import os
import sys
import shutil
import glob

initial_folder = os.path.abspath(".")

#arguments
old_project = sys.argv[1]
new_project = sys.argv[2]


# def rename_project_iml(path_folder, new_name):

# 	path = path_folder + os.sep +'*.iml'
# 	files = glob.glob(path)

# 	for f in files
# 		os.rename(f, path_folder + os.sep + new_name)
# 		break

def get_project_iml(path_folder):
	path = path_folder + os.sep +'*.iml'
	files = glob.glob(path)

	print(files)
	for f in files:
		return f
		break
	return None

def replace_text(path_file, old_text, new_text):
	f = open(path_file, "r")
	file_text = f.read()
	f.close()
	t = file_text.replace(old_text, new_text)
	f = open(path_file, "w")
	f.write(t)
	f.close()



def init_script():
	project_iml = get_project_iml(initial_folder)
	if (project_iml is not None):
		replace_text(project_iml, old_project, new_project)
		os.rename(project_iml, initial_folder + os.sep + new_project)

	workspace = initial_folder + os.sep + ".idea" + os.sep + "workspace.xml"
	replace_text(workspace, old_project, new_project)

	modules = initial_folder + os.sep + ".idea" + os.sep + "modules.xml"
	replace_text(modules, old_project, new_project)


	print("finished success")

init_script()
