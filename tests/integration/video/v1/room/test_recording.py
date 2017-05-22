# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoomRecordingTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .recordings(sid="RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "processing",
                "date_created": "2015-07-30T20:00:00Z",
                "sid": "RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source_sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "size": 0,
                "type": "audio",
                "duration": 0,
                "container_format": "mka",
                "codec": "OPUS",
                "grouping_sids": {
                    "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                },
                "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "media": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .recordings(sid="RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                .recordings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "recordings": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .recordings.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "recordings": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "completed",
                        "date_created": "2015-07-30T20:00:00Z",
                        "sid": "RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "source_sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "size": 0,
                        "type": "audio",
                        "duration": 0,
                        "container_format": "mka",
                        "codec": "OPUS",
                        "grouping_sids": {
                            "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "media": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .recordings.list()

        self.assertIsNotNone(actual)
