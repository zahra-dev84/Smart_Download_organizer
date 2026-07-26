import os
import shutil
import logging
import tkinter as tk
from tkinter import filedialog
from report import save_report

root=tk.Tk()
root.withdraw()



files_type={
    "Image":[".jpg",".png",".gif",".jpeg",".webp"],
    "Videos":[".mp4",".mkv",".avi",".mov"],
    "Audio":[".mp3",".wav"],
    "Documents":[".pdf",".docx",".txt",".xlsx",".pptx"],
    "Applications":[".exe",".msi"],
    "Archives":[".rar",".zip"],
    "Projects":[".py",".js",".html",".css"]
    
}


def get_category(extension):
    for category, extensions in files_type.items():
        if extension in extensions:
            return category
    return "General"


def count_file(folder_path,report):
    for category in files_type:
        
        new_report=os.path.join(folder_path,category)
        if os.path.exists(new_report):
            fils=os.listdir(new_report)
            report[category]=len(fils)
        folders_path=os.path.join(folder_path,"Directories")
        if os.path.exists(folder_path):
            folderr=os.listdir(folders_path)
            report["Directories"]=len(folderr)
    
    
def create_folder(folder_path,category):
    try:
        new_folder=os.path.join(folder_path,category)
        os.makedirs(new_folder,exist_ok=True)
        return new_folder
    except Exception as e:
        print(f"Error creating folder")
        
def move_file(files_path,destination_folder):
    try:
        shutil.move(files_path,destination_folder)
        logging.info(f"moved{files_path}")
    except Exception as e:
        logging.error(f"Error moving file:{e}")


def move_folder(folder_path,folder_name):
    folders_directory=os.path.join(folder_path,"Directories")
    os.makedirs(folders_directory,exist_ok=True)
    shutil.move(
        os.path.join(folder_path,folder_name),folders_directory
    )

def select_folder():
    folder_path=filedialog.askdirectory()
    return folder_path





def organize_files(folder_path):
    report={
    "Image":0,
    "Videos":0,
    "Audio":0,
    "Documents":0,
    "Applications":0,
    "Archives":0,
    "General":0,
    "Directories":0,
    "Projects":0
    }
    if os.path.exists(folder_path):    
        files=os.listdir(folder_path)
        for fil in files:
            files_path=os.path.join(folder_path,fil)
            if os.path.isfile(files_path):
                neme , extenion=os.path.splitext(fil)
                category=get_category(extenion)
                report[category]+=1
                destantion=create_folder(folder_path,category)
                move_file(files_path,destantion)
           
        files= os.listdir(folder_path)
        for fill in files:
            files_path=os.path.join(folder_path,fill)
            if os.path.isdir(files_path):
                if fill in["Directories","Image","Videos","Audio","Documents","Applications","General",     "Archives"]:
                    continue
                move_folder(folder_path,fill)
                report["Directories"]+=1
            
        count_file(folder_path,report)
        save_report(report)
        print("\n======Report=====")
        for key,value in report.items():
            print(f"{key}:{value}")                   
    else:
        logging.error("Folder not found")
        print("folder not found")
    