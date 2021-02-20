from dataclasses import dataclass
from typing import Literal, Union, Optional

import jwt
from dataclasses_json import DataClassJsonMixin

__all__ = [
    "AppleConfig",
    "AppleSignInDecoded",
    "AppleSignInFailureRet",
    "AppleSignInSuccessRet",
]


@dataclass
class AppleConfig(DataClassJsonMixin):
    """
    苹果登陆的配置项目
    """

    key_id: str
    """
    the private key id
    [find on apple developer portal -> keys -> key-detail page]
    """

    private_key: str
    """
    the private key content [.p8 file]
    [downloaded when the key generate,
    you can regenerate the key on apple developer portal -> keys]
    """

    team_id: str
    """
    the apple team id [view on apple developer portal]
    """

    bundle_id: str
    """
    the app's bundle id
    """


@dataclass
class AppleSignInFailureRet(DataClassJsonMixin):
    error: str = None
    """
    如果请求失败的原因
    """


@dataclass
class AppleSignInSuccessRet(DataClassJsonMixin):
    """
    doc:
    https://developer.apple.com/documentation/sign_in_with_apple/tokenresponse
    """

    access_token: str
    """
    (Reserved for future use) A token used to access allowed data.
    Currently, no data set has been defined for access.
    """

    expires_in: int
    """
    The amount of time, in seconds, before the access token expires.
    """

    id_token: str
    """
    A JSON Web Token that contains the user’s identity information.
    """

    refresh_token: str
    """
    The refresh token used to regenerate new access tokens.
    Store this token securely on your server.
    """

    token_type: str
    """
    The type of access token. It will always be bearer.
    """

    @property
    def decoded_id_token(self) -> Optional["AppleSignInDecoded"]:
        decoded = jwt.decode(self.id_token, "", verify=False)
        if isinstance(decoded, dict):
            return AppleSignInDecoded.from_dict(decoded)
        else:
            return None


@dataclass
class AppleSignInDecoded(DataClassJsonMixin):
    """
    doc:
    https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple
    """

    iss: str
    """
    The issuer registered claim identifies the principal
    that issued the identity token.

    Since Apple generates the token,
    the value is https://appleid.apple.com.
    """

    sub: str
    """
    The subject registered claim identifies the principal
    that is the subject of the identity token.

    Since this token is meant for your application,
    the value is the unique identifier for the user.
    """

    aud: str
    """
    The audience registered claim identifies the recipient
    for which the identity token is intended.

    Since the token is meant for your application,
    the value is the client_id from your developer account.
    """

    iat: str
    """
    The issued at registered claim indicates the time
    at which Apple issued the identity token,

    in terms of the number of seconds since Epoch, in UTC.
    """

    exp: str
    """
    The expiration time registered identifies the time on
    or after which the identity token will expire,
    in terms of number of seconds since Epoch, in UTC.

    The value must be greater than the
    current date/time when verifying the token.
    """

    email: str
    """
    A String value representing the user’s email address.
    The email address will be either
    the user’s real email address or the proxy address,

    depending on their status private email relay service.
    """

    email_verified: Union[Literal["true"], Literal["false"]]
    """
    A String or Boolean value that indicates whether the service
    has verified the email.
    The value of this claim is always true, because the servers
     only return verified email addresses.
    The value can either be a String (”true”) or a Boolean (true).
    """

    is_private_email: Union[Literal["true"], Literal["false"]]
    """
    A String or Boolean value that indicates whether the email
    shared by the user is the proxy address.
    The value can either be a String (”true” or “false”)
    or a Boolean (true or false).
    """

    real_user_status: Optional[int] = None
    """
    An Integer value that indicates
    whether the user appears to be a real person.
    Use the value of this claim to mitigate fraud.
    The possible values are:
    0 (or Unsupported). 1 (or Unknown), 2 (or LikelyReal).
    For more information, see ASUserDetectionStatus.
    This claim is present only on iOS 14 and later,
    macOS 11 and later, watchOS 7 and later, tvOS 14 and later;
    the claim is not present or supported for web-based apps.
    """

    nonce: Optional[str] = None
    """
    A String value used to associate a client session and the identity token.
    This value is used to mitigate replay attacks and is present
    only if passed during the authorization request.
    """

    nonce_supported: Optional[bool] = None
    """
    A Boolean value that indicates whether the transaction
    is on a nonce-supported platform.

    If you sent a nonce in the authorization request
    but do not see the nonce claim in the identity token,
    check this claim to determine how to proceed.

    If this claim returns true,
    you should tream nonce as mandatory and fail the transaction;
    otherwise, you can proceed treating the nonce as options.
    """
