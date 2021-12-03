"""
Loads a molecule, creates a graph representation of it,
saves the graphml file to the user's home directory and
uses the kamada-kawai force-directed algorithm to render
the graph representation inline in the YaPyCon Python
console.

This code is meant to be executed from
the YaPyCon Python Console.
"""
from yasara_kernel import *
from matplotlib import pyplot as plt
import os
import networkx

%matplotlib inline

# Load a sample molecule here
LoadPDB("1GCN", download="latest")
# Add hydrogens to pH
AddHydAll()

# Define the format for the atom information to be returned
atom_format = "ATOMNUM, ATOMELEMENT, CHARGE"
# Obtain information about the atoms
molecule_atoms = ListAtom("all", format=atom_format)
# Reformat the returned information to a list of dicts with keys obtained from the format.
molecule_atoms = yapycon_reformat_atominfo_returned(molecule_atoms, format=atom_format, delim=",")
# Obtain information about the covalent bonds
molecule_bonds = ListBond("all", "all", results=4)
# Reformat the returned information to a list of dicts with keys
# the specific attributes for each bond.
molecule_bonds = yapycon_reformat_bondinfo_returned(molecule_bonds, num_of_results=4)

# Build up the graph
g = networkx.Graph()
# Add the nodes
for an_atom in molecule_atoms:
    g.add_node(an_atom["ATOMNUM"], element=an_atom["ATOMELEMENT"], charge=an_atom["CHARGE"])
# Add the edges
for a_bond in molecule_bonds:
    g.add_edge(a_bond["atomnum_sel1"], a_bond["atomnum_sel2"],
               bond_order=a_bond["bond_order"], bond_length=a_bond["bond_length"])

# At this point, we are ready to save or visualise the network.
# Save the file as graphml to the users documents directory
networkx.write_graphml(g, os.path.expanduser("~/yasara_molecule.graphml"))
# Set the atom element as the node's label
node_labels = dict(map(lambda x:(x[0], x[1]["element"]), g.nodes(data=True)))
# Use the built in networkx functionality to visualise the network
fig = plt.figure(figsize=(12,10), dpi=92);
networkx.draw_kamada_kawai(g, with_labels=True, labels=node_labels, ax=plt.gca())
