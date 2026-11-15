#We will work on another file named poem.txt

f = open("poem.txt","w+")

content = ''' Whispers of the Wind

The wind it speaks in gentle tones,
Through silent trees and ancient stones.
It carries dreams from far and wide,
Like secrets on a moonlit tide.

It brushes cheeks and tousles hair,
A fleeting touch, a breath of air.
It tells of places never seen,
And paints the skies in silver sheen.

So close your eyes, and you might hear,
The winds soft voice, so bright and clear.
It sings of hope, of journeys new—
A quiet song meant just for you.

'''

f.write(content)
f.seek(0)
read = f.read()
print(read)
f.close()
