import pytest

from pathlib import Path
from Comparator.src.JSONComparator import Compare


def test_small_req():
    FILE1_PATH = "Comparator/RequestURLFiles/File1.txt"
    FILE2_PATH = "Comparator/RequestURLFiles/File2.txt"

    File1 = Path(FILE1_PATH)
    File2 = Path(FILE2_PATH)

    obj = Compare()
    obj.json_comparator(File1, File2)


def test_incorrect_files():
    I_FILE1_PATH = "Comparator/RequestURLFiles/IFile1.txt"
    I_FILE2_PATH = "Comparator/RequestURLFiles/IFile2.txt"

    I_File1 = Path(I_FILE1_PATH)
    I_File2 = Path(I_FILE2_PATH)
    obj = Compare()
    obj.json_comparator(I_File1, I_File2)


def test_large_req():
    L_FILE1_PATH = "Comparator/RequestURLFiles/largeFile1.txt"
    L_FILE2_PATH = "Comparator/RequestURLFiles/largeFile2.txt"

    L_File1 = Path(L_FILE1_PATH)
    L_File2 = Path(L_FILE2_PATH)
    obj1 = Compare()
    obj1.json_comparator(L_File1, L_File2)

