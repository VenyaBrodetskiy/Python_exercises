with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    games = [file.readline().strip().split(';') for i in range(n)]
def check_team(team, list):
    if team not in list:
        list[team] = [1, 0, 0, 0, 0]
    else:
        list[team][0] += 1
def check_winner(team1, score1, team2, score2, list):
    if int(score1) > int(score2):
        list[team1][1] += 1
        list[team1][4] += 3
        list[team2][3] += 1
    elif int(score1) < int(score2):
        list[team2][1] += 1
        list[team2][4] += 3
        list[team1][3] += 1
    else:
        list[team1][2] += 1
        list[team1][4] += 1
        list[team2][2] += 1
        list[team2][4] += 1
result = dict()
for i in range(n):
    check_team(games[i][0], result)
    check_team(games[i][2], result)
    check_winner(*games[i], result) #оператор * здесь загружает всю строку в аргументы функции
for i in result:
    print(i + ':', end='')
    print(*result[i]) #оч классный оператор * разворачивает список (убирает квадратные скобки)