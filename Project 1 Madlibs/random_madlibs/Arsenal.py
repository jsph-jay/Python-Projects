def madlibs():
    month = input('What Month? = ')
    year = input('What Year? = ')
    team1 = input('Winning Team = ')
    team2 = input('Losing Team = ')
    championship_name = input('Name of Championship = ')
    reporter_name = input('Name of Reporter = ')
    newspaper_name = input('Name of Newspaper = ')
    manager = input('Name of Manager = ')

    madlibs = f"In {month} {year}, {team1} beat {team2} to regain the {championship_name} and equal Preston's record of not losing an away match all season. In assessing the team's achievement, {reporter_name} of {newspaper_name} wrote: {team1} manager {manager} wanted his team to push on for more honours and described the defeat of {team2} as a shift of power in English football. The team began the following season in good stead; a 4–1 win against Leeds United in September {year} meant {team1} broke the domestic record for scoring in consecutive games, and away league games without defeat. Such was their effective start to the campaign, {manager} reiterated his belief that {team1} could remain the whole season undefeated"
    print(madlibs)
