import os
import shutil
import logging
from organizer import get_category,count_file,create_folder,move_folder,move_file,select_folder,files_type,organize_files
from report import save_report
import tkinter as tk
from tkinter import filedialog
from gui import create_window




logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

if __name__ =="__main__":
    create_window()

    logging.info("Program finished")
