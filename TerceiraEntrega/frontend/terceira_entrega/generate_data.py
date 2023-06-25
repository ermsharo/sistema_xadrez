import csv
from random import randint, shuffle
from datetime import datetime, timedelta


def simulate_championship(player_names,arbrito,chave_campeonato):
    num_players = len(player_names)
    num_games = 5

    # Shuffle the player names to randomize the pairings
    shuffle(player_names)

    fieldnames = ['jogador_primario', 'jogador_secundario', 'arbitro', 'pecas_pretas', 'pecas_brancas', 'data_inicio',
                  'data_fim', 'vencedor', 'id', 'chave_campeonato', 'chave_salao', 'numero_jogadas']

    with open('championship.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for game_id in range(num_games):
            jogador_primario = player_names[game_id % num_players]
            jogador_secundario = player_names[(game_id + 1) % num_players]
            arbitro =arbrito
      
            data_inicio = datetime.now() - timedelta(days=game_id)
            data_fim = data_inicio + timedelta(hours=randint(1, 5))
            vencedor = jogador_primario if randint(0, 1) == 0 else jogador_secundario
            chave_salao = f'Venue 1'

            writer.writerow({
                'jogador_primario': jogador_primario,
                'jogador_secundario': jogador_secundario,
                'arbitro': arbitro,
                'pecas_pretas': jogador_primario,
                'pecas_brancas': jogador_secundario,
                'data_inicio': data_inicio,
                'data_fim': data_fim,
                'vencedor': vencedor,
                'id': game_id + 1,
                'chave_campeonato': chave_campeonato,
                'chave_salao': chave_salao,
                'numero_jogadas': randint(6, 35)
            })

    print(f'Championship with {num_games} games simulated and saved to championship.csv.')


# Example usage:
player_list = ['Player A', 'Player B', 'Player C', 'Player D', 'Player E']
arbrito = 'arbrito here'
chave_campeonato = 'chave aqui'
simulate_championship(player_list,arbrito, chave_campeonato)
