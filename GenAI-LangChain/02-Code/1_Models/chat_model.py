from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# making the object of the class ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)

response = llm.invoke("Who created Python?")

print(response.content)
# this is outdated and will be removed in future versions , we have to use the chatmodels

#1st 
#import 
#all lib install
#indexing : loading 
            # splitting
            # embedding
            # vector storage 
#Retriver 
# Augmentations
# GenerationS
