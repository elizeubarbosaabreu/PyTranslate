from deep_translator import GoogleTranslator
import PySimpleGUI as sg
import clipboard, webbrowser

sg.theme('SystemDefault')

idiomas = ['auto',
           'af',           
           'ca',
           'de',
           'dv',
           'el',
           'en',
           'eo',
           'et',
           'es',
           'fi',
           'fr',
           'he',
           'hi',
           'hr',
           'hu',
           'hy',
           'id',
           'it',
           'ja',
           'ka',
           'kk',
           'kn',
           'ko',
           'lt',
           'nb',
           'pt',
           'uk',
           'zu',
           'zh']

menu = [
    ['&Arquivo',['&Novo', '&Abrir Texto', '&salvar Texto']],
    ['&Editar',['&Copiar Texto', '&Colar Texto']],
    ['&Ajuda', ['&Manual','&Autor', ['&GitHub', '&Linkedin']]]
    ]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline('Digite ou cole seu texto aqui, escolha o idioma de origem e final e clique em Traduzir...',
                  font=('Any', 15), size=(10000, 15), key='-text-', autoscroll=True)],
    [sg.Stretch(),
     sg.Text('DETECTAR IDIOMA:'),
     sg.Combo(idiomas, default_value='auto',key='-origem-'),
     sg.Text('TRADUZIR PARA:'),
     sg.Combo(idiomas, default_value='en',key='-saida-'),
     sg.Button('Traduzir'),
     sg.Stretch()]
    ]

window = sg.Window('PyTradutor', layout=layout, size=(720, 480), resizable=True)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    elif event in ('Traduzir'):
        origem = values['-origem-']
        saida = values['-saida-']
        conteudo = values['-text-']
        
        try:            
            texto = GoogleTranslator(source=origem, target=saida).translate(conteudo)
        except:
            texto = 'Algo de Errado não está certo!!!'
        window['-text-'].update(texto)
        
    elif event in ('Novo'):
         window['-text-'].update(' ')
    
    elif event in ('Salvar Texto'):
        conteudo = values['-text-']
        filename = sg.popup_get_file('Salve seu arquivo',
                                       title='Salvar Arquivo',
                                       file_types=(("Texto","*.txt"),),
                                       save_as = True,)
        
        with open(filename, 'w', encoding='utf8') as f:
            f.write(conteudo)
    
    elif event in ('Abrir Texto'):
        filename = sg.popup_get_file('Salve seu arquivo',
                                       title='Salvar Arquivo',
                                       file_types=(("Texto","*.txt"),("Outros", "*.*"),),
                                       )
        with open(filename, 'r') as f:
            conteudo = f.read()
            window['-text-'].update(str(conteudo))         
       
    elif event in ('Copiar Texto'):
        conteudo = values['-text-']
        clipboard.copy(conteudo)
        sg.popup_timed('CTRL+C CTRL+V','O texto copiado está na área de transferência...')
    
    elif event in ('Colar Texto'):
        conteudo = values['-text-']
        conteudo += '\n' + clipboard.paste()
        window['-text-'].update(conteudo)
        
    elif event in ('Manual'):
        texto = '''=========== MANUAL ===========

1. Digite, abra ou cole um texto nesta caixa. Você pode usar os atalhos:
     [Arquivo][Abrir Texto] (Para abrir um arquivo de texto plano)
     [Editar][Colar Texto] (Para colar um texto da área de transferência)
 
2. Para traduzir escolha o idioma de origem e o idioma que quer ver a tradução

3. Para copiar para área de transferência use o atalho:
    [Editar][Copiar Texto]
'''
        window['-text-'].update(str(texto))   
        
    
    elif event in ('GitHub'):
        webbrowser.open_new_tab('https://github.com/elizeubarbosaabreu') 
        
    elif event in ('Linkedin'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/')
        
    
window.close()
