import gui
import file_parser
import embedding
import pairing
import book_generator
import translation
import globals

def generateAction():

    globals.guiHandler.addOutputMessage("Starting...")
    
    try:
        pass
    except Exception as error:
        globals.guiHandler.addOutputMessage("Exceptions occurred: " + str(error))

    textParser = file_parser.Parser()
    globals.guiHandler.addOutputMessage("Sentence extraction for input A...")
    sentencesA = textParser.sentencesFromFile(globals.guiHandler.getFilePathA())
    globals.guiHandler.addOutputMessage("Sentence extraction for input B...")
    sentencesB = textParser.sentencesFromFile(globals.guiHandler.getFilePathB())

    # translate
    # textTranslator = translation.TextTranslator(fromLang="hu", toLang="en")
    # translatedSentencesB = list(map(lambda sentence: textTranslator.getTranslation(sentence), sentencesB))

    embedder = embedding.Embedder()
    globals.guiHandler.addOutputMessage("Embedding for input A...")
    embeddingsA = embedder.getSentenceListEmbedding(sentencesA)
    globals.guiHandler.addOutputMessage("Embedding for input B...")
    embeddingsB = embedder.getSentenceListEmbedding(sentencesB)

    globals.guiHandler.addOutputMessage("Sentence matching...")
    matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)

    globals.guiHandler.addOutputMessage("Book generation...")
    generator = book_generator.BookGenerator()
    generator.createEpubBook(globals.guiHandler.getOutputFilePath(), matchedSentences,
                             bookMetaData=globals.guiHandler.getOutputMetaData())
    globals.guiHandler.addOutputMessage("Book generation finished")

if __name__ == '__main__':
    globals.guiHandler = gui.MainWindow()
        
    globals.guiHandler.setGenerateButtonAction(generateAction)
    globals.guiHandler.run()