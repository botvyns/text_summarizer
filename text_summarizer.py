from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline

class TextSummarizer:
    def __init__(self, model_id: str = "cnicu/t5-small-booksum", max_input_length: int = 512):
        """
        Initialize the TextSummarizer with a specified model and maximum input length.

        Args:
            model_id (str): The model identifier for the HuggingFace model.
            max_input_length (int): The maximum length for input text chunks.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        self.pipe = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)
        self.hf_pipeline = HuggingFacePipeline(pipeline=self.pipe)
        self.max_input_length = max_input_length

    def chunk_text(self, text: str) -> list:
        """
        Split the input text into chunks by tokens.

        Args:
            text (str): The input text to be split.

        Returns:
            list: A list of text chunks.
        """
        tokens = self.tokenizer(text, return_tensors='pt', truncation=False)["input_ids"][0]
        chunks = []
        for i in range(0, len(tokens), self.max_input_length):
            chunk_tokens = tokens[i:i + self.max_input_length]
            chunk_text = self.tokenizer.decode(chunk_tokens, skip_special_tokens=True)
            chunks.append(chunk_text)
        return chunks

    def summarize(self, text: str) -> str:
        """
        Summarize the input text.

        Args:
            text (str): The input text to be summarized.

        Returns:
            str: The summarized text.
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        chunks = self.chunk_text(text)
        summaries = ' '.join([self.hf_pipeline(chunk) for chunk in chunks])
        return summaries