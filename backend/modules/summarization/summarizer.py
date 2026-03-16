from transformers import pipeline


class PolicySummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Initializes the summarization model.
        BART has a 1024-token limit; we truncate input to stay safe.
        """
        try:
            self.summarizer = pipeline("summarization", model=model_name)
            self._use_summarization = True
        except Exception:
            self.summarizer = pipeline("text-generation", model=model_name)
            self._use_summarization = False

    def generate_summary(self, text: str, max_l: int = 150, min_l: int = 50) -> str:
        if not text or len(text) < 100:
            return text

        # BART max 1024 tokens (~4 chars/token) - truncate to stay safe
        input_text = text[:900]

        try:
            if self._use_summarization:
                result = self.summarizer(
                    input_text,
                    max_length=max_l,
                    min_length=min_l,
                    do_sample=False,
                )
                return result[0]["summary_text"].strip()
        except Exception:
            pass

        # Fallback: extractive summary (first sentences)
        sents = [s.strip() for s in input_text.replace("\n", " ").split(". ") if len(s.strip()) > 30]
        return ". ".join(sents[:4]) + "." if sents else input_text[:500]