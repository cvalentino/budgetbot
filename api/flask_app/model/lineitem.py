class LineItem:

    def __init__(self, categories):
        self.dict = {}
        self.dict['month'] = ''
        self.dict['day'] = ''
        self.dict['description'] = ''
        for category in categories:
            self.dict[category.lower()] = ''

    def toSheetObject(self):
        sheetEntry = []
        for key, value in self.dict.items():
            if key != 'month':
                sheetEntry.append(value)
        return [sheetEntry]
