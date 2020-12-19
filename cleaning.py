# developed in November 2020 Gregor Hildebrand

import os

def main():
	local_app_data = os.path.join(os.environ["LOCALAPPDATA"])
	local_app_data_tmp = local_app_data + os.sep + "Temp" + os.sep

	for root,dirs,files in os.walk(local_app_data_tmp):
		for file in files:
			os.remove(os.path.join(root, file))

if __name__ == "__main__":
	main()
