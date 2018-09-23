#!/usr/bin/env python

#
# copyright Tom Goetz
#

import enum


class UnknownMessageType():
    def __init__(self, index):
        self.value = index
        self.name = 'unknown_%d' % index

    def __eq__(self, other):
        return other and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.value

    def __repr__(self):
        return '<UnknownMessageType.%s: %d>' % (self.name, self.value)


class MessageType(enum.Enum):

    file_id                         = 0
    capabilities                    = 1
    device_settings                 = 2
    user_profile                    = 3
    hrm_profile                     = 4
    sdm_profile                     = 5
    bike_profile                    = 6
    zones_target                    = 7
    hr_zone                         = 8
    power_zone                      = 9
    # 11 is unknown
    met_zone                        = 10
    sport                           = 12
    # 13,14 are unknown
    unknown_13                      = 13
    goal                            = 15
    # 16,17 are unknown
    session                         = 18
    lap                             = 19
    record                          = 20
    event                           = 21
    source                          = 22
    device_info                     = 23
    # 24,25 are unknown
    unknown_24                      = 24
    workout                         = 26
    workout_step                    = 27
    schedule                        = 28
    location                        = 29
    weight_scale                    = 30
    course                          = 31
    course_point                    = 32
    totals                          = 33
    activity                        = 34
    # 36 not known
    software                        = 35
    file_capabilities               = 37
    mesg_capabilities               = 38
    field_capabilities              = 39
    # 40-48 not known
    file_creator                    = 49
    blood_pressure                  = 51
    # 52 not known
    speed_zone                      = 53
    # 54 not known
    monitoring                      = 55
    # 56-71 not known
    training_file                   = 72
    # 73-77 not known
    hrv                             = 78
    # 79 not known
    ant_rx                          = 80
    ant_tx                          = 81
    # 83-100 not known
    ant_channel_id                  = 82
    length                          = 101
    # 102 not known
    monitoring_info                 = 103
    battery                         = 104
    pad                             = 105
    slave_device                    = 106
    # 107-126 not known
    connectivity                    = 127
    weather_conditions              = 128
    weather_alert                   = 129
    # 130 not known
    cadence_zone                    = 131
    hr                              = 132
    # 133-141 not known
    unknown_140                     = 140
    unknown_141                     = 141
    segment_lap                     = 142
    # 143, 144 not known
    memo_glob                       = 145
    # 146 not known
    sensor                          = 147
    segment_id                      = 148
    segment_leaderboard_entry       = 149
    segment_point                   = 150
    segment_file                    = 151
    # 152-157 not known
    workout_session                 = 158
    watchface_settings              = 159
    gps_metadata                    = 160
    camera_event                    = 161
    timestamp_correlation           = 162
    # 163 not known
    gyroscope_data                  = 164
    accelerometer_data              = 165
    # 166 not known
    three_d_sensor_calibration      = 167
    # 168 not known
    video_frame                     = 169
    # 170-173 not known
    obdii_data                      = 174
    # 175,176 not known
    nmea_sentence                   = 177
    aviation_attitude               = 178
    # 179-183 not known
    video                           = 184
    video_title                     = 185
    video_description               = 186
    video_clip                      = 187
    ohr_settings                    = 188
    # 189-199 not known
    exd_screen_configuration        = 200
    exd_data_field_configuration    = 201
    exd_data_concept_configuration  = 202
    # 203-205 not known
    field_description               = 206
    dev_data_id                     = 207
    magnetometer_data               = 208
    barometer_data                  = 209
    one_d_sensor_calibration        = 210
    # 211-224 not known
    set                             = 225
    # 226 not known
    stress_level                    = 227
    # 228-241 not known
    unknown_233                     = 233
    unknown_241                     = 241
    # 242-257 not known
    dive_settings                   = 258
    dive_gas                        = 259
    # 260,261 not known
    dive_alarm                      = 262
    # 263 not known
    exercise_title                  = 264
    # 265-267 not known
    dive_summary                    = 268
    unknown_273                     = 273
    unknown_284                     = 284
    #
    #
    #
    mfg_range_min                   = 0xFF00
    mfg_range_max                   = 0xFFFE

    @classmethod
    def get_type(cls, message_number):
        try:
            return cls(message_number)
        except ValueError:
            return UnknownMessageType(message_number)
