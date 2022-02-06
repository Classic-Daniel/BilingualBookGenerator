from cgitb import text
from embedding import Embedder
import numpy as np

LOOK_AHEAD = 10
MATCH_THRESHOLD = 0.7

def getMatchedSentences(embedder : Embedder, embeddingsA: list[list[float]], embeddingsB: list[list[float]], sentencesA, sentencesB, sentencesPerSection=3):
    pairingsAtoB = _matchEmbeddings(embedder, embeddingsA, embeddingsB)
    matchedSentences = _getTextPairings(sentencesA, sentencesB, pairingsAtoB, sentencesPerSection)

    pairingRatio = np.count_nonzero(pairingsAtoB != -1) / len(pairingsAtoB)
    print(f"pairingRatio: {pairingRatio}")

    return matchedSentences

def _matchEmbeddings(embedder : Embedder, embeddingsA: list[list[float]], embeddingsB: list[list[float]]) -> list[int]:
    pairingAtoB = np.full((len(embeddingsA)), -1, dtype=int)
    lastMatchedIndexB = -1
    indexA = -1

    for embeddingA in embeddingsA:
        indexA = indexA + 1

        for i in range(LOOK_AHEAD):
            indexB = min(lastMatchedIndexB + i, len(embeddingsB) - 1)
            distance = embedder.getEmbedDistance(embeddingA, embeddingsB[indexB])
            
            if(distance < MATCH_THRESHOLD):
                pairingAtoB[indexA] = indexB
                lastMatchedIndexB = indexB
                break

    return pairingAtoB

"""
Returns tuple of matched text sections
"""
def _getTextPairings(sentencesA, sentencesB, pairingsAtoB, sentencesPerSection):
        # generate text pairings
        textPairings = []
        lastUsedIndexA = -1
        lastUsedIndexB = -1
        
        for indexA in range(len(pairingsAtoB)):
            if (indexA - lastUsedIndexA) > sentencesPerSection and pairingsAtoB[indexA] != -1:

                aSentencesInCell = " ".join(sentencesA[lastUsedIndexA + 1 : indexA + 1])
                bSentencesInCell = " ".join(sentencesB[lastUsedIndexB + 1 : pairingsAtoB[indexA] + 1])
                textPairings = textPairings + [(aSentencesInCell, bSentencesInCell)]
                
                lastUsedIndexA = indexA
                lastUsedIndexB = pairingsAtoB[indexA]

        return textPairings

        