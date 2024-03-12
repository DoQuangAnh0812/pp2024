import zipfile
import os

def compress_data():
    with zipfile.ZipFile("students.dat", "w") as zipf:
        zipf.write("students.txt")
        zipf.write("courses.txt")
        zipf.write("marks.txt")

def decompress_data():
    with zipfile.ZipFile("students.dat", "r") as zipf:
        zipf.extractall()

def check_data_file():
    return "students.dat" in os.listdir()
