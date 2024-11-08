import random

def player(prev_play, opponent_history=[]):
    # We then append the previous move of the opponent to their history
    opponent_history.append(prev_play)

    # We will default to a random move if the history is not enough for a sequence
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Tracking the opponent's last 3 moves
    last_three = ''.join(opponent_history[-3:])
    
    # Possible moves combinations of 3 moves
    possible_moves = ["RRR", "RRP", "RRS", "RPR", "RPP", "RPS", "RSR", "RSP", "RSS",
                      "PRR", "PRP", "PRS", "PPR", "PPP", "PPS", "PSR", "PSP", "PSS",
                      "SRR", "SRP", "SRS", "SPR", "SPP", "SPS", "SSR", "SSP", "SSS"]

    # Initialize sequence counts if they don't exist
    sequence_counts = {move: 0 for move in possible_moves}

    # Count occurrences of each sequence (only when we have enough history)
    for i in range(len(opponent_history) - 3):
        sequence = ''.join(opponent_history[i:i + 3])
        if sequence in sequence_counts:
            sequence_counts[sequence] += 1

    # Find the most common sequence
    most_common_sequence = max(sequence_counts, key=sequence_counts.get)

    # Respond with the ideal counter for the most common move
    ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
    next_move_prediction = most_common_sequence[-1]  # Take the last move of the most common sequence
    return ideal_response[next_move_prediction]
