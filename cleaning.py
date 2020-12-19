# developed in November 2020 Gregor Hildebrand

import os

def main():
	local_app_data_tmp = os.environ["TEMP"]
	win_dir = os.environ["Windir"]
	win_tmp = os.path.join(win_dir, "TEMP")
	local_app_data = os.environ["LOCALAPPDATA"]
	local_explorer = os.path.join(local_app_data, "Microsoft","Windows","Explorer")

	for root,dirs,files in os.walk(local_explorer):
		for file in files:
			if file.startswith("thumbcache"):
				os.remove(os.path.join(root, file))

	work_dir = [local_app_data_tmp, win_tmp]

	for i in range(len(work_dir)):
		for root,dirs,files in os.walk(work_dir[i]):
			for file in files:
				os.remove(os.path.join(root, file))

if __name__ == "__main__":
	main()
