# Author: Kouveris N. Dimitrios   |   www.dimkouv.me
# Date: 03/01/2016

from highlighter import add_highlights_to_pages
from pdf_word_analyzer import analysis
from input_parser import get_input

def run(in_pdf, colors_dict, out_pdf, output_log):
	print("running...")
	
	data = analysis(in_pdf)	# Word analysis of the pdf file
	
	words = data["words"]	# All the words of the pdf file
	coordinates = data["coordinates"]	# Coordinates of each word
	pages = data["pages"]	# Page of each word
	total_pages = data["total_pages"]	# Total pages of the pdf
	
	print("Total pages " + str(total_pages+1))
	
	# Keep only given words in 'keys' dict
	# keys includes [cords, page, color] for each given word
	keys = {}
	for i in range(len(words)):		
		val = words[i].rstrip("\n\r")
		if (val in list(colors_dict)):
			dict = {}
			dict["cords"] = coordinates[i]
			dict["page"] = pages[i]
			dict["color"] = colors_dict[val]
			keys[val] = dict
			
	results = open(output_log, "w")
	
	found_words = []
	for w in words:	# each found word on pdf
		found_words.append(w.encode("utf-8").rstrip("\n\r"))
	
	for given_word in list(colors_dict):
		if given_word not in found_words:	# word not found on pdf
			res = given_word + " : " + colors_dict[given_word] + " : " + "Not found\n"
		else:
			res = given_word + " : " + colors_dict[given_word] + " : " + "Found\n"
		results.write(res)
	results.close
	# Now we have all the needed words with their coordinates and color inside 'keys dict'
	add_highlights_to_pages(in_pdf, keys, out_pdf, total_pages)
	print("Script finished...")


if __name__ == "__main__":
	input_colors = "example_inputs\input.txt"
	input_pdf = "example_inputs\input.pdf"
	output_pdf = "output.pdf"
	output_log = "results.txt"
	
	keys = get_input(input_colors)	
	run(input_pdf, keys, output_pdf, output_log)
