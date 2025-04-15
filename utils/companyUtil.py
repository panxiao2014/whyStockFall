

class CompanyUtil():
    def __init__(self):
        self.companyList = []
        return
    
    def loadCompanyFromFile(self):
        #read csv file from data/tikers.csv, save each row of the file to companyList.
        #the element of the list is a list of two elements, the first is the ticker, the second is the name of the company.
        with open("data/tickers.csv", "r") as f:
            next(f) #skip the first line
            for line in f:
                self.companyList.append(line.strip().split(","))
