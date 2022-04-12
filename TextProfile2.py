def Pr(Text, Profile):
    outcome = 1
    for i in range(len(Text)):
        outcome *= Profile[Text[i]][i]
    return outcome

def ProfileMostProbableKmer(text, k, profile):
    maxi = -1
    x = 0
    for i in range(len(text)-k+1):
        out = Pr(text[i:i+k], profile)
        if out > maxi:
            maxi = out
            x = i
    ans = text[x:x+k]
    return ans