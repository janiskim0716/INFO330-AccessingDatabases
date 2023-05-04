# imports:
import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters

# connection & cursor:
connection = sqlite3.connect('../pokemon.sqlite')
pokemonCursor = connection.cursor()

# All the "against" column suffixes:
types = ["bug", "dark", "dragon", "electric", "fairy", "fight",
   "fire", "flying", "ghost", "grass", "ground", "ice", "normal",
   "poison", "psychic", "rock", "steel", "water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
   print("You must give me six Pokemon to analyze!")
   sys.exit()


team = []
for i, arg in enumerate(sys.argv):
   if i == 0:
       continue

   final = pokemonCursor.execute("SELECT name, type1, type2, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_flying, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water FROM imported_pokemon_data WHERE pokedex_number = {}".format(i))

   # Create lists for pokemon, strong against, and weak against.
   list_pokemon = list(pokemonCursor.fetchone())
   against = list_pokemon[3:] # gets rid of name and type 1,2.
   strong_against = []
   weak_against = []

   print("Analyzing", i)
   # loop through every single i in the given length of the list.
   for i in range(len(against)):
       if float(against[i]) < 1:
           weak_against.append(types[i])
       elif float(against[i]) > 1:
           strong_against.append(types[i])
       else: continue
   print("{} ({} {}) is strong against {} but weak against {}".format(list_pokemon[0], list_pokemon[1], list_pokemon[2], strong_against, weak_against))

# Ask to save the team or not.
answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
   teamName = input("Enter the team name: ")

# Write the pokemon team to the "teams" table
   print("Saving " + teamName + " ...")
else:
   print("Bye for now!")
