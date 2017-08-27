
# ---------------  Dependencies --------------------------------#
from pprint import pprint
from colorama import init
from colorama import Fore, Back, Style
init()



# -------------------------------------------------------------------#
# ---------------  Tests functions ----------------------------------#
# -------------------------------------------------------------------#


# ----------  Status Code validation -----------------#
def test_status_code_it(response,expected):
		print (Fore.BLUE + "\nTest : status code should be :"+Fore.YELLOW + str(expected) + Style.RESET_ALL)
		try:
			assert (response.status_code==expected)
			print (Fore.GREEN +"Test Passed" + Fore.BLUE +" Status code is "+ Fore.YELLOW  + str(response.status_code)+ Style.RESET_ALL)
		except AssertionError:
			print (Fore.RED + "Test Failed" + Fore.BLUE + " Status code is "+ Fore.YELLOW + str(response.status_code)+ Style.RESET_ALL)