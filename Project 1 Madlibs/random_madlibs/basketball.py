def madlibs():
    time_between_championships = input('Time between championships = ')
    stadium_name = input('Name of Stadium =')
    animal_name = input('Name of Animal =')
    city_in_uk = input('City in UK =')
    name_of_mvp = input('Name of MVP =')
    adj1 = input('Adjective = ')
    adj2 = input('Adjective = ')
    player1 = input('Name of Player = ')
    player2 = input('Name of Player = ')
    player3 = input('Name of Player = ')
    coach_name = input('Name of Coach = ')
    year_last_champions = ('When was the last championship win? = ')
    adj3 = input('Adjective = ')
    name_of_opponent = input('Losing Team = ')

    madlibs = f"The countdown to {time_between_championships} years between championships began with 35 seconds remaining in the dry spell, when the sellout crowd inside {stadium_name} began to chant “{animal_name} in Six” in perfect pitch and harmony. On the outside, where half of {city_in_uk} gathered, the screams rose up and the beer went down. And on the floor, {name_of_mvp} waved his arms and therefore gave the signal that it was time. Time for {name_of_mvp} to join an {adj1} group of historically special players. Time for the NBA Finals to creep to a close after six mostly {adj2} games. Time for {player1} and {player2}, {player3} and {coach_name} to become a bit choked up and find someone to hug. Time for the {city_in_uk} {animal_name} to announce themselves as champions for the second time in their history and first since {year_last_champions}. Seeing how it developed and progressed and especially how it ended, with an {adj3} Game 6 that was authored by a player who instantly became a legend, it was well worth the wait. The {animal_name} rallied from 0-2 in the series and never looked back — well, actually, maybe they did a few times nervously along the journey — and then put the {name_of_opponent} away Tuesday night with a closing 105-98 victory that made a city shiver."

    print(madlibs)
