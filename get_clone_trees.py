#takes in an array and gets all the possible clone trees edge list
#input is [0, 1, 2, 3]
#output is [0, 2], [0, 1], [1, 3]
#[0, 1], [0, 2], [0, 3] etc.
from get_prufer_edges import get_prufer_edges
def get_clone_trees(vertices):
  output = []
  for i in vertices:
    for j in vertices:
      prufer_sequence = [i, j]
      edges = get_prufer_edges(prufer_sequence)
      output.append(edges)
  return output