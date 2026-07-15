from rest_framework.throttling import UserRateThrottle

class RegisterThrottle(UserRateThrottle):
    rate="10/hour"

class LoginThrottle(UserRateThrottle):
    rate="12/hour"

class GeneralThrottle(UserRateThrottle):
    rate="20/hour"

class InAppThrottle(UserRateThrottle):
    rate="10/minute"