"""Tournament"""
from typing import List, Dict, TypeVar, Tuple


class Team:
    """Team class.

    It contains team name and game results.

    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.matches_played = 0
        self.matches_won = 0
        self.matches_drawn = 0
        self.matches_lost = 0
        self.point = 0

    def won(self) -> None:
        """call if the team wins

        :return:
        """
        self.matches_played += 1
        self.matches_won += 1
        self.point += 3

    def drawn(self) -> None:
        """call if the team draws

        :return:
        """
        self.matches_played += 1
        self.matches_drawn += 1
        self.point += 1

    def lost(self) -> None:
        """call if the team loses

        :return:
        """
        self.matches_played += 1
        self.matches_lost += 1
        # self.point += 0


def tally(rows: List[str]) -> List[str]:
    """convert game results to team point overview.

    :param rows:
    :return:
    """
    teams: Dict[str, Team] = {}

    def detect_team(team_name: str) -> None:
        if teams.get(team_name) is None:
            teams[team_name] = Team(team_name)

    for row in rows:
        team1: str
        team2: str
        result: str
        team1, team2, result = row.split(';')
        detect_team(team1)
        detect_team(team2)
        if result == 'win':
            teams[team1].won()
            teams[team2].lost()
        elif result == 'loss':
            teams[team1].lost()
            teams[team2].won()
        elif result == 'draw':
            teams[team1].drawn()
            teams[team2].drawn()

    # output
    output = []
    padding = " "
    glue = ' | '
    team_column_length = 30
    field_length = 2
    # add header
    output.append(glue.join(
        [f'{"Team":{padding}<{team_column_length}}']
        + [f'{field:{padding}>{field_length}}' for field in ['MP', 'W', 'D', 'L', 'P']]
    ))

    _T = TypeVar('_T', bound=Tuple[str, Team])

    def sort_key_by_point_and_name(_team_item: _T) -> str:
        return f'{chr(1000 - _team_item[1].point)}{_team_item[1].name}'

    # noinspection PyTypeChecker
    teams = dict(sorted(teams.items(), key=sort_key_by_point_and_name))
    for team in teams.values():
        output.append(glue.join(
            [f'{team.name:{padding}<{team_column_length}}']
            + [f'{field:{padding}>{field_length}}' for field in [
                team.matches_played,
                team.matches_won,
                team.matches_drawn,
                team.matches_lost,
                team.point,
            ]]
        ))

    return output
