players = ['Halland', 'Foden', 'Walker', 'Dias', 'Collins', 'KDB', 'Akanji', 'Doku', 'Rodri']

odd_players = [odd for odd in players if len(odd) % 2 == 1]

print(odd_players)