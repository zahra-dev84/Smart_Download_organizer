
import os
def save_report(report):
    with open("report.txt","w")as file:
        file.write("=====File Organizern Report")
        for key,value in report.items():
            file.write(f"{key}:{value}\n")