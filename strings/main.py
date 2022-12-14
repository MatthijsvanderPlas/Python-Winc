# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line
scorer1 = "Ruud Gullit"
scorer2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer1 + " " + str(goal_0) + ", " + scorer2 + " " + str(goal_1)

report = f"{scorer1} scored in the {goal_0}nd minute\n{scorer2} scored in the {goal_1}th minute"

player = "Christiaan Verlaan"

first_name = player[: player.find(" ")]
last_name_len = len(player[player.find(" ") + 1 :])
name_short = player[0] + "." + player[player.find(" ") :]

chant = (len(first_name) - 1) * (first_name + "! ") + first_name + "!"

good_chant = chant[-1] != " "
