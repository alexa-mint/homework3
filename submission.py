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

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        # queryWords - это входная последовательность слов, не содержащих гласных
        self.queryWords = queryWords
        # bigramCost - это функция, которая принимает две строки, представляющие два последовательных слова, 
        # и предоставляет их оценку по биграмме.
        self.bigramCost = bigramCost
        # possibleFills - это функция, которая принимает слово в виде строки и возвращает набор реконструкций
        self.possibleFills = possibleFills

    def startState(self):
        print(f" startstate - {self.queryWords[0], 0}")
        return (self.queryWords[0], 0)

    def isEnd(self, state):
        print(f" isEnd - {state} - {state[1] == len(self.queryWords) - 1}")
        return state[1] == len(self.queryWords) - 1

    def succAndCost(self, state):
        result = []
        index = state[1] + 1
        choices = self.possibleFills(self.queryWords[index]).copy()
        if len(choices) == 0:
            choices.add(self.queryWords[index])
        for action in choices:
            cost = self.bigramCost(state[0], action)
            result.append((action, (action, index), cost))
        # print(result)    
        return result

def insertVowels(queryWords, bigramCost, possibleFills):
    if len(queryWords) == 0:
        return ''
    else:
        queryWords.insert(0, wordsegUtil.SENTENCE_BEGIN)

    ucs = util.UniformCostSearch(verbose=1)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
    words = ' '.join(ucs.actions)
    return words


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
