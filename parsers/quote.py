from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Content: {self.content} by {self.author}.'

    @property
    def content(self):
        content = QuoteLocators.CONTENT
        return  self.parent.select_one(content).string

    @property
    def author(self):
        author = QuoteLocators.AUTHOR
        return self.parent.select_one(author).string

    @property
    def tags(self):
        tags = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(tags).string]