class GetUniquePairsCount():
    def __init__(self, list_to_check, k):
        self.list_to_check = list_to_check
        self.k = k
        self.myPairsList = list()

    def get_num_unique_pairs(self):
        self.__create_unique_pairs__()
        return len(self.myPairsList)



    def __create_unique_pairs__(self):
       # I'm going to sort it, so i have all the pairs in the same order
        self.list_to_check.sort()

        for i in self.list_to_check:
            for j in self.list_to_check:
                if not i == j:
                    if (i - j) == self.k:
                        if not ([i, j]) in self.myPairsList:
                            self.myPairsList.append([i, j])



