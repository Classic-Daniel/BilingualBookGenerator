import gui
import file_parser
import embedding
import pairing
import book_generator
import translation

guiHandler = None

def generateAction():
    
    guiHandler.setOutputMessage("Starting...")
    
    try:    
        textParser = file_parser.Parser()
        sentencesA = textParser.sentencesFromFile(guiHandler.getFilePathA())
        sentencesB = textParser.sentencesFromFile(guiHandler.getFilePathB())
            
        # translate
        # textTranslator = translation.TextTranslator(fromLang="hu", toLang="en")
        # translatedSentencesB = list(map(lambda sentence: textTranslator.getTranslation(sentence), sentencesB))

        embedder = embedding.Embedder()
        embeddingsA = embedder.getSentenceListEmbedding(sentencesA)
        embeddingsB = embedder.getSentenceListEmbedding(sentencesB)

        matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)

        generator = book_generator.BookGenerator()
        generator.createEpubBook(guiHandler.getOutputFilePath(), matchedSentences)
        
    except Exception as error:
        guiHandler.setOutputMessage("Exceptions occurred: " + str(error))

if __name__ == '__main__':
    guiHandler = gui.MainWindow()
        
    guiHandler.setGenerateButtonAction(generateAction)
    guiHandler.run()