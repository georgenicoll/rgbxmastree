from tree import RGBXmasTree
from colorzero import Color

def main():
    tree = RGBXmasTree(brightness=0.05)

    colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

    try:
        while True:
            for color in colors:
                for pixel in tree:
                    pixel.color = color
    except KeyboardInterrupt:
        tree.off()
        tree.close()

if __name__ == "__main__":
    main()