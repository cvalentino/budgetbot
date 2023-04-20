class LineItem:

    def __init__(self, categories):
        self.dict = {}
        self.dict['Date'] = ''
        self.dict['Description'] = ''
        for category in categories:
            self.dict[category] = ''

    def toSheetObject(self):
        sheetEntry = []
        for label, value in self.dict.items():
            sheetEntry.append(value)
        return [sheetEntry]
