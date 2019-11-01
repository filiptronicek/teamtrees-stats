import pygame
import requests
import re
import time
from tqdm import tqdm



DELAY = 0.5


def get_trees():
    r = requests.get('https://teamtrees.org')
    return int(re.search('data-count="(\\d+)"', r.text).group(1))


def main():
    pygame.mixer.init()
    tree_sound = pygame.mixer.Sound('tree.wav')
    
    last_trees = get_trees()
    print(last_trees)
    loops = 0
    while True:
        time.sleep(DELAY)
        trees_now = get_trees()
        print(trees_now)
        loops += 1
        if trees_now > last_trees:
            print('TREE, people planted {} trees within the last {} seconds!'.format(trees_now - last_trees, round(loops*DELAY,2)))
            for tree in tqdm(range(round((trees_now - last_trees) / 10))):
                time.sleep(0.4)
                pygame.mixer.Sound.play(tree_sound)

            last_trees = trees_now
            loops = 0


if __name__ == '__main__':
    main()
