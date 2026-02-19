import asyncio
import logging
import aio_pika
from faststream import FastStream
from bot.schemas import IncidentFullInfo
from bot.settings import settings
from faststream.rabbit import RabbitBroker, RabbitQueue, ExchangeType, RabbitExchange


# Настройка логирования
logging.basicConfig(level=logging.INFO)

queue = RabbitQueue(settings.QUEUE_NAME, auto_delete=False)
exchange = RabbitExchange(settings.EXCHANGE_NAME, ExchangeType.FANOUT)
broker = RabbitBroker(url=settings.rabbitmq_url)
app = FastStream(broker)


@broker.subscriber(queue, exchange)
async def incident_tg_handler(incident: IncidentFullInfo):
    logging.info(incident)


async def main():
    async with broker:
        tg_queue: aio_pika.RobustQueue = await broker.declare_queue(queue)
        tg_exchange: aio_pika.RobustExchange = await broker.declare_exchange(exchange)
        await tg_queue.bind(exchange=tg_exchange)
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
