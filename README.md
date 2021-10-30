#Team 24 Solution for JPM8

##def takeInput(filename):
Takes filename as an input and returns all teams as an object
Also calculates the number of jobs.

```python
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
```

## Usage



##def calculateDisappointment(teams):
Calcualtes total dissapointment of all teams.

```python
def calculateDisappointment(teams):
    return sum([team.getCurrentWeight() for team in teams])```
```
##Class team 
Holds basic operations on the teams 
like setting preferences , returning preferences , getDissapointment

#Main
Main keeps most of the operation.
First calculates how many teams each job will allocate.
Creates empty places for teams

Creates a single dimensional ordered list of teams prefereces

1st of team 1 , 1st of team 2 ... last of last team

Fills the empty jobs in this order.


```python
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
```
Then checks for unallocated teams. If team x is unallocated looks for it's preferences,
Finds other teams with same preferences and moves them to other jobs if there are free jobs for them.
Fills the jobs with unallocated teams.
![alt text](https://github.com/CivanDogan/disappointmentMinimiser/blob/master/img.png)

```python
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

```
At the end prints the results with total dissapointment.


Thank you
