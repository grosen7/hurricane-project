from classes.FloridaHurricaneFind import FloridaHurricaneFind
from datetime import datetime

if __name__ == "__main__":
    print("Running FloridaHurricaneFind program")
    start = datetime.now()
    FloridaHurricaneFind().floridaHurricaneFind("data/hurdat2.txt")
    print("Script completed in {} seconds".format(datetime.now()-start))
