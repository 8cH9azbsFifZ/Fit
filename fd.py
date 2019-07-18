"""Object that defines the structure of a FIT file message field."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

import data
import basetype


class FieldDefinition(data.Data, basetype.BaseType):
    """Object that defines the structure of a FIT file message field."""

    fd_schema = data.Schema(
        'fd',
        collections.OrderedDict(
            [
                ('field_definition_number', ['UINT8', 1, '%x']),
                ('size', ['UINT8', 1, '%x']),
                ('base_type', ['UINT8', 1, '%x'])
            ]
        )
    )

    def __init__(self, file):
        super(FieldDefinition, self).__init__(file, FieldDefinition.fd_schema)

    def base_type(self):
        return self._base_type(self.base_type)

    def type_endian(self):
        return self._type_endian(self.base_type)

    def type_name(self):
        return self._type_name(self.base_type)

    def invalid(self):
        return self._invalid(self.base_type)

    def type_string(self):
        return self._type_string(self.base_type)

    def type_count(self):
        type_size = data.Schema.type_to_size(self.type_string())
        return (self.size / type_size)

    def __str__(self):
        return ("FieldDefinition: type %d: %d of %s" % (self.field_definition_number, self.type_count(), self.type_string()))