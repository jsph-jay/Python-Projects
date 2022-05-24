from random_madlibs import basketball, Arsenal, football, madlibs
import random

if __name__ == "__main__":
    m = random.choice([basketball, Arsenal, football, madlibs])
    m.madlibs()
