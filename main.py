from tkinter import *

preto = "#1a1a1a"
azul = "#0d2838"
cinza = "#dce4e8"
laranja = "#ffa91f"
branco = "#ffffff"

janela = Tk()
janela.title("Calculadora")
janela.minsize(240, 335)
janela.maxsize(240, 335)
janela.config(bg=preto)
janela.wm_iconbitmap()

frame_tela = Frame(janela, width=240, height=75, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=240, height=260)
frame_corpo.grid(row=1, column=0)

allValues = ""

stringValue = StringVar()


def valuesEntry(event):
    global allValues
    allValues = allValues + str(event)
    stringValue.set(allValues)


def calculate():
    global allValues
    resultado = eval(allValues)
    stringValue.set(str(resultado))
    allValues = ""


def clean():
    global allValues
    allValues = ""
    stringValue.set("")


app_label = Label(
    frame_tela,
    textvariable=stringValue,
    width=16,
    height=2,
    padx=5,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=("Ivy 18"),
    fg=branco,
    bg=azul,
)
app_label.place(x=0, y=0)

button_clear = Button(
    frame_corpo,
    command=clean,
    text="C",
    width=11,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_clear.place(x=0, y=0)

button_module = Button(
    frame_corpo,
    command=lambda: valuesEntry("%"),
    text="%",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_module.place(x=120, y=0)

button_division = Button(
    frame_corpo,
    command=lambda: valuesEntry("/"),
    text="/",
    width=5,
    height=2,
    bg=laranja,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_division.place(x=180, y=0)

button_7 = Button(
    frame_corpo,
    command=lambda: valuesEntry("7"),
    text="7",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_7.place(x=0, y=52)

button_8 = Button(
    frame_corpo,
    command=lambda: valuesEntry("8"),
    text="8",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_8.place(x=60, y=52)

button_9 = Button(
    frame_corpo,
    command=lambda: valuesEntry("9"),
    text="9",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_9.place(x=120, y=52)

button_product = Button(
    frame_corpo,
    command=lambda: valuesEntry("*"),
    text="*",
    width=5,
    height=2,
    bg=laranja,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_product.place(x=180, y=52)

button_4 = Button(
    frame_corpo,
    command=lambda: valuesEntry("4"),
    text="4",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_4.place(x=0, y=104)

button_5 = Button(
    frame_corpo,
    command=lambda: valuesEntry("5"),
    text="5",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_5.place(x=60, y=104)

button_6 = Button(
    frame_corpo,
    command=lambda: valuesEntry("6"),
    text="6",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_6.place(x=120, y=104)

button_sub = Button(
    frame_corpo,
    command=lambda: valuesEntry("-"),
    text="-",
    width=5,
    height=2,
    bg=laranja,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_sub.place(x=180, y=104)

button_1 = Button(
    frame_corpo,
    command=lambda: valuesEntry("1"),
    text="1",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_1.place(x=0, y=156)

button_2 = Button(
    frame_corpo,
    command=lambda: valuesEntry("2"),
    text="2",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_2.place(x=60, y=156)

button_3 = Button(
    frame_corpo,
    command=lambda: valuesEntry("3"),
    text="3",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_3.place(x=120, y=156)

button_plus = Button(
    frame_corpo,
    command=lambda: valuesEntry("+"),
    text="+",
    width=5,
    height=2,
    bg=laranja,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_plus.place(x=180, y=156)

button_0 = Button(
    frame_corpo,
    command=lambda: valuesEntry("0"),
    text="0",
    width=11,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_0.place(x=0, y=208)

button_dot = Button(
    frame_corpo,
    command=lambda: valuesEntry("."),
    text=".",
    width=5,
    height=2,
    bg=cinza,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_dot.place(x=120, y=208)

button_equal = Button(
    frame_corpo,
    command=calculate,
    text="=",
    width=5,
    height=2,
    bg=laranja,
    font=("Ivy 13 bold"),
    relief=RAISED,
    overrelief=RIDGE,
)
button_equal.place(x=180, y=208)

janela.mainloop()
