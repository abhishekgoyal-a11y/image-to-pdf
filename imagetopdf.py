from tkinter import *
from tkinter.filedialog import askopenfilenames, asksaveasfilename
from PIL import Image
import img2pdf as converter
import zipfile

def openimage():
    global file
    file = askopenfilenames(defaultextension='.png',
                            filetypes=[('All files', '*.*')])
    if file == "":
        file = None
    else:
        root.title("IMAGE TO PDF")


def convertimage():
    for i in range(len(file)):
        image1 = Image.open(file[i])
        im1 = image1.convert('RGB')
        im1.save(f'{file[i].split(".")[0]}.pdf')


def convertimages():
    all_files = []
    for i in range(len(file)):
        image = Image.open(file[i]).convert('RGB')
        image.save(f'{file[i].split(".")[0]}.jpg')
        all_files.append(f'{file[i].split(".")[0]}.jpg')
    askfilename = asksaveasfilename(initialfile="Untit", filetypes=[
        ("All files", "*.*"), ("pdf Document", "*.pdf")])
    files = open(f"{askfilename}.pdf", "wb")
    files.write(converter.convert(all_files))
    files.close()
def convertzip():
    if file!=None:
        askfilename = asksaveasfilename(initialfile="Untit", filetypes=[("zip", "*.zip")])
        my_zip = zipfile.ZipFile(f'{askfilename}.zip','w',compression=zipfile.ZIP_DEFLATED)
        for i in range(len(file)):
            my_zip.write(file[i])
        my_zip.close()

if __name__ == "__main__":
    file = None
    root = Tk()
    root.geometry("400x200")
    root.title("Notepad")
    button1 = Button(root, font="courier 10 bold",
                     text="open", command=openimage)
    button1.place(relx=0.5, y=20, anchor=CENTER)
    button2 = Button(root, font="courier 10 bold", text="convert one image to one pdf",
                     command=convertimage)
    button2.place(relx=0.5, y=50, anchor=CENTER)
    button3 = Button(
        root,  font="courier 10 bold", text="convert All images to one pdf", command=convertimages)
    button3.place(relx=0.5, y=80, anchor=CENTER)
    button4 = Button(
        root,  font="courier 10 bold", text="convert into zip", command=convertzip)
    button4.place(relx=0.5, y=110, anchor=CENTER)

    root.mainloop()
