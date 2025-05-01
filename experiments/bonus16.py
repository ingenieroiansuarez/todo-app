import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text('select files to compress')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='files')

label2 = sg.Text('select destination folder')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('compress')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('File compreser',
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].uptate(value='Compresion completed')


window.close()



