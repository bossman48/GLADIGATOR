import torch

#print("tempString: isUTFCeckCompleted : ", isUTFCeckCompleted("tempString"))
#print("François: isUTFCeckCompleted : ", isUTFCeckCompleted("François"))
# importing the requests library
import requests
import sys

pretrainedModelPath = sys.argv[1]
geneID = sys.argv[2]
diseaseID = sys.argv[3]

diseaseContextFound = False
geneProteinSequenceFound = False


# command for run script.
# python MakePrediction.py Graph_Own_0.05_model.pth P18031 C0001432
# python MakePrediction.py Graph_Own_0.5_model.pth HPSE C0001432

#Gene

# Gene 
def getUniprotIDFromGene(gene:str):
  try:
    # api-endpoint
    listData=[]
    URL = "https://rest.uniprot.org/uniprotkb/search?&query=gene:"+gene
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    tempData = []
    try:
      for element in data["results"]:
        for subelement in element:
          #print("subelement : ", subelement, " and : ", element[subelement])
          if(subelement == "primaryAccession"):
            tempData.append(element[subelement])
          elif(subelement == "secondaryAccessions"):
            for i in element[subelement] :
              tempData.append(i)
            #tempData.append(element[subelement])

        
      return tempData

    except:
      return tempData
  except Exception as exc:
    print(exc)
    return []

#print("getUniprotIDFromGene : ", getUniprotIDFromGene(geneID))


# Disease

import config

#get apikey
apikey = config.config.get("apikey")



def isUTFCeckCompleted(tempString):
  valid_utf8 = True
  try:
      tempString.encode(encoding='utf-8').decode('ascii')
  except UnicodeDecodeError:
      valid_utf8 = False

  return valid_utf8




def getDiseaseDescription(uniprotid:str):
  try:
    # api-endpoint
    listData=[]
    URL = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/"+uniprotid+"/definitions?apiKey="+apikey
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    sources = ["DO", "EFO", "HPO", "ICD9CM", "ICD10", "ICD10CM", "MSH", "NCI", "CCC","NANDA-I","PNDS","ICF","OMIM", "ORDO","MONDO","CSP","ORPHANET","AIR","CHV","GO","PSY","SNOMEDCT_US","JABL","LNC","UWDA"]
    tempData = ""
    try:
      for element in data["result"]:
        if element["rootSource"] in sources:
          tempString = element["value"]
          if(isUTFCeckCompleted(tempString)):
            tempData+=element["value"]+" "
        
      return tempData

    except:
      return tempData
  except Exception as exc:
    print(exc)
    return ""

def getDiseaseName(uniprotid:str):
  try:
    # api-endpoint
    listData=[]
    URL = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/"+uniprotid+"?apiKey="+apikey
    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    # extracting data in json format
    data = r.json()
    tempData = ""
    try:
      for element in data["result"]:
        if(element == "name"):
            tempData = data["result"]["name"]
        
      return tempData

    except:
      return tempData
  except Exception as exc:
    print(exc)
    return ""

print(diseaseID + " name is :" , getDiseaseName(diseaseID))
print(diseaseID+ " descripton is :" , getDiseaseDescription(diseaseID))


# Generate Disease Embeddings


import numpy as np
from transformers import AutoTokenizer, AutoModel
"""
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")

model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")

_ = model.save_pretrained("../../source-files/")
_ = tokenizer.save_pretrained("../../source-files/")
"""
try:
  model = AutoModel.from_pretrained("../source-files/")
  tokenizer = AutoTokenizer.from_pretrained("../source-files/")
except Exception as exc:
  print("Biobert model did not found in the source-files path. Therefore, Biobert pretrained model will be downloaded from internet.")
  tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")

  model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")

  print("Biobert pretrained model download process completed. Saving process will be run.")
  _ = model.save_pretrained("../source-files/")
  _ = tokenizer.save_pretrained("../source-files/")


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


#print("Disease Embeddings : ", diseaseDescriptionEmbedding(getDiseaseName(diseaseID)+ " " +getDiseaseDescription(diseaseID)))


# Generate Gene Embeddings
import numpy as np
import h5py

def proteinSequenceEmbedding(uniprotID):
  try:
    with h5py.File("../source-files/per-protein.h5", "r") as file:

      for sequence_id, embedding in file.items():
        if sequence_id == uniprotID:
            return np.insert(embedding[0:embedding.size],0,np.zeros(768)), True

    return np.zeros(1792), False
  except:
    print("An exception occurred")
    return np.zeros(1792), False

"""
proteinSequenceTemp, returnType = proteinSequenceEmbedding(geneID)
print("Protein Embeddings : ", proteinSequenceTemp, " return value:  ", returnType)
"""
"""
vectorizedTemp = proteinSequenceEmbedding("P04217")
vectorizedTemp2 = proteinSequenceEmbedding("O95477")
vectorizedTemp3 = proteinSequenceEmbedding("O9123")
print(vectorizedTemp)
print(len(vectorizedTemp))
print(vectorizedTemp2)
print(len(vectorizedTemp2))
print(vectorizedTemp3)
print(len(vectorizedTemp3))
print(type(vectorizedTemp2))
print(type(vectorizedTemp2[0]))
"""

# edge_label_index
def buildEdgeLabelIndex():
  index= 0
  edge_label_index2 = torch.zeros([2, 1], dtype=torch.int32)
  edge_label2 = torch.zeros([1], dtype=torch.int32)
  while(index<1 and len(graphData.edge_index[0])>0):
    edge_label_index2[0][index] = graphData.edge_index[0][0]
    edge_label_index2[1][index] = graphData.edge_index[1][0]
    edge_label2[0] = 1
    index+=1
  return edge_label_index2, edge_label2

#Build graph
import networkx as nx
mainGraph = nx.Graph()
graphConstructed = False


# build disease node
diseaseName = getDiseaseName(diseaseID)
diseaseDescription = getDiseaseDescription(diseaseID)

if(diseaseName != "" or diseaseDescription != ""):
    tempEmbeddingDisease = diseaseDescriptionEmbedding( getDiseaseName(diseaseID)+ " " +getDiseaseDescription(diseaseID))
    mainGraph.add_nodes_from([(diseaseID, {'x': tempEmbeddingDisease,'id':diseaseID,"gene_smybol":""})])
    diseaseContextFound =True
else:
    print("Disease context cannot be found")

geneRelatedProteinsUniprotIDs = getUniprotIDFromGene(geneID)
print("Gene related proteins uniprot ids: ", geneRelatedProteinsUniprotIDs)

for element in geneRelatedProteinsUniprotIDs:
  tempEmbeddingProt, geneProteinSequenceFound = proteinSequenceEmbedding(element)
  if(geneProteinSequenceFound):
    print("gene node is added. UniprotID : ", element)
    mainGraph.add_nodes_from([(geneID, {'x': tempEmbeddingProt,'id':geneID,"gene_smybol":geneID})])
    break
  else:
    print("Protein embeddings cannot be found. UniprotID : ", element)

if(mainGraph.has_node(geneID) and mainGraph.has_node(diseaseID)):           
  #mainGraph.add_edge(geneID,diseaseID,edge_nodes_attributes=str(geneID+","+diseaseID))
  #mainGraph.add_edge(diseaseID,geneID,edge_nodes_attributes=str(geneID+","+diseaseID))
  graphConstructed = True


if(graphConstructed):
  """# networkx to pytorch data"""

  from torch_geometric.utils.convert import from_networkx

  graphData = from_networkx(mainGraph)

  #print("graph Data: ", graphData)
  #print("graph Data Edge Index: ", graphData["edge_index"])
  #print("graph Data id: ", graphData["id"])
  graphData["edge_label_index"] = graphData["edge_index"]
  graphData["edge_label"] = torch.zeros([2], dtype=torch.int32)
  #print("graphData[edge_label_index]: ", graphData["edge_label_index"])
  #print("graphData[edge_label] : ", graphData["edge_label"])


  # Machine Learning Model

  import os.path as osp
  from sklearn.model_selection import KFold

  import torch
  from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
  import numpy as np
  import torch_geometric.transforms as T
  from torch_geometric.datasets import Planetoid
  from torch_geometric.nn import GCNConv
  from torch_geometric.utils import negative_sampling
  from torch.utils.data import Dataset, DataLoader,TensorDataset,random_split,SubsetRandomSampler, ConcatDataset
  from torch_geometric.utils import train_test_split_edges
  from sklearn.metrics import roc_auc_score
  from sklearn.metrics import average_precision_score, precision_recall_curve
  from sklearn.metrics import auc

  # 2 layer network
  class Net1(torch.nn.Module):
      def __init__(self, in_channels, hidden_channels, out_channels):
          super().__init__()
          self.conv1 = GCNConv(in_channels, hidden_channels)
          self.conv2 = GCNConv(hidden_channels, out_channels)

      def encode(self, x, edge_index):
          x = self.conv1(x, edge_index).relu()
          return self.conv2(x, edge_index)


      def decode(self, z, edge_label_index):
          
          print("z[edge_label_index[0]] : ", z[edge_label_index[0]])
          print("z[edge_label_index[1]] : ", z[edge_label_index[1]])
          
          return (z[edge_label_index[0]] * z[edge_label_index[1]]).sum(dim=-1)

      def decodePrediction(self, z):
          """
          print("z[0] : ", z[0])
          print("z[1] : ", z[1])
          print("z[0] * z[1] : ", z[0] * z[1])
          print("(z[0] * z[1]).sum(dim=-1) : ", (z[0] * z[1]).sum(dim=-1))
          print("(z[0] * z[1]).sum(dim=-1).sigmoid() : ", (z[0] * z[1]).sum(dim=-1).sigmoid())
          #print("(z[0] * z[1]).sigmoid() : ", (z[0] * z[1]).sigmoid())
          """
          return (z[0] * z[1]).sum(dim=-1)
          
      def decode_all(self, z):
          prob_adj = z @ z.t()
          return (prob_adj > 0).nonzero(as_tuple=False).t()

  if(geneProteinSequenceFound and diseaseContextFound):
      model = Net1(1792,112,28)
      model = torch.load(pretrainedModelPath, weights_only=False)
      
      #model.load_state_dict(torch.load(pretrainedModelPath))
      model.eval()

      #print("Graph Data : ", graphData)
      #print("Graph Data edge index : ", graphData["edge_index"])
      z = model.encode(graphData.x, graphData.edge_index)
      #print("z : ",z)
      out = model.decode_all(z).view(-1).sigmoid()
      #print("out : ", out)
      out2 = torch.round(model.decodePrediction(z).view(-1).sigmoid())
      #out2 = torch.round(model.decode(z,graphData["edge_label_index"]).view(-1).sigmoid())
      print("\n\nout2 : ", out2)
      #out2 = torch.round(model.decode(z,graphData["edge_label_index"]).view(-1).sigmoid())
      print("\n\nPrediction Output : ", int(out2[0]))
  elif(not geneProteinSequenceFound):
      print("Cannot make prediction, gene/protein seqeunce not found")
  elif(not diseaseContextFound):
      print("Cannot make prediction, disease context not found")

else:
  print("Graph is not constructed")