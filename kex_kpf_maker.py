import sys
import os
import shutil
import tkinter as tk

from tkinter import filedialog

root = tk.Tk()
root.withdraw()

directory_to_archive = filedialog.askdirectory(title="Choose Directory to Archive into a KPF")
file_name = input("KPF Name? Extension is added automatically: ")
save_path = filedialog.askdirectory(title="Choose Save Path")


def make_kpf():
    archive_path_and_name = os.path.join(save_path, file_name)

    saved_kpf_archive = shutil.make_archive(archive_path_and_name, 'zip', directory_to_archive, None)

    rename_kpf( saved_kpf_archive )

def rename_kpf(file_to_rename):
    os.rename(file_to_rename, file_to_rename.replace(".zip", '.kpf'))
    print("Packaging Complete! Your KPF: " + file_name + ".kpf" + " should be inside of: " + save_path)


if __name__ == "__main__":
    if directory_to_archive == ( () ):
        print("Directory to Archive into a KPF was Null. Either does not exist or User Exited. Closing Program.")
        sys.exit(1)
    if file_name == "":
        print("KPF Name was Null. Either does not exist or User Exited. Closing Program.")
        sys.exit(2)
    if save_path == ( () ):
        print("Save Path was Null. Either does not exist or User Exited. Closing Program. ")
        sys.exit(3)
    make_kpf()
