from rest_framework import status
from rest_framework.exceptions import APIException


class CurrentUserSubscriptionExists(APIException):
    default_detail = (
        'User has already subscribed to this subscription and '
        'current subscription is not canceled'
    )
    status_code = status.HTTP_400_BAD_REQUEST


class PaymentException(APIException):
    default_detail = 'Error occurred while processing payment'
    status_code = status.HTTP_400_BAD_REQUEST

class WrongCashbackStatusException(APIException):
    default_detail = 'Wrong cashback status'
    status_code = status.HTTP_400_BAD_REQUEST
