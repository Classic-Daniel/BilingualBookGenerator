import os
import gui
import file_parser


# temporary hardcoded generate action
def generateAction():
    textParser = file_parser.Parser()
    sentencesA = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/english/siddhartha_hesse.txt")
    sentencesB = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/german/siddhartha_hesse.txt")
    print(sentencesA[50:100])

if __name__ == '__main__':
    app = gui.MainWindow()
        
    app.setGenerateButtonAction(generateAction)
    # app.setGenerateButtonAction(lambda: print("asd"))
    app.run()