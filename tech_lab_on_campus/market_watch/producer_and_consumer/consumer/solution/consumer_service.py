import sys
from consumer_sol import mqConsumer

# format: STOCK.ticker.sector
sector, queue_name = sys.argv[1], sys.argv[2]
binding_key = "#.#.{sector}"
exchange_name = "Tech Lab Topic Exchange"
consumer = mqConsumer(binding_key, exchange_name, queue_name)
consumer.startConsuming()