import tkinter
import tkinter.ttk as ttk
import tkinter.font as tkfont
import requests
from PIL import Image, ImageTk
import html
import random
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = tkinter.Tk()


def checkIfDuplicates(arr: list) -> bool:
    return len(arr) != len(set(arr))


# -------------------------------------------------------------------------------------------------------------------
def gotonaming():
    try:
        if 1 <= int(playerCountEntry.get()) <= 12:  # testing
            # actual function
            global player_count
            player_count = int(playerCountEntry.get())
            welcoming.destroy()
            playerCountlbl.destroy()
            playerCountEntry.destroy()
            playerCountBtn.destroy()
            namesgrid()
    except ValueError:
        pass


# for i in range(0,8):
#    Label().grid(row=0, column=i, sticky="ew")
welcoming = ttk.Label(
    master=window,
    text="Welcome to the funny quiz!!!!!!!!!!!",
    font=("TkDefaultFont", 16)
)
welcoming.grid(row=0, column=8)

window.grid_columnconfigure((0, 9), weight=1)

playerCountlbl = ttk.Label(
    master=window,
    text="How many players? (1-12):",
)
playerCountlbl.grid(row=6, column=8)

playerCountEntry = ttk.Entry()
playerCountEntry.grid(row=7, column=8)

playerCountBtn = ttk.Button(text="Start!", command=gotonaming)
playerCountBtn.grid(row=8, column=8)


# window.grid_rowconfigure((6, 8), weight=1)

# ------------------------------------------------------------------------------------------------------------------

def namesgrid():
    window.grid_columnconfigure((0, 9), weight=0)
    global name_entries
    global player_add_name_labels
    name_entries = []
    player_add_name_labels = []

    for i in range(player_count):
        entry = ttk.Entry()
        name_entries.append(entry)

        name_entries[i].grid(row=i, column=0)

        player_add_name_label = ttk.Label(text=f"Player {i + 1}")
        player_add_name_labels.append(player_add_name_label)

        player_add_name_labels[i].grid(row=i, column=1)

    global tmp_lbl
    tmp_lbl = ttk.Label(text="Add names")
    tmp_lbl.grid(row=20, column=0)
    global start_btn
    start_btn = ttk.Button(text="Start!", command=getnames)
    start_btn.grid(row=20, column=1)


def getnames():
    global names
    names = []

    for entry in name_entries:
        names.append(entry.get())

    if checkIfDuplicates(names) is False:
        for name_entry in name_entries:
            name_entry.destroy()

        for name_label in player_add_name_labels:
            name_label.destroy()

        tmp_lbl.destroy()
        start_btn.destroy()
        print(names)
        start()


def clicked(button):
    global current_question_num
    global correct_answer
    global imgBtnA
    global imgBtnB
    global imgBtnC
    global imgBtnD
    global lastquestionstatuslbl
    global quiznamelbl
    global current_question_text
    global answers
    global questionlbl
    global difficulty
    global questioncountlbl
    global playerlbl
    global questiondifficultylbl

    if button == "A":
        if imgBtnA.cget("text") == correct_answer:
            scores[names.index(namesorder[current_question_num])] += 1
            lastquestionstatuslbl.config(text="Last Question: Correct!", foreground="green")
        else:
            lastquestionstatuslbl.config(text="Last Question: Wrong", foreground="red")

    elif button == "B":
        if imgBtnB.cget("text") == correct_answer:
            scores[names.index(namesorder[current_question_num])] += 1
            lastquestionstatuslbl.config(text="Last Question: Correct!", foreground="green")
        else:
            lastquestionstatuslbl.config(text="Last Question: Wrong", foreground="red")

    elif button == "C":
        if imgBtnC.cget("text") == correct_answer:
            scores[names.index(namesorder[current_question_num])] += 1
            lastquestionstatuslbl.config(text="Last Question: Correct!", foreground="green")
        else:
            lastquestionstatuslbl.config(text="Last Question: Wrong", foreground="red")

    elif button == "D":
        if imgBtnD.cget("text") == correct_answer:
            scores[names.index(namesorder[current_question_num])] += 1
            lastquestionstatuslbl.config(text="Last Question: Correct!", foreground="green")
        else:
            lastquestionstatuslbl.config(text="Last Question: Wrong", foreground="red")

    if current_question_num == len(namesorder) - 1:  # name order is len, current question num is index
        imgBtnA.destroy()
        imgBtnB.destroy()
        imgBtnC.destroy()
        imgBtnD.destroy()
        lastquestionstatuslbl.destroy()
        quiznamelbl.destroy()
        questiondifficultylbl.destroy()
        playerlbl.destroy()
        questionlbl.destroy()
        questioncountlbl.destroy()
        end()
    else:
        current_question_num += 1
        print(current_question_num)

        current_question_text = html.unescape(questions[current_question_num]['question'])

        answers = questions[current_question_num]['incorrect_answers'].copy()
        answers.append(questions[current_question_num]['correct_answer'])

        for i in range(len(answers)):
            answers[i] = html.unescape(answers[i])

        questionlbl.config(text=current_question_text)

        correct_answer = html.unescape(questions[current_question_num]['correct_answer'])
        print(correct_answer)

        difficulty = html.unescape(questions[current_question_num]['difficulty'])

        questioncountlbl.config(text=f"Question {current_question_num + 1}/{len(names) * 10}")

        playerlbl.config(text=f"Player: {namesorder[current_question_num]}")

        questiondifficultylbl.config(text=f"Difficulty: {difficulty}")

        random.shuffle(answers)

        imgBtnA.config(text=answers[0])
        imgBtnB.config(text=answers[1])
        imgBtnC.config(text=answers[2])
        imgBtnD.config(text=answers[3])


def start():
    global questions
    font = tkfont.Font(size=16)
    image = Image.open(resource_path("button_sprite.png"))
    btnimage = ImageTk.PhotoImage(image)
    global imgBtnA
    imgBtnA = tkinter.Button(window, image=btnimage, text="A", compound="center", font=font)
    global imgBtnB
    imgBtnB = tkinter.Button(window, image=btnimage, text="B", compound="center", font=font)
    global imgBtnC
    imgBtnC = tkinter.Button(window, image=btnimage, text="C", compound="center", font=font)
    global imgBtnD
    imgBtnD = tkinter.Button(window, image=btnimage, text="D", compound="center", font=font)
    imgBtnC.place(
        relx=0.0,
        rely=1.0,
        anchor="sw"
    )
    imgBtnD.place(
        relx=1.0,
        rely=1.0,
        anchor="se"
    )
    imgBtnA.place(
        x=0,
        y=270
    )
    imgBtnB.place(
        x=530,
        y=270
    )
    global playerlbl
    playerlbl = ttk.Label(text="Player:", font=("TkDefaultFont", 16))
    playerlbl.place(
        x=0,
        y=241
    )
    global questioncountlbl
    questioncountlbl = ttk.Label(text=f"Question /{len(names) * 10}", font=("TkDefaultFont", 16))
    questioncountlbl.place(
        x=0,
        y=0
    )
    global questiondifficultylbl
    questiondifficultylbl = ttk.Label(text="Difficulty:", font=("TkDefaultFont", 16))
    questiondifficultylbl.place(
        x=0,
        y=25
    )
    global quiznamelbl
    quiznamelbl = ttk.Label(text="Funny Quiz!", font=("TkDefaultFont", 16))
    quiznamelbl.place(
        x=948,
        y=0
    )
    global lastquestionstatuslbl
    lastquestionstatuslbl = ttk.Label(text="Last Answer:", font=("TkDefaultFont", 16))
    lastquestionstatuslbl.place(
        x=833,
        y=241
    )
    global questionlbl
    questionlbl = ttk.Label(text="", font=("TkDefaultFont", 12), wraplength=1060)
    questionlbl.place(
        x=0,
        y=144
    )
    imgBtnB.img_reference = btnimage
    
    if player_count <= 5:
        response = requests.get(f"https://opentdb.com/api.php?amount={player_count * 10}&category=18&type=multiple")
        while response.status_code != 200:
            response = requests.get(f"https://opentdb.com/api.php?amount={player_count * 10}&category=18&type=multiple")
        response = response.json()
        questions = response['results']
    else:
        response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
        while response.status_code != 200:
            response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
            
        response = response.json()
        questions = response['results']
        while len(questions) < (player_count*10):
            response = requests.get(f"https://opentdb.com/api.php?amount={50}&category=18&type=multiple")
            if response.status_code == 200:
                response = response.json()
                response = response['results']
            
                for i in response:
                    if i not in questions:
                        questions.append(i)
            print(len(questions))
        
        if len(questions) > (player_count*10): #this will most certainly happen but it is random
            diff = len(questions) - (player_count*10)
            for _ in range(diff):
                ind = random.randrange(len(questions))
                questions.pop(ind)
                print(len(questions))
            
            
            
            
        
    # names var shows player names

    global scores
    scores = []
    for player in names:
        scores.append(0)

    # for current_player, current_question, count in zip(names * 10, questions, range(len(names) * 10)):
    global current_question_num
    current_question_num = 0

    global namesorder
    namesorder = names * 10

    global current_question_text
    current_question_text = html.unescape(questions[0]['question'])
    global answers
    answers = questions[0]['incorrect_answers'].copy()
    answers.append(questions[0]['correct_answer'])

    for i in range(len(answers)):
        answers[i] = html.unescape(answers[i])

    questionlbl.config(text=current_question_text)
    global correct_answer
    correct_answer = html.unescape(questions[0]['correct_answer'])
    global difficulty
    difficulty = html.unescape(questions[0]['difficulty'])
    questioncountlbl.config(text=f"Question {1}/{len(names) * 10}")
    playerlbl.config(text=f"Player: {namesorder[0]}")
    questiondifficultylbl.config(text=f"Difficulty: {difficulty}")
    random.shuffle(answers)

    imgBtnA.config(text=answers[0], command=lambda: clicked("A"))
    imgBtnB.config(text=answers[1], command=lambda: clicked("B"))
    imgBtnC.config(text=answers[2], command=lambda: clicked("C"))
    imgBtnD.config(text=answers[3], command=lambda: clicked("D"))


def end():
    global names
    global scores
    scores, names = zip(*sorted(zip(scores, names)))
    names = list(names)
    scores = list(scores)
    names.reverse()
    scores.reverse()
    scoreboard = tkinter.Text(window)
    scoreboard["state"] = "normal"
    scoreboard.pack()

    print(names)
    print(scores)

    for count, name, score in zip(range(len(names)), names, scores):
        scoreboard.insert("end", f"{count + 1}. {name}    {score}/10\n")
    scoreboard.delete("end-1c")

    scoreboard["state"] = "disabled"
    ttk.Button(text="Finish", command=window.destroy).pack()


window.iconbitmap(resource_path("icon.ico"))
window.title("Quiz Game")
window.resizable(False, False)
window.geometry("1060x570")
window.mainloop()
