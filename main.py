import PySimpleGUI as sg

seklas=["gurķi","tomāti","burkāni","paprika"]
total = dict.fromkeys(seklas)
print(total)



sg.theme('DarkPurple3')
sg.theme_background_color('#E6B830')

layout = [[sg.Text('Ievadi mājas sēklu skaitu:')],
          [sg.Text('Gurķi\t'),sg.Input(key='in1')],
          [sg.Text('Tomāti\t'),sg.Input(key='in2')],
          [sg.Text('Burkāni\t'),sg.Input(key='in3')],
          [sg.Text('Paprika\t'),sg.Input(key='in4')],
          [sg.Button('Summa'),sg.Button('Atcelt'),sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Text('Ievadi nopirkto sēklu skaitu:')],
          [sg.Text('Gurķi\t'),sg.Input(key='in5')],
          [sg.Text('Tomāti\t'),sg.Input(key='in6')],
          [sg.Text('Burkāni\t'),sg.Input(key='in7')],
          [sg.Text('Paprika\t'),sg.Input(key='in8')],
          [sg.Button('Summa2'),sg.Button('Atcelt'),sg.Text(size=(15,1),key='-OUTPUT2-')],
          [sg.Text('Ievadi sagrauzto sēklu skaitu:')],
          [sg.Text('Sagrauztas\t'),sg.Input(key='in9')],
          [sg.Button('Summa3'),sg.Button('Atcelt'),sg.Text(size=(15,1), key='-OUTPUT3-')]]


window = sg.Window(' Sēklas', layout)

while True:  
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Atcelt':
        break
      
    seklas=["gurķi","tomāti","burkāni","paprika"]
    vv=[]
    vv.append(int(values['in1']))
    vv.append(int(values['in2']))
    vv.append(int(values['in3']))
    vv.append(int(values['in4']))
    dd=zip(seklas,vv)
    ddd=dict(dd)
    sam=sum(ddd.values())
    print(dd)
    print(sam)
  
    seklas2=["gurķi","tomāti","burkāni","paprika"]
    vv2=[]
    vv2.append(int(values['in5']))
    vv2.append(int(values['in6']))
    vv2.append(int(values['in7']))
    vv2.append(int(values['in8']))
    bb=zip(seklas2,vv2)
    bbb=dict(bb)
    samm=sum(bbb.values())
    print(bb)
    print(samm)
    print((samm+sam)-int(values['in9']))


  
    if event=='Summa':
      window['-OUTPUT-'].update(sam)
    if event=='Summa2':
      window['-OUTPUT2-'].update(samm+sam)
    if event=='Summa3':
      window['-OUTPUT3-'].update((samm+sam)-int(values['in9']))
  
window.close()

#visi cipari laikam jāievada vienlaicīgi citādi neiet