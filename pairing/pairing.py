from embedding import Embedder
import numpy as np

LOOK_AHEAD = 10
MATCH_THRESHOLD = 0.7

def matchEmbeddings(embedder : Embedder, embeddingsA: list[list[float]], embeddingsB: list[list[float]]) -> list[int]:
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

        