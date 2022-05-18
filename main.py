import PySimpleGUI as sg

seklas=["gurķi","tomāti","burkāni","paprika"]
total = dict.fromkeys(seklas)
print(total)



sg.theme('DarkPurple3')
sg.theme_background_color('#E6B830')

layout = [[sg.Text('Ievadi mājas sēklu skaitu:',key='-OUTPUT-')],
          [sg.Text('Gurķi\t'),sg.Input(key='-m1-')],
          [sg.Text('Tomāti\t'),sg.Input(key='-m2-')],
          [sg.Text('Burkāni\t'),sg.Input(key='-m3-')],
          [sg.Text('Paprika\t'),sg.Input(key='-m4-')],
          [sg.Button('Summa'),sg.Button('Atcelt'),sg.Text(size=(15,1))]]

layout2=[[sg.Text('Ievadi nopirkto sēklu skaitu:',key='-OUTPUT2-')],
[sg.Text('Gurķi\t'),sg.Input(key='v1')],
[sg.Text('Tomāti\t'),sg.Input(key='v2')],
[sg.Text('Burkāni\t'),sg.Input(key='v3')],
[sg.Text('Paprika\t'),sg.Input(key='v4')],
[sg.Button('Summa2'),sg.Button('Atcelt'),sg.Text(size=(15,1))]]

layout3=[[sg.Text('Ievadi sagrauzto sēklu skaitu:', key='-OUTPUT3-')],
[sg.Text('Gurķi\t'),sg.Input(key='s1')],
[sg.Text('Tomāti\t'),sg.Input(key='s2')],
[sg.Text('Burkāni\t'),sg.Input(key='s3')],
[sg.Text('Paprika\t'),sg.Input(key='s4')],
[sg.Button('Summa3'),sg.Button('Atcelt'),sg.Text(size=(15,1))]]

tabgrp = [[sg.TabGroup([[sg.Tab('Mājas', layout,tooltip='tip'), sg.Tab('Veikala', layout2,tooltip='tip2'),sg.Tab('Sagrauztās', layout3,tooltip='tip3')]])]]

window = sg.Window(' Sēklas', tabgrp)

while True:  
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Atcelt':
        break
      
    if event=='Summa':
     total[seklas[0]]=int(values['-m1-'])
     total[seklas[1]]=int(values['-m2-'])
     total[seklas[2]]=int(values['-m3-'])
     total[seklas[3]]=int(values['-m4-'])
     print(total)
     window['-OUTPUT-'].update(total)
      
    if event=='Summa2':
     total[seklas[0]]+=int(values['v1'])
     total[seklas[1]]+=int(values['v2'])
     total[seklas[2]]+=int(values['v3'])
     total[seklas[3]]+=int(values['v4'])
     print(total)
     window['-OUTPUT2-'].update(total)
      
    if event=='Summa3':
     total[seklas[0]]-=int(values['s1'])
     total[seklas[1]]-=int(values['s2'])
     total[seklas[2]]-=int(values['s3'])
     total[seklas[3]]-=int(values['s4'])
     print(total)
     window['-OUTPUT3-'].update(total)
window.close()

