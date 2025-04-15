from prompt_toolkit import prompt
from utils.companyUtil import CompanyUtil
from utils.companyCompleter import CompanyCompleter

if __name__ == "__main__":
    companyUtil = CompanyUtil()
    companyUtil.loadCompanyFromFile()

    completer = CompanyCompleter(companyUtil.companyList)
    print("Type to search tickers/companies. Tab/Arrow keys to select.")
    user_input = prompt("Search: ", completer=completer)

    # Output selected ticker
    print(f"\nSelected: {user_input}")