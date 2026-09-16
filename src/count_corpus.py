from pathlib import Path
from pypdf import PdfReader


def load():
    """Load all PDF files from the data directory."""
    dir_path = Path("data")
    files = [f for f in dir_path.iterdir() if f.is_file()]
    
    return files


def count(files):
    """Count total pages and words across all files."""
    num_pages = 0
    num_words = 0

    for file in files:
        reader = PdfReader(file)

        for page in reader.pages:
            num_pages += 1

            text = page.extract_text()

            if text:
                words = text.split()
                num_words += len(words)

    return num_pages, num_words


def report(num_pages, num_words):
    """Print the final report."""
    print("Total pages:", num_pages)
    print("Total words:", num_words)


# Main program
files = load()

num_pages, num_words = count(files)

report(num_pages, num_words)