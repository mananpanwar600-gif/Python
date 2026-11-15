'''
Slice list into 3 equal chunks and reverse each chunk
Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
Expected Outcome:

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
'''

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = len(sample_list)
chunk_size = length//3
start = 0
end = chunk_size

for i in range(3):
    print(f"Chunk {i+1} {sample_list[start:end]}")
    print(f"After reversing it {list(reversed(sample_list[start:end]))}")

    start = end
    end += chunk_size