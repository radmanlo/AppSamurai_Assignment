# AppSamurai_Assignment
Cost Calculation Program

# The Case:
We want you to write a cost calculation program that finds the cost of the item that can contain
several parts. For example, item 'a' consists of 1 of 'x' and 2 of 'y's. Each part has its own price,
'x's price 1 unit and 'y's price 2 unit, so a 'a's cost is 1*1 + 2*2 = 5 units.
Items' prices and parts are given in json format, you need to read json from url and decode. You
will calculate the cost and write it to the console. Please note that item names are unique for
each item.
Json of given sample;
{
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
Expected result;
Cost of item 'a' is 10 units. // please note that 1 'a's cost is 5 but there are 2 of it so 2 * 5 = 10
units.
sample urls;
https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_1.json
https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_2.json
https://prod-storyly-media.s3.eu-west-1.amazonaws.com/test-scenarios/sample_3.json