# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(
    weather, time_of_day, milking_status,
    location, season, slurry, grass):
    if location == 'pasture' and  (time_of_day == 'night' or weather == 'rainy'):
        return 'take cows to cowshed'
    if milking_status or grass or slurry:
        statement = """"""
        if location == 'pasture':
            statement += 'take cows to cowshed\n'
        if milking_status:
            statement += 'milk cows'
        elif slurry and weather in ('rainy', 'neutral'):
            statement += 'fertilize pasture'
        elif grass and season == 'spring' and weather == 'sunny':
            statement += 'mow grass'
        if location == 'pasture':
            statement += '\ntake cows back to pasture'
        if statement:
            return statement
        return 'wait'       
    return 'wait'

