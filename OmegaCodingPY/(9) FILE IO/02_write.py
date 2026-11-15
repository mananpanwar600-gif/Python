#Write to a file called John.txt which contain data abot John

f = open("John.txt","w")

string = '''John was a quiet man with eyes that held stories he rarely told. He lived simply, rising early to greet the sun with a strong cup of coffee and the soft rustle of morning pages. Though he kept to himself, his presence was comforting—steady, like the ticking of a reliable clock. People in the neighborhood knew him as the one who always helped without being asked: fixing a broken fence, offering an umbrella in the rain, or just listening when someone needed to talk. John didn’t speak much about his past, but his every action spoke of resilience, compassion, and a quiet kind of wisdom that left a lasting impression on everyone he met.
'''
f.write(string)
f.close()
