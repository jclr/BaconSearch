# Testing BaconSearch

# Import required libraries
import sys
from src.BaconSearch import BaconSearch

# Check to make sure arguments are valid
if len(sys.argv) != 2:
  print "Usage: python testBacon.py <unzipped directory with json film files>"

# Assign cmd line arg to sanely named variable
searchDir = sys.argv[1]

# For the purposes of this assignment, Kevin Bacon will always be the target
target = "Kevin Bacon"

# Initialize BaconSearch
baconSearch = BaconSearch(searchDir)

# Test search not completed
assert baconSearch.printPath() == "Search must be run before printing results"

# Test name not in graph
origin = "George Washington"
baconSearch.search(origin, target)
assert baconSearch.printPath() == "No result found"

# Test actor in film with Kevin Bacon
origin = "Frank Langella"
baconSearch.search(origin, target)
assert baconSearch.printPath() == "Frank Langella in Frost/Nixon -> Kevin Bacon"

# Test actor with multiple connections to Kevin Bacon, make sure shortest one is found
# Shortest path: Robin Williams in Hamlet -> Julie Christie in New York, I Love You -> Kevin Bacon
# Longer path: Robin Williams in Mrs. Doubtfire -> Sally Field in Forrest Gump -> Tom Hanks in Lost Moon: The Triumph of Apollo 13 -> Kevin Bacon
origin = "Robin Williams"
baconSearch.search(origin, target)
assert baconSearch.printPath() == "Robin Williams in Hamlet -> Julie Christie in New York, I Love You -> Kevin Bacon"

# Test actor with large bacon number
origin = "Marilyn Monroe"
baconSearch.search(origin, target)
assert baconSearch.printPath() == "Marilyn Monroe in Marilyn in Manhattan -> Ben Gazzara in Road House -> Sunshine Parker in Tremors -> Kevin Bacon"

# Test actor causing cycle infinite loop
origin = "James Stewart"
baconSearch.search(origin, target)
assert baconSearch.printPath() == "James Stewart in Hollywood Out-takes and Rare Footage -> Lauren Bacall in Ready to Wear -> Julia Roberts in Flatliners -> Kevin Bacon"




graphTest = BaconSearch('data/test')

origin = "Mark Hamill"
graph = graphTest.getGraph()
assert len(graph) == 3






print "All tests passed!"
