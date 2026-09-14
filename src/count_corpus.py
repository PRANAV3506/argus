from pathlib import Path
from pypdf import PdfReader
# Set the path to your directory (use '.' for the current directory)
dir_path = Path('data')

# List only files
files = [f for f in dir_path.iterdir() if f.is_file()]
print(files)
print(len(files))

first_file = files[0]
# with open(first_file, "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)



# Load the PDF file
reader = PdfReader(first_file)

# Extract and print text from all pages
for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"--- Page {page_num + 1} ---")
    print(text)