from tkinter import *
from translate import Translator

# initializing window
Screen = Tk()
Screen.title("Language Translator")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

# Tuple for choosing languages
LanguageChoices = {'Hindi', 'English', 'French', 'German', 'Spanish', 'Tamil', 'Japanese'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    try:
        OutputVar.set("Translating...")
        Screen.update()
        translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=TranslateLanguageChoice.get())
        Translation = translator.translate(TextVar.get())
        OutputVar.set(Translation)
    except Exception as e:
        OutputVar.set("Error: " + str(e))

# Configure grid layout to center elements
Screen.grid_rowconfigure(0, weight=1)
Screen.grid_rowconfigure(6, weight=1)
Screen.grid_columnconfigure(0, weight=1)
Screen.grid_columnconfigure(4, weight=1)

# Choice for input language
Label(Screen, text="Choose a Language ").grid(row=1, column=1, padx=10, pady=10, sticky=E)
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
InputLanguageChoiceMenu.grid(row=1, column=2, padx=10, pady=10, sticky=W)

# Choice in which the language is to be translated
Label(Screen, text="Translated Language").grid(row=2, column=1, padx=10, pady=10, sticky=E)
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
NewLanguageChoiceMenu.grid(row=2, column=2, padx=10, pady=10, sticky=W)

# Text input
Label(Screen, text="Enter Text                  ").grid(row=3, column=1, padx=10, pady=10, sticky=E)
TextVar = StringVar()
TextBoxInput = Entry(Screen, textvariable=TextVar)
TextBoxInput.grid(row=3, column=2, padx=10, pady=10, sticky=W)

# Output text
Label(Screen, text="Output Text               ").grid(row=4, column=1, padx=10, pady=10, sticky=E)
OutputVar = StringVar()
TextBoxOutput = Entry(Screen, textvariable=OutputVar)
TextBoxOutput.grid(row=4, column=2, padx=10, pady=10, sticky=W)

# Button for calling function
B = Button(Screen, text="Translate", command=Translate, relief=GROOVE)
B.grid(row=5, column=1, columnspan=2, pady=20)

mainloop()
