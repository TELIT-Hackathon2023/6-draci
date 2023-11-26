from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import  OpenAI
from langchain.chains import RetrievalQA
from langchain.evaluation import load_evaluator
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from sklearn.metrics.pairwise import cosine_similarity
import os
import nltk

openai_api_key = ""
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
evaluator = load_evaluator("pairwise_embedding_distance",embeddings=embeddings)
loader = TextLoader("dataset_technical.txt")
loader2 = PyPDFLoader("test.pdf")
query = "Which programing languages are  used for software"
query2 = "There any Assistance to disabled people"

def compareEmbeddings(string1,string2):
    return evaluator.evaluate_string_pairs(
        prediction=string1, prediction_b=string2
    )
def embedCriteria(loader,query):

    data=loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    docsearch = FAISS.from_documents(texts, embeddings)


    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())
    result= qa.run(query)
    return result

string1 = embedCriteria(loader,query)
string2 = embedCriteria(loader2,query2)
print(compareEmbeddings(string1, string2))

