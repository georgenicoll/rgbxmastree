from tree import RGBXmasTree
from colorzero import Color
from time import sleep

def main():
    tree = RGBXmasTree(brightness=0.04)

    colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

    try:
        while True:
            for color in colors:
                tree.color = color
                sleep(0.25)
    except KeyboardInterrupt:
        tree.off()
        tree.close()

if __name__ == "__main__":
    main()
