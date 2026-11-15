'''
Create a simple countdown timer using a while loop.
Write a code to create a simple countdown timer of 5 seconds using a while loop.

Once the timer finishes (when the remaining time reaches zero), print a “Time’s up!” message.

Expected Output:

Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!
'''
import time

n = int(input("Set timer in seconds : "))
while(n+1!=0):
    print(f"Time remaining : {n} seconds")
    time.sleep(1)
    n = n-1

print("Time's Up!")