from pathlib import Path
from pypdf import PdfReader
# Set the path to your directory (use '.' for the current directory)
dir_path = Path('data')

# List only files
files = [f for f in dir_path.iterdir() if f.is_file()]
print(files)
print(len(files))


# Load the PDF file
num_pages = 0
num_words = 0
# Extract and print text from all pages
for file in files:
    reader = PdfReader(file)
    for page_num, page in enumerate(reader.pages):
        num_pages = num_pages + 1
        text = page.extract_text()
        words = text.split()
        num_words = num_words + len(words)

print(num_pages)
print(" ")
print(num_words)