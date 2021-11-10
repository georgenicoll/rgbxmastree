from tree import RGBXmasTree
import random

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def main():
    tree = RGBXmasTree(brightness=0.05)
    try:
        while True:
            pixel = random.choice(tree)
            pixel.color = random_color()
    except KeyboardInterrupt:
        tree.off()
        tree.close()

if __name__ == "__main__":
    main()
