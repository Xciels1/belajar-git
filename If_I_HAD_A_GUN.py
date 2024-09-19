import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [ 
        ("Hope I didn't speak too soon", 0.1),
        ("My eyes have always ", 0.1),
        ("followed you around the room", 0.1),
        ("'Cause you're the only ", 0.2),
        ("God that I will ever need", 0.1),
        ("I'm holding on, I'm waiting for the moment", 0.2),
        ("For my heart to be unbroken by the seeeeeeeeeeeeeeeaaaaaaaa", 0.1),
     ]
    delays = [0.3, 5.0, 10.0, 3.0, 20.3, 25.0, 27.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()