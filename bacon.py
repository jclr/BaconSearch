################################### Main Script ###################################

# Usage: python bacon.py <unzipped directory with json film files> <origin actor>

# Import required libraries
import sys
from src.BaconSearch import BaconSearch

# Check to make sure arguments are valid
if len(sys.argv) != 3:
  print "Usage: python bacon.py <unzipped directory with json film files> <origin actor>"

# Assign cmd line args to sanely named variables
searchDir = sys.argv[1]
originName = sys.argv[2]

# For the purposes of this assignment, Kevin Bacon will always be the target
targetName = "Kevin Bacon"

# Initialize BaconSearch object with directory containing actor info
baconSearch = BaconSearch(searchDir)

# Search graph for shortest path
baconSearch.search(originName, targetName)

# Print result
print baconSearch.printPath()

