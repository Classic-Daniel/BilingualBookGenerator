import pathlib
import pygubu
import threading
from book_generator import BookMetaData

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "main_gui.ui"


class MainWindow:
    def __init__(self, master=None):
        # 1: Create a builder and setup resources path (if you have images)
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)

        # 2: Load an ui file
        builder.add_from_file(PROJECT_UI)

        # 3: Create the mainwindow
        self.mainwindow = builder.get_object('main_gui', master)

        # 4: Connect callbacks
        builder.connect_callbacks(self)
        
        self.defineDict()
        self.setDefaults()
        self.outputMessage = self.builder.get_variable('outputMessage').get()

    def run(self):
        self.mainwindow.mainloop()
        
    def setGenerateButtonAction(self, action):
        self.generateAction = action
        
    def generate(self):
        actionThread = threading.Thread(target=self.generateAction)
        actionThread.start()

    def getFilePathA(self):
        return self.builder.get_variable('filePathA').get()
    
    def getFilePathB(self):
        return self.builder.get_variable('filePathB').get()

    def getTestRunEnabled(self):
        return self.builder.get_variable('testCheckbox').get()
    
    def getOutputFilePath(self):
        return self.builder.get_variable('outputFilepath').get()

    def getOutputMetaData(self):
        title = self.builder.get_object('outputTitle').get()
        author = self.builder.get_object('outputAuthor').get()
        return BookMetaData(title=title, author=author, language=self.getLanguageA())
    
    def getLanguageA(self):
        return self.languageDict[self.builder.get_variable('languageA').get()]
    
    def getLanguageB(self):
        return self.languageDict[self.builder.get_variable('languageB').get()]
    
    def addOutputMessage(self, message):
        currentMessage = self.builder.get_variable('outputMessage').get()
        newMessage = currentMessage + "\n" + message
        self.outputMessage = newMessage
        return self.builder.get_variable('outputMessage').set(newMessage)

    def printProgress(self, currentIndex, maxIndex):
        newMessage = self.outputMessage + f"\n({currentIndex}/{maxIndex})"
        return self.builder.get_variable('outputMessage').set(newMessage)
    
    def setDefaults(self):
        self.builder.get_variable('languageA').set("English")
        self.builder.get_variable('languageB').set("German")
        self.builder.get_variable('filePathA').set("example_books/german/siddhartha_hesse.txt")
        self.builder.get_variable('filePathB').set("example_books/english/siddhartha_hesse.txt") # example_books/hungarian/amok_zweig.rtf
        self.builder.get_variable('outputExtension').set("EPUB")
        self.builder.get_variable('outputFilepath').set("test.epub")
        
    def defineDict(self):
        self.languageDict = {
            "Arabic": "ar",
            "Chinese-simplified": "zh-CN",
            "Chinese-traditional": "zh-TW",
            "English": "en",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Japanese": "ja",
            "Korean": "ko",
            "Dutch": "nl",
            "Polish": "pl",
            "Portuguese": "pt",
            "Spanish": "es",
            "Thai": "th",
            "Turkish": "tr",
            "Russian": "ru",
            "Hungarian(Experimental)": "hu",
            "Danish(experimental)": "da",
            "Automatic(Experimental)": "auto"
        }