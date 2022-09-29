import re
from typing import Callable, List, Set

import shell
import util
import wordsegUtil


############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):

    def __init__(self, query: str, unigramCost: Callable[[str], float]):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        return self.query

    def isEnd(self, state) -> bool:
        return len(state) == 0

    def succAndCost(self, state):
        result = []
        if len(state) > 0:
            for i in range(len(state), 0, -1):
                action = state[:i]
                remainder = state[len(action):]  # оставшийся текст
                result.append((action, remainder, self.unigramCost(action)))
        return result


def segmentWords(query: str, unigramCost: Callable[[str], float]) -> str:
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=1)
    ucs.solve(SegmentationProblem(query, unigramCost))

    return ' '.join(ucs.actions)


############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

# class VowelInsertionProblem(util.SearchProblem):
#     def __init__(self, queryWords, bigramCost, possibleFills):
#         # queryWords - это входная последовательность слов, не содержащих гласных
#         self.queryWords = queryWords
#         # bigramCost - это функция, которая принимает две строки, представляющие два последовательных слова, 
#         # и предоставляет их биграмм-скор.
#         self.bigramCost = bigramCost
#         # possibleFills - это функция, которая принимает слово в виде строки и возвращает набор реконструкций
#         self.possibleFills = possibleFills

#     def startState(self):
#         return (self.queryWords[0], 0)

#     def isEnd(self, state):
#         return state[1] == len(self.queryWords) - 1

#     def succAndCost(self, state):
#         result = []
#         print(f"all state - {state}")
#         index = state[1] + 1
#         choices = self.possibleFills(self.queryWords[index]).copy()
#         # print(f"choices {choices}")
#         if len(choices) == 0:
#             choices.add(self.queryWords[index])
#         for action in choices:
#             # print(f"state - ")
#             cost = self.bigramCost(state[0], action)
#             print(f"cost - {cost} ; state - {state[0]} ; action - {action}")
#             result.append((action, (action, index), cost))
#             # print(f"result {result}")   
#         return result

# def insertVowels(queryWords, bigramCost, possibleFills):
#     if len(queryWords) == 0:
#         return ''
#     else:
#         queryWords.insert(0, wordsegUtil.SENTENCE_BEGIN)

#     ucs = util.UniformCostSearch(verbose=1)
#     ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
#     words = ' '.join(ucs.actions)
#     return words


class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        return self.queryWords[0], 1

    def isEnd(self, state):
        return state[1] == len(self.queryWords)

    def succAndCost(self, state):
        previousFill, state = state
        word = self.queryWords[state]
        possibleFills = self.possibleFills(word)
        results = []
        for fill in possibleFills:
            results.append((fill, (fill, state+1), self.bigramCost(previousFill, fill)))
            print(results[-1])
        if len(results) == 0:
            return [(word, (word, state+1), self.bigramCost(previousFill, word))]
        return results


def insertVowels(queryWords, bigramCost, possibleFills):
    if len(queryWords) == 0: 
        return ""
    queryWords = [wordsegUtil.SENTENCE_BEGIN] + queryWords
    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
    return " ".join(ucs.actions)


############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query: str, bigramCost: Callable[[str, str], float],
                 possibleFills: Callable[[str], Set[str]]):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def isEnd(self, state) -> bool:
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 14 lines of code, but don't worry if you deviate from this)
        raise Exception("Not implemented yet")
        # END_YOUR_CODE


def segmentAndInsert(query: str, bigramCost: Callable[[str, str], float],
                     possibleFills: Callable[[str], Set[str]]) -> str:
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE


############################################################

if __name__ == '__main__':
    shell.main()
