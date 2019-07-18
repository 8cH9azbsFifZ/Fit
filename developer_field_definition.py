"""Objects defining FIT file developer fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

import data
import base_type
import fields
import exceptions


class DeveloperFieldDefinition(data.Data, base_type.BaseType):
    """Developer filed definitions decoded from a FIT file."""

    dfd_schema = data.Schema(
        'dfd_schema',
        collections.OrderedDict(
            [
                ('field_number', ['UINT8', 1, '%x']),
                ('size', ['UINT8', 1, '%x']),
                ('developer_data_index', ['UINT8', 1, '%x'])
            ]
        )
    )

    def __init__(self, dev_field_dict, file):
        super(DeveloperFieldDefinition, self).__init__(file, DeveloperFieldDefinition.dfd_schema)
        self.dev_field = dev_field_dict.get(self.field_number)
        if self.dev_field is None:
            raise exceptions.FitUndefDevMessageType('Dev field %d undefined in %r' % (self.field_number, dev_field_dict))
        self.field_name = self.dev_field['field_name'].value
        self.native_message_num = self.dev_field['native_message_num'].value
        self.native_field_num = self.dev_field['native_field_num'].value
        self.units = self.dev_field['units'].value
        self.offset = self.dev_field['offset'].value
        self.scale = self.dev_field['scale'].value

    def __base_type_value(self):
        return self.dev_field['fit_base_type_id'].orig

    def field(self):
        # if self.native_message_num is not None and self.native_field_num is not None:
        #     message_data = DefinitionMessageData.get_message(self.native_message_num)
        #     field_dict = message_data[1]
        #     return field_dict[self.native_field_num]
        return fields.DevField('dev_' + self.field_name, self.units, self.scale, self.offset)

    def base_type(self):
        return self._base_type(self.__base_type_value())

    def type_endian(self):
        return self._type_endian(self.__base_type_value())

    def type_name(self):
        return self._type_name(self.__base_type_value())

    def invalid(self):
        return self._invalid(self.__base_type_value())

    def type_string(self):
        return self._type_string(self.__base_type_value())

    def type_count(self):
        type_size = data.Schema.type_to_size(self.type_string())
        return (self.size / type_size)

    def __str__(self):
        return ("%s: type %d: %d %d of %s" % (self.__class__.__name__, self.field_number, self.developer_data_index, self.type_count(), self.type_string()))