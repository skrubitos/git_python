
import os
import time


malw_pjesma= [
"""Oh no, he's got malware in his computer now,
He's never been very good with technology, oh how
He wishes that he knew what to do
But he's in way over his head, it's true

He clicks on every link that comes his way
He doesn't know which ones are safe or which ones to stray
He's always trying to keep up with the times
But he's always a step behind

Oh no, he's got malware in his computer now
He's never been very good with technology, oh how
He wishes that he knew what to do
But he's in way over his head, it's true

He's tried to get help from all his friends
But they just tell him to do it again
He's feeling so frustrated and all alone
But he knows he has to find a way to get it done

Oh no, he's got malware in his computer now
He's never been very good with technology, oh how
He wishes that he knew what to do
But he's in way over his head, it's true"""
]
metni_pismu= malw_pjesma[0]
user_name= os.listdir("C:\\Users")
print(user_name)

for x in  (user_name):
    try:
        print("\novo je korisnik:         "+x)
        os.chdir("C:\\Users\\"+ x +"\\Desktop")
        print("directory path:      "+os.getcwd())
        try:
            os.mkdir("open me")
            os.chdir("C:\\Users\\"+ x +"\\Desktop\\open me")

            time.sleep(2)
            os.mkdir("getting song in 5 seconds")
            time.sleep(1)
            os.mkdir("getting song in 4 seconds")
            time.sleep(1)
            os.mkdir("getting song in 3 seconds")
            time.sleep(1)
            os.mkdir("getting song in 2 seconds")
            time.sleep(1)
            os.mkdir("getting song in 1 seconds")

            otvaramo_datoteku= open("malware song.txt", "w")
            otvaramo_datoteku.write(str(malw_pjesma[0]))
            time.sleep(1)
            for pozadina in range (400):
                os.chdir("C:\\Users\\"+ x +"\\Desktop")
                os.mkdir("get pwned"+ str(pozadina))


            time.sleep(1)
        except PermissionError and FileExistsError and FileNotFoundError:
            pass

    except NotADirectoryError and FileNotFoundError and FileExistsError and PermissionError:
        pass
