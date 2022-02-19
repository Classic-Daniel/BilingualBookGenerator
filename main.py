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

    if globals.guiHandler.getTestRunEnabled():
        sentencesA = sentencesA[:globals.TEST_RUN_LENGTH]
        sentencesB = sentencesB[:globals.TEST_RUN_LENGTH]

    # translate to english if language not supported by the sentence embedder
    translatedSentencesA = sentencesA
    translatedSentencesB = sentencesB

    langAliasA = globals.guiHandler.getLanguageA()
    if langAliasA not in globals.EMBEDDING_LANGUAGES:
        translatedSentencesA = translateSentences(sentencesA, langAliasA)

    langAliasB = globals.guiHandler.getLanguageB()
    if langAliasB not in globals.EMBEDDING_LANGUAGES:
        translatedSentencesB = translateSentences(sentencesB, langAliasB)

    embedder = embedding.Embedder()
    globals.guiHandler.addOutputMessage("Embedding for input A...")
    embeddingsA = embedder.getSentenceListEmbedding(translatedSentencesA)
    globals.guiHandler.addOutputMessage("Embedding for input B...")
    embeddingsB = embedder.getSentenceListEmbedding(translatedSentencesB)

    globals.guiHandler.addOutputMessage("Sentence matching...")
    matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)

    globals.guiHandler.addOutputMessage("Book generation...")
    generator = book_generator.BookGenerator()
    generator.createEpubBook(globals.guiHandler.getOutputFilePath(), matchedSentences,
                             bookMetaData=globals.guiHandler.getOutputMetaData())
    globals.guiHandler.addOutputMessage("Book generation finished")

def translateSentences(sentences, language):
    counter = [0]  # trick to be able to pass int by reference
    numOfSentences = len(sentences)
    globals.guiHandler.addOutputMessage("Text translation...")
    textTranslator = translation.TextTranslator(fromLang=language, toLang="en")
    # translatedSentences = list(map(lambda sentence: textTranslator.getTranslation(sentence), sentences))
    translatedSentences = [translateSentence(sentence, textTranslator, counter, numOfSentences)
                           for sentence in sentences]
    print(translatedSentences)
    return translatedSentences

def translateSentence(sentence, translator, counter, numOfSentences):
    translatedSentence = translator.getTranslation(sentence)
    counter[0] = counter[0] + 1
    globals.guiHandler.printProgress(counter[0], numOfSentences)
    return translatedSentence


if __name__ == '__main__':
    globals.guiHandler = gui.MainWindow()
        
    globals.guiHandler.setGenerateButtonAction(generateAction)
    globals.guiHandler.run()
