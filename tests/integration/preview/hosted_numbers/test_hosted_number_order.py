# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class HostedNumberOrderTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_sid": "AD11111111111111111111111111111111",
                "call_delay": 15,
                "capabilities": {
                    "sms": true,
                    "voice": false
                },
                "cc_emails": [
                    "aaa@twilio.com",
                    "bbb@twilio.com"
                ],
                "date_created": "2017-03-28T20:06:39Z",
                "date_updated": "2017-03-28T20:06:39Z",
                "email": "test@twilio.com",
                "extension": "5105",
                "failure_reason": "",
                "friendly_name": "friendly_name",
                "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                "phone_number": "+14153608311",
                "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "signing_document_sid": "PX11111111111111111111111111111111",
                "status": "received",
                "unique_name": "foobar",
                "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_attempts": 0,
                "verification_call_sids": [
                    "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                ],
                "verification_code": "8794",
                "verification_document_sid": null,
                "verification_type": "phone-call"
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_sid": "AD11111111111111111111111111111111",
                "call_delay": 15,
                "capabilities": {
                    "sms": true,
                    "voice": false
                },
                "cc_emails": [
                    "test1@twilio.com",
                    "test2@twilio.com"
                ],
                "date_created": "2017-03-28T20:06:39Z",
                "date_updated": "2017-03-28T20:06:39Z",
                "email": "test+hosted@twilio.com",
                "extension": "1234",
                "failure_reason": "",
                "friendly_name": "new friendly name",
                "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                "phone_number": "+14153608311",
                "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "signing_document_sid": "PX11111111111111111111111111111111",
                "status": "pending-loa",
                "unique_name": "new unique name",
                "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_attempts": 1,
                "verification_call_sids": [
                    "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                ],
                "verification_code": "8794",
                "verification_document_sid": null,
                "verification_type": "phone-call"
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders(sid="HRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.hosted_numbers.hosted_number_orders.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/HostedNumbers/HostedNumberOrders',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders?PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders?PageSize=50&Page=0"
                },
                "items": []
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders?PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders?PageSize=50&Page=0"
                },
                "items": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "address_sid": "AD11111111111111111111111111111111",
                        "call_delay": 15,
                        "capabilities": {
                            "sms": true,
                            "voice": false
                        },
                        "cc_emails": [
                            "aaa@twilio.com",
                            "bbb@twilio.com"
                        ],
                        "date_created": "2017-03-28T20:06:39Z",
                        "date_updated": "2017-03-28T20:06:39Z",
                        "email": "test@twilio.com",
                        "extension": "1234",
                        "failure_reason": "",
                        "friendly_name": "friendly_name",
                        "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                        "phone_number": "+14153608311",
                        "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "signing_document_sid": "PX11111111111111111111111111111111",
                        "status": "received",
                        "unique_name": "foobar",
                        "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "verification_attempts": 0,
                        "verification_call_sids": [
                            "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
                        ],
                        "verification_code": "8794",
                        "verification_document_sid": null,
                        "verification_type": "phone-call"
                    }
                ]
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.hosted_numbers.hosted_number_orders.create(phone_number="+15017122661", sms_capability=True)

        values = {'PhoneNumber': "+15017122661", 'SmsCapability': True, }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/HostedNumbers/HostedNumberOrders',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_sid": "AD11111111111111111111111111111111",
                "call_delay": 0,
                "capabilities": {
                    "sms": true,
                    "voice": false
                },
                "cc_emails": [],
                "date_created": "2017-03-28T20:06:39Z",
                "date_updated": "2017-03-28T20:06:39Z",
                "email": "test@twilio.com",
                "extension": null,
                "failure_reason": "",
                "friendly_name": null,
                "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                "phone_number": "+14153608311",
                "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "signing_document_sid": null,
                "status": "received",
                "unique_name": null,
                "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_attempts": 0,
                "verification_call_sids": null,
                "verification_code": null,
                "verification_document_sid": null,
                "verification_type": "phone-call"
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders.create(phone_number="+15017122661", sms_capability=True)

        self.assertIsNotNone(actual)

    def test_create_without_optional_loa_fields_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_sid": null,
                "call_delay": 0,
                "capabilities": {
                    "sms": true,
                    "voice": false
                },
                "cc_emails": [],
                "date_created": "2017-03-28T20:06:39Z",
                "date_updated": "2017-03-28T20:06:39Z",
                "email": null,
                "extension": null,
                "failure_reason": "",
                "friendly_name": null,
                "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                "phone_number": "+14153608311",
                "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "signing_document_sid": null,
                "status": "received",
                "unique_name": null,
                "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_attempts": 0,
                "verification_call_sids": null,
                "verification_code": null,
                "verification_document_sid": null,
                "verification_type": "phone-call"
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders.create(phone_number="+15017122661", sms_capability=True)

        self.assertIsNotNone(actual)

    def test_create_with_phone_bill_verification_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address_sid": null,
                "call_delay": 0,
                "capabilities": {
                    "sms": true,
                    "voice": false
                },
                "cc_emails": [],
                "date_created": "2017-03-28T20:06:39Z",
                "date_updated": "2017-03-28T20:06:39Z",
                "email": null,
                "extension": null,
                "failure_reason": "",
                "friendly_name": null,
                "incoming_phone_number_sid": "PN11111111111111111111111111111111",
                "phone_number": "+14153608311",
                "sid": "HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "signing_document_sid": null,
                "status": "received",
                "unique_name": null,
                "url": "https://preview.twilio.com/HostedNumbers/HostedNumberOrders/HRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_attempts": 0,
                "verification_call_sids": null,
                "verification_code": null,
                "verification_document_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "verification_type": "phone-bill"
            }
            '''
        ))

        actual = self.client.preview.hosted_numbers.hosted_number_orders.create(phone_number="+15017122661", sms_capability=True)

        self.assertIsNotNone(actual)
