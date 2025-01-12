"""Class that represents a FIT file header."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import collections

import exceptions
import data


class FileHeader(data.Data):
    """Class that represents a FIT file header."""

    fh_primary_schema = data.Schema(
        'fh_primary',
        collections.OrderedDict(
            [
                ('header_size', ['UINT8', 1, '%d']),
                ('protocol_version', ['UINT8', 1, '%x']),
                ('profile_version', ['UINT16', 1, '%d']),
                ('data_size', ['UINT32', 1, '%d']),
                ('data_type', ['CHAR', 4, '%c'])
            ]
        )
    )
    fh_optional_schema = data.Schema(
        'fh_optional',
        collections.OrderedDict([('crc', ['UINT16', 1, '%x'])])
    )
    profile_version_str = {100 : 'activity', 1602 : 'device'}

    min_file_header_size = 12
    opt_file_header_size = 14
    min_protocol_version = 0x10
    file_data_type = [46, 70, 73, 84]
#    file_data_type = ['.', 'F', 'I', 'T']

    def __init__(self, file):
        """Return a FileHeader instance created by reading data from a Fit file."""
        super(FileHeader, self).__init__(file, FileHeader.fh_primary_schema, [(FileHeader.fh_optional_schema, self.__decode_secondary)])
        self.__check()

    def __decode_secondary(self):
        return (self.header_size >= FileHeader.opt_file_header_size)

    def __check(self):
        if self.header_size < FileHeader.min_file_header_size:
            raise exceptions.FitFileBadHeaderSize("%d < %d" % (self.header_size, FileHeader.min_file_header_size))
        if self.protocol_version < FileHeader.min_protocol_version:
            raise exceptions.FitFileBadProtocolVersion("%d < %d" % (self.protocol_version, FileHeader.min_protocol_version))
        if self.data_type != FileHeader.file_data_type:
            raise exceptions.FitFileDataType("%r < %r" % (self.data_type, FileHeader.file_data_type))

    def __str__(self):
        """Return a string representation of a FileHeader instance."""
        return ("%s(header size %d prot ver %x prof ver %d)" %
                (self.__class__.__name__, self.header_size, self.protocol_version, self.profile_version))
