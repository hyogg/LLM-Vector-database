from docarray import BaseDoc
from docarray.typing import NdArray

from module.model import Model

class ToyDoc(BaseDoc):
  text: str = ''
  embedding: NdArray[4096]


from docarray import DocList
import numpy as np
from vectordb import InMemoryExactNNVectorDB, HNSWVectorDB

# Specify your workspace path
db = InMemoryExactNNVectorDB[ToyDoc](workspace='workspace_path')


# Download Data
from datasets import load_dataset
data = load_dataset("juicyjung/easylaw_kr")
print(data)


# Define model
model = Model()



# # Index a list of documents with random embeddings
# doc_list = [ToyDoc(text = i['instruction'], embedding = model.get_embedding(i['instruction'])) for i in data['train']]
# db.index(inputs=DocList[ToyDoc](doc_list))


prompt = "사업장 자동측정기기 및 시료채취기 기준이 어떻게 되나요?"

# Perform a search query
query = ToyDoc(text = prompt, embedding = model.get_embedding(prompt))
results = db.search(inputs=DocList[ToyDoc]([query]), limit=10)



# Save db
db.persist()



# Print out the matches
for m in results[0].matches:
  print(m)