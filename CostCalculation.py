
import urllib.request
import json


# this is a function for calculating the cost of items
# the algorithm of this function is inspired by DFS
# since it is going to the lowest node and start calculating from there
def cost_calc(json_str):

    # variables
    count = 0
    price = 0
    cost = 0

    # convert string object of json to json object
    json_obj = json.loads(json_str)

    for key in json_obj:
        if key == "name":
            pass
        elif key == "count":
            count = json_obj[key]
        elif key == "price":
            price = json_obj[key]
            return count * price
        elif key == "items":
            jso_dump = json.dumps(json_obj[key])
            # call the recursive
            cost += cost_calc(jso_dump)
            return count * cost
        else:
            jso_dump = json.dumps(key)
            # call the recursive
            cost += cost_calc(jso_dump)
    return cost


# the sample in the assignment is initialized
data_set = {

            "name": "a",
            "count": 2,
            "items": [
                        {
                            "name": "x",
                            "count": 1,
                            "price": 1
                        },
                        {
                            "name": "y",
                            "count": 2,
                            "price": 2
                        }
            ]
}

# make a string object of json
json_dump = json.dumps(data_set)
# call cost_calc function for calculating cost
cost1 = cost_calc(json_dump)

# First Sample URL
url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json"
json_dump = urllib.request.urlopen(url)
cost2 = cost_calc(json_dump.read())

# Second Sample URL
url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json"
json_dump = urllib.request.urlopen(url)
cost3 = cost_calc(json_dump.read())

# Third Sample URL
url = "https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json"
json_dump = urllib.request.urlopen(url)
cost4 = cost_calc(json_dump.read())

# prints of cost of each sample
print("Cost1: ", cost1)
print("Cost2: ", cost2)
print("Cost3: ", cost3)
print("Cost4: ", cost4)

