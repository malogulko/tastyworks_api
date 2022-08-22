from tastyworks.dxfeed.mapped_item import MappedItem
import datetime


class Quote(MappedItem):
    DXFEED_TEXT = 'Quote'

    def _process_fields(self, data_dict: dict):
        return data_dict

    def __init__(self, data=None):
        super().__init__(data=data)
