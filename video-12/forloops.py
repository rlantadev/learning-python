fenerbahce_players = ["Volkan Demirel", "Gustavo Henrique", "Alex Souza", "Talischa", "Jose Mourinho"]
techical_manager = "Jose Mourinho"

# for player in fenerbahce_players:
#     print(player)

    # print(player) fonksiyonu ile fenerbahce_players listesindeki her bir elemanı ekrana yazdırıyoruz. Bunu yaparken
    # döngü her indexi inceleyerek sıralayacak ve print fonksiyonu ile ekrana yazdıracak.

# player_number = 0
# for player in fenerbahce_players:
#     player_number = player_number + 1
#     print(player_number, player)

    # burada ise döngü her bir elemanı incelediğinde player_number değişkenine 1 ekleyerek her bir elemanın indexini
    # oluşturacak. Bu sayede her bir elemanın sırasını ve elemanı ekrana yazdırabileceğiz.

# player_number = 0
# for player in fenerbahce_players:
#     player_number = player_number + 1
#     print(player_number, player)


# print(fenerbahce_players[0])
# print(fenerbahce_players[0].split())

# ad, soyad = fenerbahce_players[0].split()[0], fenerbahce_players[0].split()[1]

# print(ad)
# print(soyad)

# player_number = 0
# for player in fenerbahce_players:
#     player_number = player_number + 1
#     firstname, lastname = player.split()[0], player.split()[1]
#     print("{0}. Player Name: {1} Player Lastname: {2}".format(player_number, firstname, lastname))

player_number = 0
techical_manager_number = 0

for player in fenerbahce_players:
    firstname, lastname = player.split()[0], player.split()[1]

    if player == techical_manager:
        techical_manager_number += 1 
        print("{0}. Tech. Manager Name: {1} Tech. Manager Lastname: {2}".format(techical_manager_number, firstname, lastname))
    else:
        player_number += 1
        print("{0}. Player Name: {1} Player Lastname: {2}".format(player_number, firstname, lastname))





