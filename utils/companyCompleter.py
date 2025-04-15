from prompt_toolkit.completion import Completer, Completion

class CompanyCompleter(Completer):
    def __init__(self, companies):
        self.companies = companies  # List of (ticker, name) tuples

    def get_completions(self, document, complete_event):
        word = document.text_before_cursor.lower()
        for ticker, name in self.companies:
            ticker_lower = ticker.lower()
            name_lower = name.lower()
            if ticker_lower.startswith(word) or name_lower.startswith(word):
                yield Completion(text=name, display=f"{ticker} - {name}", start_position=-len(word))
