# Author: Kouveris N. Dimitrios   |   www.dimkouv.me
# Date: 04/01/2016

def get_input(filename):
	if (filename.endswith(".txt")):
		print("Getting input from txt file...")
		return get_txt_input(filename)
	else:
		print("File should end with .txt")
		return
		
		
def get_txt_input(filename):
	try:
		f = open(filename, "r")
		data = f.read()
	except Exception as e:
		print(e)
		return

	return_data = {}
	data = data.split("\n")
	for entry in data:
		entry_data = entry.replace(" ", "").split(":")
		try:
			word = entry_data[0]
			color = entry_data[1]
			return_data[word] = color
		except Exception as e:
			print("Error reading txt input", e)
			continue
	
	print(return_data)
	return return_data

