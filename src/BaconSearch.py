import os
import json
from collections import defaultdict

class BaconSearch:

  # Initialize BaconSearch object with search directory and construct graph
  def __init__(self, searchDir):
    self.searchDir = searchDir
    self.currOrigin = False
    self.currTarget = False
    self.currPath = False
    self.__initGraph()

  # Initialize graph object for searching
  # @param: searchDir directory containing files to import
  # @return: constructed graph
  def __initGraph(self):
    # Declare graph (using adjacency list to store edges)
    graph = defaultdict(list)

    # Get list of files in directory
    files = os.listdir(self.searchDir)

    # Parse each file and add relevant verteces and edges to the graph
    for movieFile in files:
      # Open the file for parsing
      with open(os.path.join(self.searchDir, movieFile)) as f:
        # Parse JSON file
        try:
          fileContents = json.loads(f.read())

        # Fail if not all files are valid JSON
        except ValueError:
          print "Invalid JSON in file " + movieFile
          exit()

        # Extract film name and cast list
        film = fileContents['film']['name']
        cast = fileContents['cast']

        # For each actor in the cast, create an edge with every other actor in the cast,
        # storing the movie metadata in the process
        for actor in cast:
          name = actor['name']

          # Loop through cast members again to add a connection for each other cast   member
          for connection in cast:
            connectionName = connection['name']
            if connectionName != name:
              if 'image' in connection:
                image = connection['image']
              else:
                image = "No Image Available"
              graph[name].append((connectionName, image, film, 0))
    # Save graph as class attribute
    self.graph = graph

  def getGraph(self):
    return self.graph



  # Search the graph using BFS for degrees of separation
  # @param graph: graph object constructed by initGraph()
  # @param origin: actor from which to start searching
  # @param target: actor to whom we want to find the bacon distance
  # @return shortest path between origin and target, including movie metadata
  def search(self, origin, target):
    self.currOrigin = origin
    self.currTarget = target
    # Keep track of possible paths to explore
    paths = []

    # Keep track of names seen
    namesSeen = []

    # Start with first node
    paths.append([(self.currOrigin,)])

    while len(paths) > 0:
        # Get next path to search
        path = paths.pop(0)
        # Get last node in path to inspect
        connection = path[-1]

        # Check for cycles
        if connection[0] in namesSeen:
          continue
        else:
          namesSeen.append(connection[0])
        # If the names match, we've found the right path
        if connection[0] == target:
            self.currPath = path
            return path
        # For each connection, create a new path to explore
        for connection in self.graph[connection[0]]:
            # Copy the list
            adjPath = path[:]
            # Add the new connection to the list
            adjPath.append(connection)
            # Add the new path to the list of paths to explore
            paths.append(adjPath)

  # Pretty print the shortest path found with searchGraph
  # @return path: path
  def printPath(self):
    # If search hasn't been run yet, return error
    if not self.currOrigin:
      return "Search must be run before printing results"
    # If path isn't valid, tell user no path was found
    if not self.currPath:
      return "No result found"

    # Construct origin name and film
    string = self.currOrigin + ' in ' + self.currPath[1][2] + ' -> '
    path = self.currPath[1:]

    # String together path to form result string (grouping the next film with the current
    # actor to match the spec)
    for i, connection in enumerate(path):
      if connection[0] == self.currTarget:
        return string + self.currTarget
      else:
        nextConnection = path[i + 1]
        string += connection[0] + ' in ' + nextConnection[2] + ' -> '
    return string

  # Return JSON representation of path for web consumption
  # @return JSON path for web consumption
  def getJSONPath(self):
    # If search hasn't been run yet, return error
    if not self.currOrigin:
      return None
    # If path isn't valid, tell user no path was found
    if not self.currPath:
      return None

    return {"data": self.currPath}


