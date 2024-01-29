from main import play_game


if __name__ == "__main__":
    g = play_game(interactive=True)
    print("Game ended:")
    print("  did player win?", g.player_won)
    print("  mana spent:", g.player.mana_spent)
