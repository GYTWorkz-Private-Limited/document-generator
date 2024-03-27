
from langchain.text_splitter import NLTKTextSplitter

class NLTKSplitter:
    def __init__(self) -> None:
        self.splitter = NLTKTextSplitter()

    def semantic_split(self, text : any):
        return self.splitter.split_text(text)
