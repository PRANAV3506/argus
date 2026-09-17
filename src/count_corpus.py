from pathlib import Path
from pypdf import PdfReader



def load():
    """Load all PDF files from the data directory."""
    dir_path = Path("data")
    files = [f for f in dir_path.iterdir() if f.is_file()]
    
    return files


def count(files):
    """Count total pages and words across all files."""
    file_stats = {}
    
    num_pages = 0
    num_words = 0
    for file in files:
        reader = PdfReader(file)

        per_file_page = 0
        per_file_words = 0

        for page in reader.pages:
            num_pages += 1
            per_file_page += 1
            text = page.extract_text()

            if text:
                words = text.split()
                num_words += len(words)
                per_file_words += len(words)
        temp = {"pages" : per_file_page , "words" : per_file_words}
        file_stats[file.name] = temp 
    file_final = {"files": len(files),
  "pages": num_pages,
  "words": num_words,
  "per_file": file_stats
  }
    return file_final


def report(stats):
    """Print a summary report of the parsed PDF data."""
    print(f"Files: {stats['files']}")
    print(f"Pages: {stats['pages']}")
    print(f"Words: {stats['words']}\n")
    
    # .items() is the method that returns key-value pairs from a dictionary
    for filename, data in stats['per_file'].items():
        pages = data['pages']
        words = data['words']
        
        # Using f-string formatting for clean column alignment
        # <25 left-aligns the filename in a 25-character block
        # >2 and >7 right-align the numbers so the columns line up perfectly
        print(f"{filename:<25} {pages:>2} pages {words:>7} words")

# Main program
if __name__ == "__main__":
    files = load()
    file_stats = count(files)
    report(file_stats)