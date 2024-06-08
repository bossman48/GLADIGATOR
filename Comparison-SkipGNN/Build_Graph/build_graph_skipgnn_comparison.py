# -*- coding: utf-8 -*-
"""Build_Graph_SkipGNN_Comparison.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SfzhsYBqsnpToID2zB-TDFFd2v1FGZxs

# Install pytorch packages
"""
"""!!!
#install pytorch packages
"""
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

import csv
rowsDiseaseDescription = []
with open("../../source-files/diseaseFeaturesWithDescription.csv", "r") as file:
    csvreader = csv.reader(file)
    headerDiseaseDescription = next(csvreader)
    for row in csvreader:
        rowsDiseaseDescription.append(row)

"""!!!
#read gene features but we dont use that data
"""

import csv
rowsGeneFeatures = []
with open("../../source-files/GeneFeatures.csv", "r") as file:
    csvreader = csv.reader(file)
    headerGeneFeatures = next(csvreader)
    for row in csvreader:
        rowsGeneFeatures.append(row)

geneProteinSequenceDict = {}
counterForMeanLenght = 0
totalLenght = 0
for element in rowsGeneFeatures:
  if(len(element)>8 and element[2] != None and element[8] != None ):
    if(geneProteinSequenceDict.get(element[2]) == None):
      geneProteinSequenceDict[element[2]] = element[8]
      totalLenght+=len(element[8])
      counterForMeanLenght+=1

"""!!!
#read data from csv.

that data gathered from disgenet
"""

# !
import csv
rowsGeneDisease = []
with open("../../source-files/AllGeneDiseaseLinkedData40.csv", "r") as file:
    csvreader = csv.reader(file)
    headerGeneDisease = next(csvreader)
    for row in csvreader:
        rowsGeneDisease.append(row)

# !
import csv
rowsGeneDiseaseComparison = []
with open("../../source-files/curated_gene_disease_associations.tsv", "r") as file:
    csvreader = csv.reader(file, delimiter="\t")
    headerGeneDiseaseComparison = next(csvreader)
    for row in csvreader:
        rowsGeneDiseaseComparison.append(row)

# !
import csv
rowsGeneUniprotID = {}
with open("../../source-files/mapa_geneid_4_uniprot_crossref.tsv", "r") as file:
    csvreader = csv.reader(file, delimiter="\t")
    headerGeneUniprot = next(csvreader)
    for row in csvreader:
        rowsGeneUniprotID[int(row[1])] = row[0]

"""# Build vectorizer"""

# !
geneFeaturesList = []
geneFeaturesDict = {}
geneIndex = 0
diseaseFeaturesList = []
diseaseFeaturesDict = {}
diseaseIndex = 0
index =1
for element in rowsGeneDiseaseComparison:
  if(rowsGeneUniprotID.get(int(element[0]))!=None):
    if(geneFeaturesDict.get(rowsGeneUniprotID.get(int(element[0]))) == None and geneProteinSequenceDict.get(rowsGeneUniprotID.get(int(element[0]))) != None ):
      geneFeaturesList.append(geneProteinSequenceDict[rowsGeneUniprotID.get(int(element[0]))])
      geneFeaturesDict[rowsGeneUniprotID.get(int(element[0]))]=geneIndex
      geneIndex+=1
  else:
    print("Not found gene, index: " , element[0])
  if(len(element)>4 and element[4] != None):
    for diseaseElement in rowsDiseaseDescription:
      if(len(diseaseElement)>7 and diseaseElement[0] == element[4]):
        if(diseaseFeaturesDict.get(element[4]) == None):
          #diseaseFeaturesList.append(diseaseElement[1]+" "+diseaseElement[7])
          diseaseFeaturesDict[element[4]]=diseaseElement[1]+" "+diseaseElement[7]
          #diseaseIndex+=1
  else:
    print("Not found gene, index : ", element[4])

  #print(index)
  index+=1

"""# Build protein sequence embedding

"""

import numpy as np
import h5py

with h5py.File("../../source-files/per-protein.h5", "r") as file:
    print(f"number of entries: {len(file.items())}")
    print(file)
    print(dir(file))
    print(type(file))

    for sequence_id, embedding in file.items():
      if sequence_id == "P04217":

        print("seq:", sequence_id, " protein embedding", embedding[0:embedding.size])

def proteinSequenceEmbedding(uniprotID):
  try:
    with h5py.File("../../source-files/per-protein.h5", "r") as file:

      for sequence_id, embedding in file.items():
        if sequence_id == uniprotID:
          return np.insert(embedding[0:embedding.size],0,np.zeros(768))

    return np.zeros(1792)
  except:
    print("An exception occurred")
    return np.zeros(1792)

"""# build biobert_v1.1"""

#!pip install -q transformers

import tensorflow as tf
import re
import numpy as np
from transformers import AutoTokenizer, AutoModel

try:
  model = AutoModel.from_pretrained("../source-files/")
  tokenizer = AutoTokenizer.from_pretrained("../source-files/")
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

"""# Build  dict that contains gene symbol and disease id"""

# !
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

geneDiseaseDict = {}

try:

  for element in rowsGeneDiseaseComparison:
    if(rowsGeneUniprotID.get(int(element[0]))!=None):
      if(geneDiseaseDict.get(rowsGeneUniprotID.get(int(element[0]))) == None and geneProteinSequenceDict.get(rowsGeneUniprotID.get(int(element[0]))) != None ):
        #geneDiseaseDict[element[1]]=kMerAlgorithmForSequenceSlidingWindow(seq=geneProteinSequenceDict[element[1]],kMer=3)
        geneDiseaseDict[rowsGeneUniprotID.get(int(element[0]))]=geneProteinSequenceDict[rowsGeneUniprotID.get(int(element[0]))]

    if(element[4] != None):
      if(geneDiseaseDict.get(element[4]) == None):
        for diseaseElement in rowsDiseaseDescription:
          if(len(diseaseElement)> 7 and diseaseElement[0] == element[4]):
            py_nltk = re.sub(r'[^\w\s]',' ',(diseaseElement[1]+" "+diseaseElement[7]).lower())
            text_tokens = word_tokenize(py_nltk)
            py_nltk1 = stopwords.words ('english')
            vector = [t for t in text_tokens if t not in py_nltk1]
            #vector.split()
            if(len(vector)>512):
              tempVect = " ".join(vector[:511])
              print(len(tempVect.split()),tempVect, "\n")
              print(len(" ".join(vector).split())," ".join(vector), "\n")
            else:
              tempVect = " ".join(vector)

            geneDiseaseDict[element[4]]=tempVect
except:
  print("problem is here 1")


print(headerDiseaseDescription)
print(rowsDiseaseDescription[0])

"""# build a graph via using networkx


"""

import matplotlib.pyplot as plt
import networkx as nx

# cv.transform([geneDiseaseDict.get("A1BG")]).toarray()
dictGeneSymbolUniprotID={}
#clear ram
bagOfWords = []

mainGraph = nx.Graph()
index = 0
try:
  for element in rowsGeneDiseaseComparison:
    if(len(element) > 4 and rowsGeneUniprotID.get(int(element[0]))!=None and element[4] != None and geneDiseaseDict.get(rowsGeneUniprotID.get(int(element[0]))) != None and geneDiseaseDict.get(rowsGeneUniprotID.get(int(element[0]))) != None):
      if(mainGraph.has_node(rowsGeneUniprotID.get(int(element[0]))) == False):
        #mainGraph.add_nodes_from([(element[1], {'x': cv.transform([geneDiseaseDict.get(element[1])]).toarray()[0]})])
        dictGeneSymbolUniprotID[element[1]]=rowsGeneUniprotID.get(int(element[0]))
        tempEmbeddingProt = proteinSequenceEmbedding(rowsGeneUniprotID.get(int(element[0])))
        mainGraph.add_nodes_from([(rowsGeneUniprotID.get(int(element[0])), {'x': tempEmbeddingProt,'id':rowsGeneUniprotID.get(int(element[0])),"gene_smybol":element[1]})])
        #print(element[2], " " ,tempEmbeddingProt)
      if(mainGraph.has_node(element[4]) == False):
        #mainGraph.add_nodes_from([(element[8], {'x': cv.transform([geneDiseaseDict.get(element[8])]).toarray()[0]})])
        #print(geneDiseaseDict.get(element[8]))

        tempEmbeddingDisease = diseaseDescriptionEmbedding(geneDiseaseDict.get(element[4]))
        mainGraph.add_nodes_from([(element[4], {'x': tempEmbeddingDisease,'id':element[4],"gene_smybol":""})])
        #print(geneDiseaseDict.get(element[8]), " " ,tempEmbeddingDisease)

      if(mainGraph.has_edge(rowsGeneUniprotID.get(int(element[0])),element[4]) == False):
        mainGraph.add_edge(rowsGeneUniprotID.get(int(element[0])),element[4],edge_nodes_attributes=str(rowsGeneUniprotID.get(int(element[0]))+","+element[4]))
        print("New edge is added, index : " , index)

      index+=1
    else:
      index+=1
except Exception as e:
  print("problem is here  2  ", e )

"""
attrs = {str(element[1]): {"geneid": element[0], "protein_class": element[6],"protein_class_name":element[7]},str(element[8]):{ "diseaseid": element[9],"disease_class":element[10],"disease_type":element[12]}}
nx.set_node_attributes(mainGraph,attrs)
"""

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

"""add association between diseases that 2 diseases are already in graph"""

for element in rowsDiseaseDisease:
  if(len(element)>17   and element[16]!=None and element[17] != None and geneDiseaseDict.get(element[16])!=None and geneDiseaseDict.get((element[17]))!=None and mainGraph.has_node(element[16]) == True and mainGraph.has_node(element[17]) == True ):
    mainGraph.add_edge(element[16],element[17],edge_nodes_attributes=str(element[16]+","+element[17]))

"""# Read tab file that is contains gene-gene association."""

# !
import csv
rowsGeneGene = []
with open("../../source-files/BIOGRID-ORGANISM-Homo_sapiens-4.4.217.tab.txt", "r") as file:
    csvreader = csv.reader(file, delimiter='\t')
    headerGeneGene = next(csvreader)
    for row in csvreader:
        rowsGeneGene.append(row)

"""# Add association that 2 genes are already i graph"""

for element in rowsGeneGene:
  firstNodeUniprotID=dictGeneSymbolUniprotID.get(element[2])
  secondNodeUniprotID=dictGeneSymbolUniprotID.get(element[3])
  if(firstNodeUniprotID!=None and secondNodeUniprotID != None and geneDiseaseDict.get(firstNodeUniprotID)!=None and geneDiseaseDict.get(secondNodeUniprotID)!=None and mainGraph.has_node(firstNodeUniprotID) == True and mainGraph.has_node(secondNodeUniprotID) == True ):
    mainGraph.add_edge(firstNodeUniprotID,secondNodeUniprotID,edge_nodes_attributes=str(firstNodeUniprotID+","+secondNodeUniprotID))

"""# networkx to pytorch data"""

from torch_geometric.utils.convert import from_networkx

graphData = from_networkx(mainGraph)

"""!!!
#save dataset to drive
"""

import torch

torch.save(graphData,"../../graph-files/Graph_Comparison_SkipGNN.pt")

print("Graph is built successfully")