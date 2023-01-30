#!/usr/bin/env python3
from brain_games.launch import launch_game
from brain_games.games import gcd


def main():
    launch_game(gcd)


if __name__ == '__main__':
    main()