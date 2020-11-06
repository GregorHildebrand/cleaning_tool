# Copyright (c) 2020 Gregor Hildebrand

import os

def main():
	workdir0 = os.path.expanduser("~/AppData/Local/Temp/")
	workdir1 = os.path.expanduser("~/AppData/Local/Microsoft/Windows/Explorer/")
	workdir2 = os.path.expanduser("~/AppData/Local/Microsoft/INetCache/IE/")
	workdir3 = os.path.expanduser("~/Windows/TEMP/")
	workdir4 = os.path.expanduser("~/AppData/Local/CrashDumps/")
	workdir5 = os.path.expanduser("~/Windows/Logs/")

	working_array = [workdir0, workdir1, workdir2, workdir3, workdir4, workdir5]

	for i in range(len(working_array)):
		if os.path.exists(working_array[i]):
			for root, dirs, files in os.walk(working_array[i]):
				for file in files:
					os.remove(os.path.join(root, file))

	if __name__ == "__main__":
		main()
