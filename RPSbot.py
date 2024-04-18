import random

def RPSbot(prev_play, opponent_history=[], play_order={}):
    chain_length = 5
    if not prev_play:
        prev_play = 'R'
        play_order.clear()
    
    opponent_history.append(prev_play)
    prediction = 'P'

    if len(opponent_history) < chain_length +1:
        pass
    else:
        last_5 = opponent_history[-chain_length:]
        
        order = ''.join(last_5[:-1])
        
        play = last_5[-1]

        if order in play_order.keys():
            if play in play_order[order].keys():
                play_order[order][play] += 1
            else:
                play_order[order][play] = 1
        else:
            play_order[order] = {}
            play_order[order][play] = 1

    pattern = ''.join(opponent_history[-(chain_length - 1):])
    if pattern in play_order.keys():
        options = play_order[pattern]
        prediction = max(options, key=options.get)

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]

def RPSbot_chat(prev_play, opponent_history=[], play_order={}):
    chain_length = 5
    if not prev_play:
        prev_play = random.choice(['R','P','S'])
        play_order.clear()
    
    opponent_history.append(prev_play)
    prediction = 'P'

    if len(opponent_history) < chain_length +1:
        prediction = random.choice(['R','P','S'])
    else:
        last_5 = opponent_history[-chain_length:]
        
        order = ''.join(last_5[:-1])
        
        play = last_5[-1]

        if order in play_order.keys():
            if play in play_order[order].keys():
                play_order[order][play] += 1
            else:
                play_order[order][play] = 1
        else:
            play_order[order] = {}
            play_order[order][play] = 1

    pattern = ''.join(opponent_history[-(chain_length - 1):])
    if pattern in play_order.keys():
        options = play_order[pattern]
        prediction = max(options, key=options.get)

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]