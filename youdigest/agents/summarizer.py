import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

class Summarizer:
    def __init__(self, api_key: str = None, model: str = "mistral-large-latest", temperature: float = 0):
        # Load environment variables from .env file
        load_dotenv()
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY is not set.")

        # Initialize the Mistral AI model
        self.llm = ChatMistralAI(
            model=model,
            temperature=temperature,
            mistral_api_key=self.api_key
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an assistant that summarizes long transcripts into concise bullet points."),
            ("human", "{input}"),
        ])
        self.chain = self.prompt | self.llm


    # # 1. Charger votre texte long (exemple ici)
    # with open("votre_livre.txt", "r", encoding="utf-8") as f:
    #     long_text = f.read()

    # # 2. Découper le texte en chunks adaptés à la taille du LLM
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    # texts = text_splitter.split_text(long_text)

    # # 3. Créer des embeddings (ici OpenAI, remplacez par vos embeddings locaux si besoin)
    # embedding = OpenAIEmbeddings()

    # # 4. Indexer les chunks dans FAISS
    # vectorstore = FAISS.from_texts(texts, embedding)

    # # 5. Créer un retriever
    # retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # # 6. Initialiser le LLM Mistral (exemple, adaptez selon votre setup)
    # llm = ChatMistralAI(model="mistral-7b-instruct", temperature=0)

    # # 7. Construire la chaîne RAG RetrievalQA
    # qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # # 8. Poser une question
    # question = "Quel est le thème principal du livre ?"
    # answer = qa_chain.run(question)

    # print("Question :", question)
    # print("Réponse :", answer)
    

    # Method to summarize text
    def summarize(self, text: str) -> str:
        result = self.chain.invoke({"input": text})
        return result.content
