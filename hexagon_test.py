graph_connections = {}

for letter in list(map(chr, range(ord("A"), ord("L") + 1))):
    graph_connections[letter] = {}
for letter in list(map(chr, range(ord("A"), ord("L") + 1))):
    graph_connections[letter]["prev"] = {}
    graph_connections[letter]["next"] = {}

graph_connections["A"]["prev"]["direct"] = ["F", "G"]
graph_connections["A"]["next"]["direct"] = ["B", "H"]
graph_connections["A"]["prev"]["inverse"] = ["B", "H"]
graph_connections["A"]["next"]["inverse"] = ["F", "G"]

graph_connections["B"]["prev"]["direct"] = ["A", "H"]
graph_connections["B"]["next"]["direct"] = ["C", "I"]
graph_connections["B"]["prev"]["inverse"] = ["C", "I"]
graph_connections["B"]["next"]["inverse"] = ["A", "H"]

graph_connections["C"]["prev"]["direct"] = ["B", "I"]
graph_connections["C"]["next"]["direct"] = ["J", "D"]
graph_connections["C"]["prev"]["inverse"] = ["J", "D"]
graph_connections["C"]["next"]["inverse"] = ["B", "I"]

graph_connections["D"]["prev"]["direct"] = ["C", "J"]
graph_connections["D"]["next"]["direct"] = ["E", "K"]
graph_connections["D"]["prev"]["inverse"] = ["E", "K"]
graph_connections["D"]["next"]["inverse"] = ["C", "J"]

graph_connections["E"]["prev"]["direct"] = ["D", "K"]
graph_connections["E"]["next"]["direct"] = ["F", "L"]
graph_connections["E"]["prev"]["inverse"] = ["F", "L"]
graph_connections["E"]["next"]["inverse"] = ["D", "K"]

graph_connections["F"]["prev"]["direct"] = ["E", "L"]
graph_connections["F"]["next"]["direct"] = ["A", "G"]
graph_connections["F"]["prev"]["inverse"] = ["A", "G"]
graph_connections["F"]["next"]["inverse"] = ["E", "L"]

graph_connections["G"]["prev"]["direct"] = ["A", "F"]
graph_connections["G"]["next"]["direct"] = ["H", "I", "J", "K", "L"]
graph_connections["G"]["prev"]["inverse"] = ["H", "I", "J", "K", "L"]
graph_connections["G"]["next"]["inverse"] = ["A", "F"]

graph_connections["H"]["prev"]["direct"] = ["A", "B"]
graph_connections["H"]["next"]["direct"] = ["G", "I", "J", "K", "L"]
graph_connections["H"]["prev"]["inverse"] = ["G", "I", "J", "K", "L"]
graph_connections["H"]["next"]["inverse"] = ["A", "B"]

graph_connections["I"]["prev"]["direct"] = ["B", "C"]
graph_connections["I"]["next"]["direct"] = ["G", "H", "J", "K", "L"]
graph_connections["I"]["prev"]["inverse"] = ["G", "H", "J", "K", "L"]
graph_connections["I"]["next"]["inverse"] = ["B", "C"]

graph_connections["J"]["prev"]["direct"] = ["C", "D"]
graph_connections["J"]["next"]["direct"] = ["G", "H", "I", "K", "L"]
graph_connections["J"]["prev"]["inverse"] = ["G", "H", "I", "K", "L"]
graph_connections["J"]["next"]["inverse"] = ["C", "D"]

graph_connections["K"]["prev"]["direct"] = ["E", "D"]
graph_connections["K"]["next"]["direct"] = ["G", "H", "I", "J", "L"]
graph_connections["K"]["prev"]["inverse"] = ["G", "H", "I", "J", "L"]
graph_connections["K"]["next"]["inverse"] = ["E", "D"]

graph_connections["L"]["prev"]["direct"] = ["E", "F"]
graph_connections["L"]["next"]["direct"] = ["G", "H", "I", "J", "K"]
graph_connections["L"]["prev"]["inverse"] = ["G", "H", "I", "J", "K"]
graph_connections["L"]["next"]["inverse"] = ["E", "F"]

# algorithm for checking a single string
#'prev','current','direction','next' are variables of string type
# we start with a variable 'valid' set to 1, and if any of the conditions result in a break, set 'valid' to 0, only then break
# 1 Check if the first letter in a string is either A or F or G,
#   otherwise break
# that is, check if we enter the part at gate in vertex of edges AFG
# 2 Check if the last letter is A or F or G, otherwise break
# that is, we exit the part at gate in vertex of edges AFG


# As we have checked the first and the last letters, now we can simply initialize 'previous' with the first letter
# 3 For the second letter, write it to 'current'
# and then check if 'current' is in graph_connections[current][prev][direct]
# or graph_connections[current][prev][inverse] , then store 'direction' as 'inverse' or 'direct' correspondingly
# otherwise break
# 4 For the third letter and onwards (up to the end): write this letter to 'next'
# then we check if 'current' is in graph_connections[current][prev][direct]
# or in graph_connections[current][prev][inverse] , then store 'direction' as 'inverse' or 'direct' correspondingly
# then check if 'next' is in graph_connections[current][next][direction] , on fail break
# 5 If all passes, we write 'current' into 'prev', write 'next' into 'current', then repeat step (4) or end of cycle
# 6 on end of cycle, return the value of 'valid' : it will be 0 if no breaks happened or 1 if the route was incorrect

# reading input data
with open("test.txt", "r") as input_file:
    n = int(input_file.readline())
    routes = input_file.read().splitlines()
result = ""

for route in routes:
    valid = "1"
    # check if entrance and exit are in principle, correct
    if (route[0] in ["A", "F", "G"]) and (route[-1] in ["A", "F", "G"]):
        # clear the values of previous, current, next from the last route
        previous: str = ""
        current: str = ""
        next: str = ""
        direction = ""

        for letter in route:
            # check if the letter is the first letter
            if previous == "":
                previous = letter
            # determine the direction of route in a graph if the second letter is legitimate
            elif (current == "") and (direction == ""):
                current = letter
                if previous in graph_connections[current]["prev"]["direct"]:
                    direction = "direct"
                elif previous in graph_connections[current]["prev"]["inverse"]:
                    direction = "inverse"
                else:
                    valid = "0"
                    break
            # determine if the third and further letters are legitimate
            # that is, check if it matches the dictionary and is not equal to "previous"

            else:
                # we try to check if this new letter is valid, so we write it to "next"
                next = letter
                # same code for previous to be valid
                if previous in graph_connections[current]["prev"]["direct"]:
                    direction = "direct"
                elif previous in graph_connections[current]["prev"]["inverse"]:
                    direction = "inverse"
                else:
                    valid = "0"
                    break
                # new code for next to be valid
                if (next in graph_connections[current]["next"][direction]) and (
                    next != previous
                ):
                    previous = current
                    current = next
                    next = ""
                else:
                    valid = "0"
                    break

    else:
        valid = "0"
    result = result + valid

with open("output.txt", "w+") as output_file:
    output_file.writelines(result)

