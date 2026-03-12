import sys
from solution.producer_sol import publishOrder

#Read from command line
ticker = sys.argv[1]
price = sys.argv[2]
sector = sys.argv[3]

#Create routing key
RoutingKey = f"Stock.{ticker}.{price}"

#Implement logic to create a message variable from the variables
message = f"{ticker} is ${price}"
publishOrder(message)