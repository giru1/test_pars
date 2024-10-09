from event.base_producer import Producer

class RemoveRmkProducer(Producer):
    module = "workplace"
    event = "removeRmk"
    event_consumers = ["store"]
