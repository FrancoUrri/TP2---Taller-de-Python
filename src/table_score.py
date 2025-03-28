def show_table(score_dict):
    print("{:<10} {:<8} {:<14} {:<10} {:<10} {:<9}".format(
    "Jugador", "Kills", "Asistencias", "Muertes", "MPVs", "Puntos")
    )
    for player in score_dict:
        print("{:<10} {:<8} {:<14} {:<10} {:<10} {:<9}".format(
        player, score_dict[player]["kills"], score_dict[player]["assists"],
        score_dict[player]["deaths"], score_dict[player]["mvps"],
        score_dict[player]["score"]
        ))
def process_round(score_dict, round):
    max_score = 0
    mvps_list = []
    for player in round:
        score_dict[player]["kills"] += round[player]["kills"]
        score_dict[player]["assists"] += round[player]["assists"]
        player_round_score = 3 * round[player]["kills"] + round[player]["assists"]
        if round[player]["deaths"]:
            score_dict[player]["deaths"] += 1
            player_round_score -= 1
        score_dict[player]["score"] += player_round_score
        if max_score < player_round_score:
            max_score = player_round_score
            mvps_list = [player]
        elif max_score == player_round_score:
            mvps_list = mvps_list + [player]
    for player in mvps_list:
        score_dict[player]["mvps"] += 1
    return score_dict
def sort_dict_by_score(score_dict):
    sorted_dict = {}
    def player_score(player):
        return score_dict[player]["score"]
    player_list = [player for player in score_dict]
    player_list.sort(reverse = True, key=player_score)
    for player in player_list:
        sorted_dict[player] = score_dict[player]
    return sorted_dict
def print_game(score_dict, rounds):
    for round_index in range(len(rounds)):
        score_dict = process_round(score_dict, rounds[round_index])
        score_dict = sort_dict_by_score(score_dict)
        print(f'Ronda {round_index + 1}: ' if round_index < len(rounds) - 1 else 'Ronda final: ')
        show_table(score_dict)
        print('---------------------------------------------------------------')