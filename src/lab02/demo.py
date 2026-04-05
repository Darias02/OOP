from model import CharacterCollection
from model import Character
def main():
    k1, k2 = create()
    collection = CharacterCollection()
    collection.add(k1)
    collection.add(k2)
    print(collection)

def create():
    k1 = Character("Lol", 66, 3, 50, 99)
    k2 = Character("Bob", 100, 1, 20, 10)
    return k1, k2

main()