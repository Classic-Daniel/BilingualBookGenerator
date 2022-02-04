import os
import gui
import file_parser
import embedding
import pairing
import book_generator

import numpy as np

# temporary hardcoded generate action
def generateAction():
    textParser = file_parser.Parser()
    sentencesA = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/german/siddhartha_hesse.txt")
    sentencesB = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/english/siddhartha_hesse.txt")
    
    embedder = embedding.Embedder()
    embeddingsA = embedder.getSentenceListEmbedding(sentencesA)
    embeddingsB = embedder.getSentenceListEmbedding(sentencesB)
    
    matchedSentences = pairing.getMatchedSentences(embedder, embeddingsA, embeddingsB, sentencesA, sentencesB)
        
    generator = book_generator.BookGenerator()
    generator.createEpubBook("test.epub", matchedSentences)

if __name__ == '__main__':
    app = gui.MainWindow()
        
    app.setGenerateButtonAction(generateAction)
    # app.setGenerateButtonAction(lambda: print("asd"))
    app.run()