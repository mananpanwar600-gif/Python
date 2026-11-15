''' PRINT SECOND MAXNUMBER FROM AN ARRAY OF NUMBERS'''

n = int(input())
arr = map(int, input().split())

unique_scores = set(arr)
unique_scores.remove(max(unique_scores))
print(max(unique_scores))