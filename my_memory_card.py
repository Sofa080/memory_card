from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QApplications, QWidget, QHBoxtLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint

class Question ():
    ''' содержит вопрос, правильный ответ и три неправельных '''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3)
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    


question_list = []
question_list.append(
    Question('Государственный язык бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(
    Question('Какого цвета нет в флаге России?', 'Зеленый', 'Красный', 'Белый', 'Синий'))
question_list.append(
    Question('Национальная хижина якутов', 'Ураса', 'Юрта' , 'Ката')


    app = QApplication([])

    btn_OK = QPushButton('Ответить')
    Ib_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответы')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QPushButtonGroup()
RadioGroup.AddButton(rbtn_1)
RadioGroup.AddButton(rbtn_2)
RadioGroup.AddButton(rbtn_3)
RadioGroup.AddButton(rbtn_4)

layout_ans1 = QHBoxtLayout()
layout_ans2 = QVBoxtLayout()
layout_ans3 = QVBoxtLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
Ib Result = QLabel('прав ты или нет?')
Ib Correct = QLabel('ответ будет тут!')

layout_res = QVBoxtLayout()
layout_res.addWidget( Ib_Result, aligment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_Correct, aligment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxtLayout() 
layout_line2 = QHBoxtLayout() 
layout_line3 = QHBoxtLayout()

layout_line1.addWidget(Ib_Question, aligment = (Qt.AlignHCenter | Qt.AlignHCenter ))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

Layout_card = QVBoxtLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show result():
        '''показать панель ответов'''
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers =  [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    '''функция записыввает значение вопроса и ответов в соответствующие виджеты, при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].set.Text(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    Ib_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    '''показать результат - установим переданный текст в надпись "результат" и покажем нужную панель'''
    if answers[0].isCheced():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n - Всего вопросов:' , window.total, '\n-Правильных ответов', window.score)
        print('Рейтинг:' , (window.score/wimdow.total*100), "%")
    else:
        if answers[1].isCheced() or answers[2].isCheced() or answers[3].isCheced():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), "%")
        
def next_question():
    window.total += 1
    print('Статистика\n - Всего вопросов:' , window.total, '\n-Правильных ответов', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить'
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(Layout_card)
window.setWindowTitle('Memo Card')

btn_OK.clicked.connect(click_OK)

window.score = 0
wintow.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()







