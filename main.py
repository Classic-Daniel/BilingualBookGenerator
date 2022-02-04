import os
import gui
import file_parser
import embedding
import pairing

# temporary hardcoded generate action
def generateAction():
    textParser = file_parser.Parser()
    sentencesA = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/english/siddhartha_hesse.txt")
    sentencesB = textParser.sentencesFromFile(os.path.dirname(__file__) + "/example_books/german/siddhartha_hesse.txt")
    
    embedder = embedding.Embedder()
    embeddingsA = embedder.getSentenceListEmbedding(sentencesA[:100])
    embeddingsB = embedder.getSentenceListEmbedding(sentencesB[:100])
    
    pairingAtoB = pairing.matchEmbeddings(embedder, embeddingsA, embeddingsB)
    pairintRatio = np.count_nonzero(pairingAtoB != -1) / len(pairingAtoB)
    print("pairintRatio: " + pairintRatio)
    
    # Print sentence pairings
    for i in range(20, 30): # len(pairingAtoB)
        if(pairingAtoB[i] != -1):
            print(sentencesA[i])
            print(sentencesB[pairingAtoB[i]])
            print()

if __name__ == '__main__':
    app = gui.MainWindow()
        
    app.setGenerateButtonAction(generateAction)
    # app.setGenerateButtonAction(lambda: print("asd"))
    app.run()