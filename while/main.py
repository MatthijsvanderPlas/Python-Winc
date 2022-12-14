from helpers import random_koala_fact
import re

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
def unique_koala_facts(i):
    koala_facts_list = []
    count = 0
    while(len(koala_facts_list) < i):
        if(count == 1000):
            break
        new_fact = random_koala_fact()
        if new_fact not in koala_facts_list:
            koala_facts_list.append(new_fact)
            continue        
        count += 1
    return koala_facts_list
 
def num_joey_facts():
    first_fact = []
    result = []
    count = 0
    while(count <= 10):
        new_fact = random_koala_fact()
        if count == 0:
            first_fact.append(new_fact)
            if 'joey' in new_fact:
                result.append(new_fact)
            count += 1
            continue
        if new_fact == first_fact[0]: # Same fact has been returned 
            count += 1 
            continue
        if 'joey' in new_fact:
            if new_fact not in result:
                result.append(new_fact)
        
    return len(result)

def koala_weight():
    kg = 0
    while(kg == 0):
        fact = random_koala_fact()
        if 'kg' in fact:
           res = re.search('([0-9]+)+(kg)', fact).group(0)
           kg = int(res[:-2])
    return kg
            
    
if __name__ == "__main__":
    print(random_koala_fact())
    print(koala_weight())
   