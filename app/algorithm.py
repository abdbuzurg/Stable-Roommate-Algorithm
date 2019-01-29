from collections import OrderedDict
from operator import itemgetter
import copy

########################################
def getKeyByVal(inptDict, inputVal):
    for key, val in inptDict.items():
        if val == inputVal:
            return key
def removeCycle(preferences, table):
    tmpPreferences = preferences
    # remove the cycle matches symmetrically
    for i in range(len(table[0]) - 1):
        tmpPreferences[table[1][i]].remove(table[0][i + 1])
        tmpPreferences[table[0][i + 1]].remove(table[1][i])
    return tmpPreferences
def cycleExists(table):
    tableLeft = table[0]
    tableRight = table[1]
    # check if all elements in column are unique
    if len(tableLeft) > len(set(tableLeft)):
        return True
    else:
        return False
def stableNotPossible(preferences):
    for i in preferences:
        if len(preferences[i]) == 0:
            return True
    return False
def isStable(preferences):
    for i in preferences:
        if len(preferences[i]) != 1:
            return False
    return True
def step1(inputList):
    proposals = {}
    numProposals = {}
    queue = []
    for i in inputList["preferences"]:
        queue.append(i)
        proposals[i] = None
        numProposals[i] = 0
    tmpPreferences = copy.deepcopy(inputList["preferences"])
    while not len(queue) == 0:
        i = queue[0]
        numProposals[i] += 1
        for j in inputList["preferences"][i]:
            if proposals[j] == None:
                del queue[0]
                proposals[j] = i
                break
            elif proposals[j] != i:
                current_index = inputList["preferences"][j].index(i)
                other_index = inputList["preferences"][j].index(proposals[j])

                if current_index < other_index:
                    del queue[0]
                    queue.insert(0, proposals[j])
                    # Remove old proposal symmetrically
                    tmpPreferences[proposals[j]].remove(j)
                    tmpPreferences[j].remove(proposals[j])
                    proposals[j] = i
                    break
                else:
                    # Remove invalid proposal symmetrically
                    tmpPreferences[i].remove(j)
                    tmpPreferences[j].remove(i)
        inputList["preferences"] = copy.deepcopy(tmpPreferences)
    return (proposals, inputList)
def step2(proposals, inputList):
    tmpPreferences = copy.deepcopy(inputList["preferences"])
    for i in inputList["preferences"]:
        #  Remove the right hand side of the preferred element
        proposalIndex = tmpPreferences[i].index(proposals[i])
        tmpPreferences[i] = tmpPreferences[i][:proposalIndex + 1]
        # Remove all other instances of the given element
        for j in inputList["preferences"]:
            # Try to remove element from all preference lists
            key = getKeyByVal(proposals, i)
            if j != i and j != proposals[i] and j != key:
                try:
                    tmpPreferences[j].remove(i)
                except ValueError:
                    pass
    # for i in inputList["preferences"]:
    #    pass
    return tmpPreferences
def step3(preferences):
    first = True
    # search for cycles until a stable or unstable matches are found
    while True:
        # create a table with two columns
        table = ([], [])
        # check if stable matching is possible
        if stableNotPossible(preferences):
            raise AlgorithmError("Stable matching not possible.")
        for i in preferences:
            # add the first instance that has atleast 2 preferences
            if len(preferences[i]) >= 2 and first == True:
                # add element
                firstPreference = i
                table[0].append(firstPreference)
                # add second preference of element
                secondPreference = preferences[i][1]
                table[1].append(secondPreference)
                first = False
            elif first == False:
                # check if a cycle exists in the table
                if cycleExists(table):
                    # remove cycle
                    preferences = removeCycle(preferences, table)
                    first = True
                    # start again
                    break
                # add the last preference of the previous second preference
                # from the table
                firstPreference = preferences[secondPreference][-1]
                table[0].append(firstPreference)
                # add the second preference of the first preference
                secondPreference = preferences[firstPreference][1]
                table[1].append(secondPreference)
        # If the preferences are stable, return them
        if isStable(preferences):
            return preferences
def apply(input1):
    step_1 = step1(input1)
    return step3(step2(step_1[0], step_1[1]))
########################################
def executeAlgorithm(quierySet):
    country = {}
    data = {}
    # code below takes the data from EXCEL file
    # data will have all the numeric values that is sent by the users
    # campus will have campus names as keys and the list of names of the students as a value to key
    # same with gender and country.
    for person in quierySet:
        data[person.full_name] = [
                person.scale1,
                person.scale2,
                person.scale3,
                person.scale4,
                person.scale5,
                person.scale6,
                person.scale7,
                person.scale8
            ]
        if country.get(person.country, None) is None:
            country[person.country] = [person.full_name]
        else:
            country[person.country].append(person.full_name)

    # gender dictionary is in the form of gender = {'male': [person1, person2], 'female': [person3, person4]}
    # code below will give to each person their numerical values 🔥🔥🔥🔥🔥
    # code below will add another person named 'Unknown' if the number of people in each campus and in each gender has and odd number of
    # people, if a person will be matched by the unknown the person will not have a roommate :((((
    if len(data) % 2 == 1:
        data['NoRoommate'] = []
        for _ in range(len(data[list(data.keys())[0]])):
            data['NoRoommate'].append(5.0)

    # code below does several stuff:
    # 1) it finds the preference value for each person to every other person within  gender
    # 2) it sorts the preferences of each person according to the preference value (ascending order)
    # 3) the preference values are removed and each person will have its preference list of individuals
    # 4) each individual preference is being sorted by country (two people from one Country cannot be roommates) unless there are no other chances
    #print(gender)
    subResult = dict()
    for person, person_values in data.items():
        subResult[person] = dict()
        for another_person, another_person_values in data.items():
            if person != another_person:
                difference = 0
                for i in range(len(person_values)):
                    difference += abs(person_values[i] - another_person_values[i])

                subResult[person][another_person] = difference

        # sorts the dictionary according to the score of each ANOTHER_PERSON to PERSON
        subResult[person] = dict(OrderedDict(sorted(subResult[person].items(), key=itemgetter(1))))

        # code below removes the numbers from the dictionary entirely
        all_names = []
        for key in subResult[person].keys():
            all_names.append(key)

        subResult[person] = all_names

    for key, items in subResult.items():
        everyone = items[:]
        for country_name, people in country.items():
            for item in items:
                if item in people and key in people:
                    everyone.append(item)
                    del everyone[everyone.index(item)]

        subResult[key] = everyone


    #applying the algorithm and 
    data = subResult
    preferences = {"preferences": data}
    result = apply(preferences)
    final_result = {}
    for key, item in result.items():
        if key != final_result.get(item[0]):
                final_result[key] = item[0]
    
    return final_result