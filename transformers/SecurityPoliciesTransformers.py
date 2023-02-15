import json
import pandas as pd
import logging
import GenericTransformers

def GetShowAsCsv(jsonResults):
    columns = ['id', 'name','policyType','createdAt','updatedAt', 'groups']
    return GenericTransformers.GetShowAsCsvNoNesting(jsonResults,'securityPolicy',columns)

def GetListAsCsv(jsonResults):
    columns = ['id', 'name','policyType', 'groups']
    return GenericTransformers.GetListAsCsv(jsonResults,columns)

def GetAddOrRemoveGroupsAsCsv(jsonResults):
    columns = ['ok','error','id', 'name','groups']
    return GenericTransformers.GetUpdateAsCsvNoNesting(jsonResults,'securityPolicyUpdate',columns)