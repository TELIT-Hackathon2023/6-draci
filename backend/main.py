from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import  OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain.evaluation import load_evaluator
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader, TextLoader
from sklearn.metrics.pairwise import cosine_similarity
import os
import nltk

openai_api_key = ""
llm = OpenAI(openai_api_key=openai_api_key,temperature=0.9)




loaders = {
    "technical": TextLoader("dataset_technical.txt"),
    "functional": TextLoader("dataset_functional.txt"),
    "compliance": TextLoader("dataset_compliance.txt"),
    "domain": TextLoader("dataset_domain.txt"),
}

topic = ["technical"]

technical_query = f"Summarize how should RFP files must look like from functional point of view"
functinal_query = "Summarize how should RFP files must look like from technical point of view"
compliance_query = "Summarize how should RFP files must look like from compliance point of view"
domain_query = "Summarize how should RFP files must look like from domain point of view"

query_pdf ="""Summarize how is RFP file look like from function point of view" """

query_summary="""Write summary about document using in these points,to each point write at least 3 sentences corresponding to information from document.
For each point, there is description about what should data be :

Problem Statement: A brief description of the issue or requirement that the RFP aims to resolve.
Scope of the Work: The project's boundaries, outlining what needs to be achieved and the expected deliverables.
Required Technology Stack: A list of necessary technology tools, frameworks, and languages needed to complete the work.
Pricing Model: Details on how the costs of the work will be calculated and charged, specifying whether it's Time and Materials (T&M) or a Fixed Price.
Service Level Agreements (SLAs): Agreed-upon levels of service performance and availability, including penalties for non-compliance.
Selection Criteria: The standards or requirements that proposals must meet to be considered for selection.
Timelines: Key dates and milestones for the RFP processing schedule.
Contact Details: Information for the point of contact, including name, address, phone number, and email.
Penalty Clauses: Conditions under which penalties may be applied for failing to meet the terms of the contract.
Required Offer Type (Binding or Non-Binding): Clarification on whether proposals are legally binding and the associated conditions for their acceptance."""


summary_template="""Fill given data to example in <t> </t> ,must be formated in json , without parethences
<t>
"problem statement": "",
"scope of the work": "",
"required technology stack": "",
"pricing model": "",
"service level agreements (slas)": "",
"compliance": "",
"selection criteria": "",
"timelines": "",
"contact details": "",
"penalty clauses": "",
"required offer type (binding or non-binding)": ""
</t>
{context}

"""



template = """
Fill given data to e
{context}
Question: {question}
Helpful Answer:"""


summary_prompt = PromptTemplate.from_template(summary_template)

def compareEmbeddings(string1, string2):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    evaluator = load_evaluator("pairwise_embedding_distance", embeddings=embeddings)
    return evaluator.evaluate_string_pairs(
        prediction=string1, prediction_b=string2
    )

def embendingsCriteria(loader, query):

    data = loader.load()


    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)

    docsearch = FAISS.from_documents(texts, embeddings)

    qa = RetrievalQA.from_chain_type(
        llm=llm, chain_type="map_reduce", retriever=docsearch.as_retriever()
    )


    result = qa.run(query)
    return result

def embendingsSummary(loader, query,prompt):
    data = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    if texts:
        docsearch = FAISS.from_documents(texts, embeddings)

        qa = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(), chain_type_kwargs={"prompt": prompt}
        )

        result = qa.run(query)
        return result
    return "Corupted FILE!!"
# Example usage
#string1 = embedCriteria(loaderFolder, technical_query)

def getCriteriaValues(pdfPath):
    prompts =["fuctional","technical","compliance","domain"]
    loadUserData = PyPDFLoader(pdfPath)
    loaderFolder = DirectoryLoader('./files', glob='**/*.txt')
    result = []
    for x in prompts:
        pdf = embendingsCriteria(loadUserData,f"Summarize how is RFP file look like from {x} point of view")
        dataset = embendingsCriteria(loaderFolder, f"Summarize how should RFP files must look like from {x} point of view")
        r = compareEmbeddings(pdf, dataset)
        result.append({x: r})
    return result
print(getCriteriaValues("vyhra/tes2.pdf"))


def getSummaryValues(pdfPath):
    loadUserData = PyPDFLoader(pdfPath)
    res = embendingsSummary(loadUserData,query_summary,summary_prompt)
    return res
print(getSummaryValues("vyhra/tes2.pdf"))

