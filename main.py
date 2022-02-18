import gui
import file_parser
import embedding
import pairing
import book_generator
import translation

guiHandler = None

def generateAction():

    guiHandler.addOutputMessage("Starting...")
    
    try:
        textParser = file_parser.Parser()
        guiHandler.addOutputMessage("Sentence extraction for input A...")
        sentencesA = textParser.sentencesFromFile(guiHandler.getFilePathA())
        guiHandler.addOutputMessage("Sentence extraction for input B...")
        sentencesB = textParser.sentencesFromFile(guiHandler.getFilePathB())

        # translate
        # textTranslator = translation.TextTranslator(fromLang="hu", toLang="en")
        # translatedSentencesB = list(map(lambda sentence: textTranslator.getTranslation(sentence), sentencesB))

        embedder = embedding.Embedder()
        guiHandler.addOutputMessage("Embedding for input A...")
        embeddingsA = embedder.getSentenceListEmbedding(sentencesA)
        guiHandler.addOutputMessage("Embedding for input B...")
        embeddingsB = embedder.getSentenceListEmbedding(sentencesB)

        guiHandler.addOutputMessage("Sentence matching...")
        matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)

        guiHandler.addOutputMessage("Book generation...")
        generator = book_generator.BookGenerator()
        generator.createEpubBook(guiHandler.getOutputFilePath(), matchedSentences,
                                 bookMetaData=guiHandler.getOutputMetaData())
        guiHandler.addOutputMessage("Book generation finished")
    except Exception as error:
        guiHandler.addOutputMessage("Exceptions occurred: " + str(error))




if __name__ == '__main__':
    guiHandler = gui.MainWindow()
        
    guiHandler.setGenerateButtonAction(generateAction)
    guiHandler.run()