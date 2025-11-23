import PyPDF2, os
merger = PyPDF2.PdfMerger()
files = [f for f in os.listdir() if f.endswith('.pdf')]
if files:
    for f in files: merger.append(f)
    merger.write("merged.pdf")
    print("Merged into merged.pdf")
else:
    print("No PDF files found.")