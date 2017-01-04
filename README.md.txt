@INSTRUCTIONS
I have two sample pdf files (eminem.pdf, input.pdf)
app.py has a dictionary of {word: color}

Run: "python app.py"
It will find all the words of the dictionary and it will create output.pdf and outputem.pdf



@IMPORTANT
Install dependencies first

Run: "pip install pdfminer pypdf2 reportlab"

pdfminer is used to analyze and extract content from pdf file
pypdf2 is used to write the output pdf file
report lab is used to create the highlights



@TODO
- outputem.pdf highlights only last letter of found words
- read input data from txt, csv, excel
- better error handling and debugging information









