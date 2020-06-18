class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        choiceOne = {}
        for i, rest in enumerate(list1):
            choiceOne[rest] = i
        minSum = len(list1) + len(list2) - 2
        #print(minSum)
        choice = []
        for i, rest in enumerate(list2):
            if rest in choiceOne:
                #print("rest in choiceOne  %s " % rest)
                if minSum > i + choiceOne[rest]:
                    choice = [rest]
                    minSum = i + choiceOne[rest]
                    #print("new choice  %s " % choice)
                elif minSum == i + choiceOne[rest]:
                    choice.append(rest)
                    #print("append to choice  %s " % choice)
        return choice
        
