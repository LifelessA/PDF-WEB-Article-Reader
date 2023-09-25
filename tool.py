import requests
from bs4 import BeautifulSoup
import pyttsx3
import PyPDF2
import os

def speak(text, rate=None, language=None):
    if language == 'hi':
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[-2].id)
        engine.setProperty('pitch', 10.8)
        engine.setProperty('rate',rate)
        engine.say(text)
        engine.runAndWait()
    if language == 'en' or language == None:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.setProperty('rate',rate)
        engine.say(text)
        engine.runAndWait()


def extract_paragraphs_from_page(pdf_file_path, page_number):
    """Extracts all paragraphs present in the specified page of the PDF file.

    Args:
        pdf_file_path: The path to the PDF file.
        page_number: The page number to extract paragraphs from.

    Returns:
        A list of strings, each string representing a paragraph.
    """

    paragraphs = []

    # Open the PDF file in read-binary mode using PdfFileReader
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Get the specified page
        page = pdf_reader.getPage(page_number - 1)  # Page numbers are 0-based

        # Extract text from the page
        text = page.extractText()

        # Split the text into paragraphs
        for line in text.splitlines():
            if line.strip():
                paragraphs.append(line)

    return paragraphs


def extract_text_from_pdf(pdf_file_path,words_size):
    try:
        # Open the PDF file in read-binary mode
        with open(pdf_file_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)

            # Initialize an empty list to store the extracted text chunks
            extracted_text_chunks = []

            # Loop through each page in the PDF
            for page_number in range(pdf_reader.numPages):
                # Get the page
                page = pdf_reader.getPage(page_number)
                    
                # Extract text from the page
                page_text = page.extractText()

                # Split the page_text into chunks of 2000 words
                words = page_text.split()
                chunk_size = words_size
                current_chunk = []

                for word in words:
                    if len(' '.join(current_chunk + [word])) <= chunk_size:
                        current_chunk.append(word)
                    else:
                        extracted_text_chunks.append(' '.join(current_chunk))
                        current_chunk = [word]

                # Append the last chunk if it's not empty
                if current_chunk:
                    extracted_text_chunks.append(' '.join(current_chunk))

            return extracted_text_chunks

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def split_text_into_chunks(text, max_words_per_chunk=2000):
    # Split the text by whitespace into words
    words = text.split()
    # Initialize variables
    chunks = []
    current_chunk = []
    current_word_count = 0
    for word in words:
        # Calculate the word count in the current chunk
        current_word_count += len(word.split())
        if current_word_count <= max_words_per_chunk:
            current_chunk.append(word)
        else:
            # Start a new chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_word_count = len(word.split())
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def html_to_text(url, List_of_tags, help = None):
    if help == "help" or help == "-h":
        print("print(dict['data1 to n'])")
    result = requests.get(url)

    soup = BeautifulSoup(result.text,"html.parser")

    dicT = {}

    for k,item in enumerate(List_of_tags):
        data = []
        if item == "h":
            for j in range(1,6):
                data_1 = soup.find_all(f"h{j}")
                for l in data_1:
                    data.append(l.text)
        else:
            data_2 = soup.find_all(item)
            for m in data_2:
                data.append(m.text)
        # data_name = f"data{k}"
        # exec(f'{data_name} = {data}')
        
        dicT[item] = data

    return dicT



def text_replace(list_1, List_2,chuck):
    for j in range(len(list_1)):
        chuck = chuck.replace(list_1[j],List_2[j])
        chuck = chuck.replace(f"{list_1[j]}�s",f"{List_2[j]}�s")
        chuck = chuck.replace(f"{list_1[j]}'s",f"{List_2[j]}'s")
       
    return chuck







