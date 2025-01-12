"""FIT file definition message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections

import data
import fields
from developer_field_definition import DeveloperFieldDefinition
from definition_message_data import DefinitionMessageData
from field_definition import FieldDefinition
from message_type import MessageType


class DefinitionMessage(data.Data):
    """FIT file definition message."""

    dm_primary_schema = data.Schema(
        'dm_primary',
        collections.OrderedDict(
            [('reserved', ['UINT8', 1, '%x']), ('architecture', ['UINT8', 1, '%x'])]
        )
    )
    dm_secondary_schema = data.Schema(
        'dm_secondary',
        collections.OrderedDict(
            [('global_message_number', ['UINT16', 1, '%x']), ('fields', ['UINT8', 1, '%x'])]
        )
    )
    dm_dev_schema = data.Schema(
        'dm_dev',
        collections.OrderedDict(
            [('dev_fields', ['UINT8', 1, '%x'])]
        )
    )

    def __init__(self, record_header, dev_field_dict, file):
        """
        Return a DefinitionMessage instance created by reading data from a FIT file.

        Paramters:
            record_header (RecordHeader): the record header associated with this definition message.
            dev_field_dict (dict): a dictionary of developer defoined fields in the FIT file.
            file (File): the FIT file instance to read the definition message data from.
        """
        super(DefinitionMessage, self).__init__(file, DefinitionMessage.dm_primary_schema, [(DefinitionMessage.dm_secondary_schema, self.__decode_secondary)])

        self.message_type = MessageType.get_type(self.global_message_number)
        self.message_data = DefinitionMessageData.get_message_definition(self.message_type)

        self.field_definitions = []
        for index in xrange(self.fields):
            field_definition = FieldDefinition(file)
            self.file_size += field_definition.file_size
            self.field_definitions.append(field_definition)

        self.has_dev_fields = record_header.developer_data()
        self.dev_field_definitions = []
        if self.has_dev_fields:
            self._decode(DefinitionMessage.dm_dev_schema)
            for index in xrange(self.dev_fields):
                dev_field_definition = DeveloperFieldDefinition(dev_field_dict, file)
                self.file_size += dev_field_definition.file_size
                self.dev_field_definitions.append(dev_field_definition)

    def __decode_secondary(self):
        self.endian = data.Architecture(self.architecture)
        return True

    def field(self, field_number):
        """Return an instance of the proper Field subclass for the given field definition."""
        return DefinitionMessageData.reserved_field_indexes.get(field_number, self.message_data.get(field_number, fields.UnknownField(field_number)))

    def __str__(self):
        """Return a string representation of a DefinitionMessage instance."""
        return ("DefinitionMessage: %r %d %s fields" % (self.message_type, self.fields, self.endian.name))
