def SymbolArray(Genome, symbol):
    Symbol = "A"
    Genome = "AAAAGGGG"
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array
def PatternCount(symbol,ExtendedGenome ):
    count = 0
    for i in range(0,len(ExtendedGenome)-len(symbol)+1):
        if ExtendedGenome[i:i+len(symbol)] == symbol:
            count = count+1
    return count