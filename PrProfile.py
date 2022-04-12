def Pr(Text, Profile):
    running_pr = 1
    for index, nucleotide in enumerate(Text):
        running_pr *= Profile[nucleotide][index]
    return running_pr
