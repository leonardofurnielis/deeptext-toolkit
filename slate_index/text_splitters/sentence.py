from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter

from slate_index.core.document import Document

class SentenceSplitter():

    def __init__(self, 
                 chunk_size: int = 512 , 
                 chunk_overlap: int = 256,
                 length_function = len,
                 separators = ["\n\n", "\n", " ", ""]
                 ) -> None:

        
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.length_function = length_function
        self.separators = separators


    def from_text(self, text: str) -> List[str]: 
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=self.length_function,
            separators=self.separators,
        )
        
        return text_splitter.split_text(text)

    
    def from_documents(self, documents: List[Document]) -> List[Document]: 
        chunks = []
        
        for document in documents:
            texts = self.from_text(document.get_text())

            for text in texts:
                chunks.append(Document(text=text, metadata=document.get_metadata()))

        return chunks