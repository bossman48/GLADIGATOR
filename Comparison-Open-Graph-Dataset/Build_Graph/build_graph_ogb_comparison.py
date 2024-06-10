# -*- coding: utf-8 -*-
"""Build_Graph_OGB_Comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1purgKKdHNWLO1fVuCLqh5kfnvkxcOGVc
"""
"""!!!
#install pytorch packages
"""
#!pip install ogb
#!pip install nltk
#!pip install tensorflow
#!pip install h5py
#!pip install -q transformers
#!pip install torch
#!pip install torchvision
#!pip install scikit-metrics

#!pip install -q torch-scatter -f https://data.pyg.org/whl/torch-${TORCH}.html
#!pip install -q torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}.html
#!pip install -q git+https://github.com/pyg-team/pytorch_geometric.git

"""!!!
#install scipy and networkx packages
"""

#!pip install 'scipy>=1.8'
#!pip install 'networkx<2.7'

"""# read disease decsription"""


from ogb.linkproppred import LinkPropPredDataset

dataset = LinkPropPredDataset(name = "ogbl-biokg")


diseaseProtein = dataset[0].get("edge_index_dict")[list(dataset[0].get("edge_index_dict").keys())[0]]
print(diseaseProtein.shape)
print(diseaseProtein)

"""
you can save dataset

import urllib.request
urllib.request.urlretrieve("http://snap.stanford.edu/ogb/data/linkproppred/biokg.zip", "/content/drive/MyDrive/masterProject/projectComparison/data/biokg.zip")


"""
"""#drive access"""

#from google.colab import drive
#drive.mount('/content/drive')

"""# disease id to entities"""

# read disease id from csv, from gozsari
import csv
diseaseEntities = []
with open("../../source-files/disease_entidx2name.csv", "r") as file:
    csvreader = csv.reader(file)
    headerDiseaseEntity = next(csvreader)
    for row in csvreader:
        diseaseEntities.append(row)

print(headerDiseaseEntity)
print(diseaseEntities[0])

def findDiseaseEntName(index):
  for element in diseaseEntities:
    if(int(index) == int(element[0])):
      return element[1]


findDiseaseEntName(0)

# read protein id from csv, from gozsari
import csv
proteinEntities = []
with open("../../source-files/protein_entidx2name.csv", "r") as file:
    csvreader = csv.reader(file)
    headerProteinEntity = next(csvreader)
    for row in csvreader:
        proteinEntities.append(row)

print(headerProteinEntity)
print(proteinEntities[0])
print(proteinEntities[1])

def findGeneEntName(index):
  for element in proteinEntities:
    if(int(index) == int(element[0])):
      return element[1]


print(findGeneEntName(0))
print(findGeneEntName(1))
print(findGeneEntName(1653))

"""#disease discription and gene sequence is gathered"""

# disease description
import csv
diseaseDescriptions = []
with open("../../source-files/diseaseDescription.csv", "r") as file:
    csvreader = csv.reader(file)
    headerDiseaseDescription = next(csvreader)
    for row in csvreader:
        diseaseDescriptions.append(row)

print(headerProteinEntity)
print(diseaseDescriptions[0])
print(diseaseDescriptions[1])

def findDiseaseDescription(index):
  for element in diseaseDescriptions:
    if(int(index) == int(element[0])):
      return element[2]

def findDiseaseEntryName(index):
  for element in diseaseDescriptions:
    if(int(index) == int(element[0])):
      return element[1]


print(findDiseaseDescription(0))
print(findDiseaseEntryName(0))

# gene sequence
import csv
geneSequences = []
geneNameAndEntryDict={}
with open("../../source-files/idmapping_2023_12_13.tsv", "r") as file:
    csvreader = csv.reader(file, delimiter="\t")
    headerGeneSequence = next(csvreader)
    for row in csvreader:
        geneSequences.append(row)
        geneNameAndEntryDict[row[5]] = row[1]

print(headerGeneSequence)
print(geneSequences[0])

def findGeneSequence(index):
  for element in geneSequences:
    if(int(index) == int(element[0])):
      if(element[2]=='reviewed'):
        return element[9]

print(findGeneSequence(1))
print(findGeneSequence(10))

def findGeneEntry(index):
  for element in geneSequences:
    if(int(index) == int(element[0])):
      if(element[2]=='reviewed'):
        return element[1]

print(findGeneEntry(1))
print(findGeneEntry(10))

def findGeneID(entryName):
  for element in geneSequences:
    if(entryName == element[1]):
      if(element[2]=='reviewed'):
        return int(element[0])

print(findGeneID("P04217"))
print(findGeneID("P11245"))


def gatherGeneSequenceFromOpenGraphProteinID(index):
  tempIndex=findGeneEntName(int(index))
  if(tempIndex!=None):
    return findGeneSequence(int(tempIndex))

print(gatherGeneSequenceFromOpenGraphProteinID(0))
print(gatherGeneSequenceFromOpenGraphProteinID(1))

def gatherEntryFromGeneName(geneName):
  return geneNameAndEntryDict.get(geneName)

print(gatherEntryFromGeneName("A1BG"))

"""# Build protein sequence embedding

"""

import numpy as np
import h5py


proteinSequenceEmbeddingDict = {}
with h5py.File("../../source-files/per-protein.h5", "r") as file:
    print(f"number of entries: {len(file.items())}")
    print(file)
    print(dir(file))
    print(type(file))


    for sequence_id, embedding in file.items():

      proteinSequenceEmbeddingDict[sequence_id] = embedding[0:embedding.size]
      if sequence_id == "P04217":
        print(proteinSequenceEmbeddingDict.get(sequence_id))

def proteinSequenceEmbedding(uniprotID):
  try:
    tempEmbedding = proteinSequenceEmbeddingDict.get(uniprotID)
    if((tempEmbedding != None).any()):
      return np.insert(tempEmbedding,0,np.zeros(768))
    else:
      return np.zeros(1792)
  except Exception as exc:
    print("An exception occurred: ",exc)
    return np.zeros(1792)

print(proteinSequenceEmbedding("P04217"))
def proteinSequenceEmbedding2(uniprotID):
  try:
    with h5py.File("../../source-files/per-protein.h5", "r") as file:

      for sequence_id, embedding in file.items():
        if sequence_id == uniprotID:
          return np.insert(embedding[0:embedding.size],0,np.zeros(768))

    return np.zeros(1792)
  except:
    print("An exception occurred")
    return np.zeros(1792)

def getProteinEmbeddingFromOpenGraphId(index):
  tempEntryName = findGeneEntry(int(index))
  if(tempEntryName!=None):
    return proteinSequenceEmbedding(tempEntryName)

print(getProteinEmbeddingFromOpenGraphId(1))


def getProteinEmbeddingFromOpenGraphEntryName(entryName):
  return proteinSequenceEmbedding(entryName)

print(getProteinEmbeddingFromOpenGraphEntryName("P04217"))

"""# build biobert_v1.1"""

#!pip install -q transformers

import tensorflow as tf
import re
import numpy as np
from transformers import AutoTokenizer, AutoModel

try:
  model = AutoModel.from_pretrained("../../source-files/")
  tokenizer = AutoTokenizer.from_pretrained("../../source-files/")
except Exception as exc:
  print("Biobert model did not found in the source-files path. Therefore, Biobert pretrained model will be downloaded from internet.")
  tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")

  model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")

  print("Biobert pretrained model download process completed. Saving process will be run.")
  _ = model.save_pretrained("../../source-files/")
  _ = tokenizer.save_pretrained("../../source-files/")

"""#diseaseDescriptionEmbedding"""

def diseaseDescriptionEmbedding(description):
  try:
    inputs = tokenizer(description, return_tensors="pt",truncation=True, max_length=512)
    outputs = model(**inputs)
    vector = outputs["pooler_output"].detach().cpu().numpy()[0]
    return np.pad(vector, (0, 1024), 'constant')
  except:
    print("exception in diseaseDescriptionEmbedding ")
    return np.zeros(1792)



def getDiseaseEmbedding(index):
  tempEmbedding = findDiseaseDescription(int(index))
  if(tempEmbedding!=None):
    return diseaseDescriptionEmbedding(tempEmbedding)

print(getDiseaseEmbedding(0))
print(len(getDiseaseEmbedding(0)))
print(getDiseaseEmbedding(1))


def getDiseaseEmbeddingByEntryName(entryName):
  return diseaseDescriptionEmbedding(entryName)

print(getDiseaseEmbeddingByEntryName("C0038586"))
print(len(getDiseaseEmbeddingByEntryName("C0038586")))

"""
#Build a graph via using networkx
"""

import matplotlib.pyplot as plt
import networkx as nx

mainGraph = nx.Graph()
index = 0
try:
  while(index<len(diseaseProtein[0])):
    tempDiseaseID = findDiseaseEntryName(diseaseProtein[0][index])
    tempGeneIdFromOpenGraph = findGeneEntName(diseaseProtein[1][index])
    tempGeneID = findGeneEntry(tempGeneIdFromOpenGraph)
    print("Index: ",index ," Disease : ", tempDiseaseID, " Gene : ",tempGeneID)
    if(tempGeneID != None and tempDiseaseID != None):
      if(mainGraph.has_node(tempGeneID) == False):
        #mainGraph.add_nodes_from([(element[1], {'x': cv.transform([geneDiseaseDict.get(element[1])]).toarray()[0]})])
        tempEmbeddingProt = getProteinEmbeddingFromOpenGraphEntryName(tempGeneID)
        if((tempEmbeddingProt != None).any()):
          mainGraph.add_nodes_from([(tempGeneID, {'x': tempEmbeddingProt,'id':tempGeneID,"gene_smybol":tempGeneID})])
        #print(element[2], " " ,tempEmbeddingProt)
      if(mainGraph.has_node(tempDiseaseID) == False):
        #mainGraph.add_nodes_from([(element[8], {'x': cv.transform([geneDiseaseDict.get(element[8])]).toarray()[0]})])
        #print(geneDiseaseDict.get(element[8]))

        tempEmbeddingDisease = getDiseaseEmbeddingByEntryName(tempDiseaseID)
        if((tempEmbeddingDisease != None).any()):
          mainGraph.add_nodes_from([(tempDiseaseID, {'x': tempEmbeddingDisease,'id':tempDiseaseID,"gene_smybol":""})])
        #print(geneDiseaseDict.get(element[8]), " " ,tempEmbeddingDisease)

      if(mainGraph.has_edge(tempGeneID,tempDiseaseID) == False):
        mainGraph.add_edge(tempGeneID,tempDiseaseID,edge_nodes_attributes=str(tempGeneID+","+tempDiseaseID))
        print("New edge is added, index : " , index)


    index+=1

except Exception as e:
  print("Exception : ", e )

"""
attrs = {str(element[1]): {"geneid": element[0], "protein_class": element[6],"protein_class_name":element[7]},str(element[8]):{ "diseaseid": element[9],"disease_class":element[10],"disease_type":element[12]}}
nx.set_node_attributes(mainGraph,attrs)
"""

print(mainGraph.number_of_nodes())
print(mainGraph.number_of_edges())

"""!!!
#read csv that contains disease disease associations
"""

# !
import csv
rowsDiseaseDisease = []
with open("../../source-files/AllDiseaseDiseaseLinkedData.csv", "r") as file:
    csvreader = csv.reader(file)
    headerDiseaseDisease = next(csvreader)
    for row in csvreader:
        rowsDiseaseDisease.append(row)

"""# Add association between diseases that 2 diseases are already in graph"""

for element in rowsDiseaseDisease:
  if(element[16]!=None and element[17] != None and  mainGraph.has_node(element[16]) == True and mainGraph.has_node(element[17]) == True ):
    mainGraph.add_edge(element[16],element[17],edge_nodes_attributes=str(element[16]+","+element[17]))

print(mainGraph.number_of_nodes())
print(mainGraph.number_of_edges())

"""
# Read tab file that is contains gene-gene association."""

# !
import csv
rowsGeneGene = []
with open("../../source-files/BIOGRID-ORGANISM-Homo_sapiens-4.4.217.tab.txt", "r") as file:
    csvreader = csv.reader(file, delimiter='\t')
    headerGeneGene = next(csvreader)
    for row in csvreader:
        rowsGeneGene.append(row)

"""!!!
# Add association that 2 genes are already i graph
"""

index=0
for element in rowsGeneGene:
  firstNodeUniprotID=gatherEntryFromGeneName(element[2])
  secondNodeUniprotID=gatherEntryFromGeneName(element[3])
  if(firstNodeUniprotID!=None and secondNodeUniprotID != None  and mainGraph.has_node(firstNodeUniprotID) == True and mainGraph.has_node(secondNodeUniprotID) == True ):
    mainGraph.add_edge(firstNodeUniprotID,secondNodeUniprotID,edge_nodes_attributes=str(firstNodeUniprotID+","+secondNodeUniprotID))

  print(index)
  index+=1

"""# networkx to pytorch data"""

from torch_geometric.utils.convert import from_networkx

graphData = from_networkx(mainGraph)

"""
# Save dataset to drive"""

import torch

torch.save(graphData,"../../graph-files/Graph_Comparison_OGB.pt")

print("Graph is built successfully")