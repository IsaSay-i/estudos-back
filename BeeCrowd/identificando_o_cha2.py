# BeeCrowd não lê inputs do input(), hmm. Na verdade lê sim, mas não pode conter texto.
# Precisa levar ao pé da letra a forma do input ;-;
T = int(input())
choices = list(map(int, input().split()))
counter = choices.count(T)
print(counter)