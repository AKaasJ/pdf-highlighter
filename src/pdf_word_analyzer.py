# Author: Kouveris N. Dimitrios   |   www.dimkouv.me
# Date: 03/01/2016

# PDF Word Analyzer using pdfminer
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure
import sys


# Explanation of analysis:
# 1. Read PDF File
# 2. For each page of PDF file
# 3. Find LTTextBox fields
# 4. Find words inside LTTextBox
# 5. Calculate word coordinates by finding first and last letter  boxes
# TODO for multiple sentences it returns only last letter coordinates
def analysis(pdf_file_path):
	try:
		f = open(pdf_file_path, "rb")
		parser = PDFParser(f)
		doc = PDFDocument(parser)
		rsrcmgr = PDFResourceManager()
		laparams = LAParams()
		device = PDFPageAggregator(rsrcmgr, laparams=laparams)
		interpreter = PDFPageInterpreter(rsrcmgr, device)

	except Exception as e:
		print("Error opening pdf file", e)
		sys.exit(1)

	print("Starting word analysis...")
	words = []
	coordinates = []
	pages = []

	for idx, page in enumerate(PDFPage.create_pages(doc)):
		interpreter.process_page(page)
		layout = device.get_result()
		for x in layout:
			if (type(x).__name__ == "LTTextBoxHorizontal" or type(x).__name__ == "LTTextBoxVertical"):
				for y in x:
					text = y.get_text()
#					word = ""
#					cords = []
#					for z in y:	# for each letter
#						if (z.get_text() != " "):
#							word += z.get_text()
#							try:
#								cords.append(z.bbox)
#							except:
#								continue
#						else:
#							if (word != ""):
#								words.append(word)
#								pages.append(idx)
#								# TODO fix only last letter highlighting
#								coordinates.append(cords[-1])
#								word = ""

					if (text != "" and text not in words):
						words.append(text)
						pages.append(idx)
						coordinates.append(y.bbox)

	print("Word analysis completed...")
	f.close()
	return {"words": words, "pages": pages, "coordinates": coordinates, "total_pages": idx}

