from tree import RGBXmasTree
from colorzero import Color, Hue

def main():
    tree = RGBXmasTree(brightness=0.1)

    tree.color = Color('red')

    try:
        while True:
            tree.color += Hue(deg=10)
    except KeyboardInterrupt:
        tree.off()
        tree.close()

if __name__ == "__main__":
    main()
