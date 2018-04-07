import ipfsapi
from subprocess import call



if __name__ == "__main__":
	try:
		ipfs_api = ipfsapi.connect('127.0.0.1', 5001)
		choice = input("1.Upload file 2.Download file 3.Upload Directory: ")
		if choice == '1':
			file_path = input("Enter file path : ")
			try:
				call("cd " + file_path)
				file_name = input("Enter file name : ")
				try:
					new_file = ipfs_api.add(file_name)
					try:
						with(open("save_data_address.txt","w+")) as file:
							file.write(new_file)
						choice2 = input("Want to pin file? press Y : ")
						if choice2 == "Y":
							ipfs_api.pin_ls(new_file['Hash'])
					except:
						pass
				except:
					pass
			except:
				pass
		if choice == '2':
			key = input("Please enter key : ")
			_type = input("Enter file type : ")
			ipfs_api.cat(key)
			call("mv " + str(key) + str(_type)) #Linux
			call("rename " + str(key) + str(_type))
		if choice == '3':
			choice3 = input("1.Upload by file type 2.upload all : ")
			file_path = input("Enter file path where directory is present : ")
			try:
				call("cd " + file_path)
				if choice3 == '1':
					_type = input("Enter file types : ")
					directory_name = input("Enter directory name : ")
					try:
						files = ipfs_api.add(directory_name,match = "*." + str(_type))
						with(open("save_data_address.txt","w+")) as file:
							file.write(files)
					except:
						pass
				if choice3 == '2':
					directory_name = input("Enter directory name : ")
					try:
						files = ipfs_api.add(directory_name,recursive = True)
						with(open("save_data_address.txt","w+")) as file:
							file.write(files)
					except:
						pass
			except:
				pass
	except ipfsapi.exceptions.ConnectionError as ce:
		print(str(ce))