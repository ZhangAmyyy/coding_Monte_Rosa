#regular expression check compound
import re
#add a timestamp when returning information
from datetime import datetime
from collections import defaultdict
#the set to register compound
#Desigin: use set, because it just needs O(1) to check whether a element in it
global compound_register_set
compound_register=set()

#Desigin: use map, because well_id and compounds assigned to it is key-value pair
#Design: use set for value, because there is one-to-many relation between well id and compounds
# and set can avoid duplicate and just needs O(1) to check whether a element in it
global well_assignment_map
well_assignment_map=defaultdict(set)


#function used to output information with timestamp
def information_output_with_timestamp(message):
    current_time = datetime.now().strftime('%Y-%M-%D %H:%M:%S')
    print(f"[{current_time}] {message}")

#reset global variables
def reset_global_variables():
    global compound_register, well_assignment_map
    compound_register = set()
    well_assignment_map =defaultdict(set)

# compound register
#Assumption1: the input of the compound is a string
#Assumption2: there is no capacity limitation of register
#compound_register performs the compound registration operation. If the registration is successful, it will print the registration success and return True.
#If registration fails, False is returned: If compound is invalid, print compound is invalid; if compound has been registered, print compoubd has been registered.
def compound_registration(compound):
    #check the validation of compound format
    pattern=r'^MRT-\d{6}$'
    if not re.match(pattern,compound):
        message="The input compound: "+f"{compound}"+ "is invalid."
        information_output_with_timestamp(message)
        return False
    #Check whether compound has been registered
    if compound in compound_register:
        message="The input compound: "+f"{compound}"+" has already been registerred."
        information_output_with_timestamp(message)
        return False
    #register the compound
    compound_register.add(compound)
    message="The input compound: "+f"{compound}"+" is registerred successfully."
    information_output_with_timestamp(message)
    return True

#assign_compound_to_well: the funtion used to assign a compound to a well
#The input is the compound and the well_id
#If operation success, return True, print the successful information
#If not: return False and error information
#Assumption3: Besides the format of well_id: {a uppercase}+{an integer large than 0}, there is no other limitation
#Assumption4: a give compound cannot be added to 2 different well
def assign_compound_to_well(compound,well_id):
    #check the validation of compound format
    pattern=r'^MRT-\d{6}$'
    if not re.match(pattern,compound):
        message="The input compound: "+f"{compound}"+" is invalid."
        information_output_with_timestamp(message)
        return False
    #check the validation of well_id
    pattern=r'^[A-Z]\d+$'
    if not re.match(pattern,well_id):
        message="The input well id: "+f"{well_id}"+" is invalid."
        information_output_with_timestamp(message)
        return False
    #check whether the compound has been registered
    if compound not in compound_register:
        message= "The input compound: "+f"{compound}"+" hasn't been registerd."
        information_output_with_timestamp(message)
        return False
    #check if the compound is already in this given well
    contents=well_assignment_map[well_id]
    if compound in contents:
        message="The input compound: "+f"{compound}"+" has already been assigned to given well: "+f"{well_id}"
        information_output_with_timestamp(message)
        return False
    #assign to well
    contents.add(compound)
    message="The input compound: "+f"{compound}"+" is assigned to given well: "+f"{well_id}"+" successfully."
    information_output_with_timestamp(message)
    return True

#copy_well: copy the compound from one well to another
#return True and output successful information if success, otherwise return False and error information
def copy_well(well_id1,well_id2):
    #check the validation of well_id
    pattern=r'^[A-Z]\d+$'
    if not re.match(pattern,well_id1):
        message="The input well id: "+f"{well_id1}"+" is invalid."
        information_output_with_timestamp(message)
        return False
    pattern=r'^[A-Z]\d+$'
    if not re.match(pattern,well_id2):
        message="The input well id: "+f"{well_id2}"+" is invalid."
        information_output_with_timestamp(message)
        return False
    copy=well_assignment_map[well_id1]
    target=well_assignment_map[well_id2]
    #check if the copy well is empty
    if len(copy)==0:
        message="The copy well: "+f"{well_id1}"+" is empty."
        information_output_with_timestamp(message)
        return False
    #copy
    message="The copy well has: "+f"{copy}"
    information_output_with_timestamp(message)
    message="The target well has: "+f"{target}"
    information_output_with_timestamp(message)
    for compound in copy:
        if compound not in target:
            target.add(compound)
    message="Copy from well: "+f"{well_id1}"+" to well: "+f"{well_id2}"+" successfully."
    information_output_with_timestamp(message)
    message="Now "+f"{well_id2}"+" has: "+f"{target}"
    information_output_with_timestamp(message)
    return True

#get_compounds_from_well: get all the compounds in a given well
#if the well is empty, return an empty list, otherwise return the list of compounds in given well
#if succes, also output successful information, otherwise output error information and empty list
def get_compounds_from_well(well_id):
    result=[]
    #check the validation of well_id
    pattern=r'^[A-Z]\d+$'
    if not re.match(pattern,well_id):
        message="The input well id: "+f"{well_id}"+" is invalid."
        information_output_with_timestamp(message)
        return result
    #extract the compounds from the give well
    compounds=well_assignment_map[well_id]
    for compound in compounds:
        result.append(compound)
    message="Operation Successful!"
    information_output_with_timestamp(message)
    print("The well with id "+f"{well_id}"+ " has compounds: "+f"{result}")
    result=sorted(result)
    return result 

#get_compounds_from_plate get the compounds from a plate
#return the list of compounds, and if plate is empty, output empty information, otherwise successful information
def get_compounds_from_plate():
    result=set()
    if not well_assignment_map:
        message="The plate is empty."
        information_output_with_timestamp(message)
        return list(result)
    for well in well_assignment_map.values():
        for compound in well:
            result.add(compound)
    message="The compounds in this plate: "+f"{result}"
    information_output_with_timestamp(message)
    result=sorted(list(result))
    return result

    