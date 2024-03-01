# Import the Hero class from the hero module
from hero import Hero

# Import the heroes list and the izuku, tsuyu,
# and fumikage dictionaries from the data module
from data import heroes, izuku, tsuyu, fumikage

# Create three Hero objects with the izuku, tsuyu,
# and fumikage dictionaries
izuku_hero = Hero(izuku)
tsuyu_hero = Hero(tsuyu)
fumikage_hero = Hero(fumikage)

print(izuku_hero.hero_name)
print(tsuyu_hero.hero_name)
print(fumikage_hero.hero_name)

# Call the display_info methods on each of the
# Hero objects.
izuku_hero.display_info()
tsuyu_hero.display_info()
fumikage_hero.display_info()

# Create a list of Hero objects using the
# get_heroes class method.
heroes_list_of_objects = Hero.get_heroes(heroes)

# Iterate through the list and call the display_info
# method on each Hero object in the list to test if
# you were successful.

for each_hero in heroes_list_of_objects:
    each_hero.display_info()
