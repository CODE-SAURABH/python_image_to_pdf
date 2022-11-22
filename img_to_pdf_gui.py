from tkinter import *
from PIL import  Image
import os
from tkinter import filedialog

# GUI application window
win = Tk()
win.title('Img to Pdf converter application')
win.geometry('400x200')
win.resizable(0,0)

def disable(btn):
    btn['state']='disabled'

def enable(btn):
    btn['state']='active'

files = {}
def upload_imgs():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')],
    initialdir = os.getcwd(), title='Select File/Files')
    if len(files['filename'])!=0:
        enable(download_button)
    

def saveas():
    try:
        img_list = []
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File')
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        disable(download_button)
    except:
        return
# upload button
upload_button = Button(win, text='UPLOAD IMAGES', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='green', command=upload_imgs)
upload_button.grid(row =2, column = 0, padx=90, pady =20)

# Download button
download_button = Button(win, text='Download PDF', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='red', command=saveas)
download_button.grid(row=3, column=0)
disable(download_button)


win.mainloop()