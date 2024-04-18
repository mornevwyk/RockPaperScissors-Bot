from tabulate import tabulate

def play_game(player1, player2, verbose=True):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"You": 0, "RPSbot": 0, "tie": 0}

    while True:
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == 'EXIT':
            break

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["You"] += 1
            winner = "You win!"
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["RPSbot"] += 1
            winner = "RPSbot wins."

        if verbose:
            print("You:", p1_play, "| RPSbot:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['RPSbot'] + results['You']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['You'] / games_won * 100

    print()
    print("Final results:")
    print_results(results)
    print()
    print(f"Your win rate:\t {win_rate}%")
    print()

    return (win_rate)


def human(prev_opponent_play):
    play = ""
    while play.upper() not in ['R', 'P', 'S', 'EXIT']:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play.upper()

def print_results(res):
    tab = []
    for key in res:
        tab.append([key, res[key]])
    print(tabulate(tab, headers=['Player', 'Wins']))

def check_outcome(p1_play, p2_play, results):
    if p1_play == p2_play:
        results["Tie"] += 1
        winner = "Tie."
    elif (p1_play == "P" and p2_play == "R") or (
            p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                    and p2_play == "P"):
        results["You"] += 1
        winner = "You win!"
    elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
        results["RPSbot"] += 1
        winner = "I win."

    return winner