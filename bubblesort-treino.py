teams_nfl = ["49ers", "Eagles", "Chiefs", "Bills", "Ravens", "Dolphins", "Cowboys", "Lions"]

for i in range(len(teams_nfl)):
    for j in range(len(teams_nfl) - i - 1):
        if teams_nfl[j] > teams_nfl[j + 1]:
            teams_nfl[j], teams_nfl[j + 1] = teams_nfl[j + 1], teams_nfl[j]

print(teams_nfl)
