# ---------------  Dependencies --------------------------------#
import json

#  -------------------------------------------------------------#
# ---------------  Internal Modules ----------------------------#
from TestStepTemplate import *
# from corehit import *
# from coretests import *


# Input Data
# data=json.load(open('Runner_v1.json', 'r'))
teststeps=[{
"method":'GET',
"url":'https://api.myjson.com/bins/xw2f9',
"payload":{
'data':{}
},
# ---------------- Scripts and Tests -------------------------
"prehit":{},
"tests":{
    'test_status_code':{'expected':200}
},
"posthit":{},
# ---------------- Response -------------------------
"response":{}
}]

T1=TestStepTemplate(teststeps)
T1.runnit()


# for item in teststep:
#     response=Hitit(item["method"],item["url"])
#     test_status_code_it(response,item["tests"]['test_status_code']['expected'])
