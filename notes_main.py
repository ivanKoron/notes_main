from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel,QListWidget, QLineEdit,QTextEdit,QInputDialog   #    
import json

notes = {
    "Добро пожаловать" :{
        "Текст" : "Это самое лучшее приложение для создания заметок",
        "тег" : ["Добро","Инструкция"]
    }
}
with open('notes_data.json',"w",) as file:
    json.dump(notes,file)





app = QApplication([])


main_win = QWidget()
main_win.setWindowTitle("Умные заметки")
main_win.resize(900,600)


LW1 = QListWidget()
LW2 = QListWidget()

fiold_tag = QLineEdit()
fiold_tag.setPlaceholderText('Введите тег')
fiold_Text = QTextEdit()


text1 = QLabel("Список заметок")
text2 = QLabel("список тегов")
Button1 = QPushButton("Создать заметку")
Button2 = QPushButton("Удалить заметку")
Button3 = QPushButton("Сохранить заметку")
Button4 = QPushButton("Добавить к заметке")
Button5 = QPushButton("Открепить от заметки")
Button6 = QPushButton("Искать заметки по тегу")


lineHG = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()

lineV1.addWidget(fiold_Text)
lineV2.addWidget(text1)
lineV2.addWidget(LW1)
lineH1.addWidget(Button1)
lineH1.addWidget(Button2)
lineH2 = QHBoxLayout()
lineH2.addWidget(Button3)
lineV2.addLayout(lineH1)
lineV2.addLayout(lineH2)

lineV2.addWidget(LW2)
lineV2.addWidget(text2)
lineV2.addWidget(fiold_tag)
lineH3 = QHBoxLayout()
lineH3.addWidget(Button4)
lineH3.addWidget(Button5)
lineH4 = QHBoxLayout()
lineH4.addWidget(Button6)
lineV2.addLayout(lineH3)
lineV2.addLayout(lineH4)

lineHG.addLayout(lineV1, stretch = 2)
lineHG.addLayout(lineV2, stretch = 1)
main_win.setLayout(lineHG)

def show_note():
    key = LW1.selectedItems()[0].text()
    print(key)
    fiold_Text.setText(notes[key]["Текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["тег"])
LW1.itemClicked.connect(show_note)

def add_note():
    note_name, ok =  QInputDialog.getText(main_win,"Добавить заметку","название заметки")   #Создание переменных
    if note_name and ok !="":
        notes[note_name] = {"Текст" : "","тег" : []}
        LW1.addItem(note_name)
        list_tags.addItems(notes[note_name]["тег"])
        print(notes)
def save_note():
    if LW1.selectedItems()[0].text(): # сохранение LW1 в notes при условии наличия в нем чего либо 
        key = LW1.selectedItems()[0].text()
        notes[key]['Текст'] = fiold_Text.toPlainText()
        with open('notes_data.json',"r",) as file:
            json.dump(notes,file,sort_keys = True, ensure_anscii = False)
            print(notes)
    else:
        print("Заметка для сохранениия невыбрана")        
def del_note():
    if LW1.selectedItems()[0].text():
        del notes[key]
        list_tags.clear()
        list_notes.clear()
        fiold_Text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json',"r",) as file:
            json.dump(notes,file,sort_keys = True, ensure_anscii = False)
            print(notes)
    else:
        print("заметка для удаления невыбрана")

def add_tag():
    if list_notes.selectedItems():   #проверка на то выбран ли тег 
        key = LW1.selectedItems()[0].text()  
        tag = list_notes.selectedItems()[0].text()
        if not tag and notes[key]['тег']:
            notes[key]['тег'].append(tag)
            list_tags.addItems(tag)
            fiold_tag.clear()
        with open('notes_data.json',"w",) as file:
            json.dump(notes,file,sort_keys = True, ensure_anscii = False)
            print(notes)    
    else:
        print("Заметка для добавления тега недобавлена")
def del_tag():
    if list_notes.selectedItems():   #проверка на то выбран ли тег 
        key = LW1.selectedItems()[0].text()  
        tag = list_notes.selectedItems()[0].text()
        notes[key]['тег'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['тег'])
        with open('notes_data.json',"w",) as file:
            json.dump(notes,file,sort_keys = True, ensure_anscii = False)
        print(notes)    
    else:
        print("тег для удаления не выбран")
        
def search_tag():
    print(Button6.Text())
    tag = fiold_tag.Text()
    if Button6.Text()=="искать заметки по тегу" and  tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['тег']:
                notes_filtered[note] = notes[note]
        Button6.setText("Сбросить поиск") 
        list_tags.clear()   
        list_notes.clear()
        list_notes.addItems(notes)
        print(Button6.Text())
    elif Button6.Text()=="Сбросить поиск":
        list_tags.clear()   
        list_notes.clear()
        list_tag.clear()
        list_notes.addItems(notes)
        Button6.setText("искать заметки по тегу") 
        print(Button6.Text())
    else:
        pass

    
LW1.itemClicked.connect(show_note)
Button1.сlicked.connect(add_note)
Button2.сlicked.connect(del_note)
Button3.сlicked.connect(save_notede)    
Button4.сlicked.connect(add_tag)
Button5.сlicked.connect(del_tag)
Button6.сlicked.connect(search_tag)
main_win.show()
with open('notes_data.json',"r",) as file:
    notes = json.load(file)
LW1.addItems(notes)
app.exec_()