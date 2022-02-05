import os
import gui
import file_parser
import embedding
import pairing
import book_generator
import translation

import numpy as np

# temporary hardcoded generate action
def generateAction():
    
    textParser = file_parser.Parser()
    # sentencesA = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/german/siddhartha_hesse.txt")
    # sentencesB = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/english/siddhartha_hesse.txt")
    sentencesA = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/german/amok_zweig.txt")
    sentencesB = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/hungarian/amok_zweig.rtf")
        
    # translate
    textTranslator = translation.TextTranslator(fromLang="hu", toLang="en")
    translatedSentencesB = list(map(lambda sentence: textTranslator.getTranslation(sentence), sentencesB[:100]))
        
    embedder = embedding.Embedder()
    embeddingsA = embedder.getSentenceListEmbedding(sentencesA[:100])
    embeddingsB = embedder.getSentenceListEmbedding(translatedSentencesB[:100])
    
    matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)
    print(matchedSentences)
        
    generator = book_generator.BookGenerator()
    generator.createEpubBook("test.epub", matchedSentences)

if __name__ == '__main__':
    app = gui.MainWindow()
        
    app.setGenerateButtonAction(generateAction)
    # app.setGenerateButtonAction(lambda: print("asd"))
    app.run()