import json

from contractor.dao import ContractorDAO
from event.dao import EventDAO


class ConsumerMethods:
    @staticmethod
    async def process_incoming_ack(message):
        await message.ack()
        body = json.loads(message.body)
        return await EventDAO.update(body["eventId"], {"status": "response_received"})

    @staticmethod
    async def process_incoming_remove_organization(message):
        await message.ack()
        body = json.loads(message.body)
        return await ContractorDAO.hide_by_organization_id(body["organizationId"])
