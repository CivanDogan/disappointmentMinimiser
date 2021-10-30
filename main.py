# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from pprint import pprint


def takeInput(filename):
    teams = []
    opt = set()
    with open(filename, "r") as f:
        lines = f.readlines()
        for l in lines:
            l = l.replace(" ", "").strip().split(",")
            teams.append(Team(l[0], l[1:]))
            opt = opt.union(set(l[1:]))

    return teams, opt


def calculateDisappointment(teams):
    return sum([team.getCurrentWeight() for team in teams])


class Team():
    job = None
    preferences = []

    def __init__(self, name):
        self.name = name
        self.job = None

    def __init__(self, name, pref):
        self.name = name
        self.preferences = pref
        self.job = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def setPreferences(self, pref):
        self.preferences = pref

    def getPreferences(self):
        return self.preferences

    def hasJob(self, ):
        if self.job == None:
            return False
        return True

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job

    def getWeight(self, pref):
        if pref in self.preferences:
            return self.preferences.index(pref)
        else:
            return 100

    def getCurrentWeight(self):
        return self.getWeight(self.job)

    def getPref(self, index):
        return self.preferences[index]


if __name__ == '__main__':
    teams, opts = takeInput("input.txt")
    team_per_options = math.ceil(len(teams) / len(opts))
    jobs = {option: [None] * team_per_options for option in opts}
    print(sorted(jobs))

    flat_list = []  # List of (team,choice,weight)
    for weight in range(len(opts) - 1):
        for team in teams:
            flat_list.append((team, team.getPref(weight)))

    print(flat_list)
    # letting each team get their best choice if empty
    for team, t_pref in flat_list:
        if (None in jobs[t_pref]) and not team.hasJob():
            index = jobs[t_pref].index(None)
            jobs[t_pref][index] = (team)
            team.setJob(t_pref)

    for team in [team for team in teams if not team.hasJob()]:
        # iterates over teams that has no job
        for pref_i in team.getPreferences():
            # get their job preferences
            for target_team_index, target_team in enumerate(jobs[pref_i]):
                # looks for other teams that has same jobs.
                if not team.hasJob():
                    for preference in target_team.getPreferences():
                        # looks other teams preferences has empty space so it can move them there.
                        if None in jobs[preference]:
                            jobs[preference][jobs[preference].index(None)] = (target_team)
                            jobs[pref_i][target_team_index] = team
                            target_team.setJob(preference)
                            team.setJob(pref_i)
                            print(jobs)


    for team in teams:
        print(f"{team.name} gets {team.getJob()} with dissapointment of {team.getCurrentWeight()}")

    print(f"Total dissapointment is {calculateDisappointment(teams)}")
