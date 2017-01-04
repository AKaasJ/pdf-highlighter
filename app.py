# Author: Kouveris N. Dimitrios   |   www.dimkouv.me
# Date: 03/01/2016

from highlighter import add_highlights_to_pages
from pdf_word_analyzer import analysis

def run(in_pdf, colors_dict, out_pdf):
	print("running...")
	
	data = analysis(in_pdf)	# Word analysis of the pdf file
	
	words = data["words"]	# All the words of the pdf file
	coordinates = data["coordinates"]	# Coordinates of each word
	pages = data["pages"]	# Page of each word
	total_pages = data["total_pages"]	# Total pages of the pdf
	
	print("Total pages " + str(total_pages))
	
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
	
	# Now we have all the needed words with their coordinates and color inside 'keys dict'
	add_highlights_to_pages(in_pdf, keys, out_pdf, total_pages)


if __name__ == "__main__":
	# TODO read data from csv, txt, excel file
	keys = {"-2.048A": "red",
			"-2.048B": "green",
			"-3.059A": "Yellow",
			"-3.005B": "Blue",
			"1.005A": "Yellow",
			"1.015A": "Blue",
			"0.016A": "Yellow",
			"0.017A": "Blue",
			"keep": "Red",
			"know": "Green",
			"can": "Yellow",
			"piggy": "Blue",
			"kdokoliv": "Green"}
			
	run("input.pdf", keys, "output.pdf")
	run("eminem.pdf", keys, "outputem.pdf")
