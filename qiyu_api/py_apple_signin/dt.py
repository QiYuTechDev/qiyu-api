from typing import Literal, Union, Optional

import jwt
from pydantic import BaseModel, Field

__all__ = [
    "AppleConfig",
    "AppleSignInDecoded",
    "AppleSignInFailureRet",
    "AppleSignInSuccessRet",
]


class AppleConfig(BaseModel):
    """
    苹果登陆的配置项目
    """

    key_id: str = Field(
        ...,
        title="the private key id",
        description="[find on apple developer portal -> keys -> key-detail page]",
    )
    private_key: str = Field(
        ...,
        title="the private key content [.p8 file]",
        description="downloaded when the key generate,you can regenerate the key on apple developer portal -> keys",
    )
    team_id: str = Field(
        ..., title="the apple team id", description="view on apple developer portal"
    )
    bundle_id: str = Field(..., title="the app's bundle id")


class AppleSignInFailureRet(BaseModel):
    error: Optional[str] = Field(None, title="请求失败的原因")


class AppleSignInSuccessRet(BaseModel):
    """
    doc: https://developer.apple.com/documentation/sign_in_with_apple/tokenresponse
    """

    access_token: str = Field(
        ...,
        title="A token used to access allowed data",
        description="Currently, no data set has been defined for access.(Reserved for future use)",
    )
    expires_in: int = Field(
        ..., title="The amount of time, in seconds, before the access token expires."
    )
    id_token: str = Field(
        ..., title="A JSON Web Token that contains the user’s identity information."
    )
    refresh_token: str = Field(
        ...,
        title="The refresh token used to regenerate new access tokens",
        description="Store this token securely on your server.",
    )
    token_type: str = Field(
        ..., title="The type of access token.", description="It will always be bearer."
    )

    @property
    def decoded_id_token(self) -> Optional["AppleSignInDecoded"]:
        decoded = jwt.decode(self.id_token, "", verify=False)
        if isinstance(decoded, dict):
            return AppleSignInDecoded(**decoded)
        else:
            return None


class AppleSignInDecoded(BaseModel):
    """
    doc:
    https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple
    """

    iss: str = Field(
        ...,
        title="",
        description="""
    The issuer registered claim identifies the principal
    that issued the identity token.

    Since Apple generates the token,
    the value is https://appleid.apple.com.
    """,
    )

    sub: str = Field(
        ...,
        title="",
        description="""
    The subject registered claim identifies the principal
    that is the subject of the identity token.

    Since this token is meant for your application,
    the value is the unique identifier for the user.
    """,
    )

    aud: str = Field(
        ...,
        title="",
        description="""
    The audience registered claim identifies the recipient
    for which the identity token is intended.

    Since the token is meant for your application,
    the value is the client_id from your developer account.
    """,
    )

    iat: str = Field(
        ...,
        title="iat",
        description="""
    The issued at registered claim indicates the time
    at which Apple issued the identity token,

    in terms of the number of seconds since Epoch, in UTC.
    """,
    )

    exp: str = Field(
        ...,
        title="The expiration time",
        description="""
The expiration time registered identifies the time on
or after which the identity token will expire,
in terms of number of seconds since Epoch, in UTC.

The value must be greater than the
current date/time when verifying the token.
    """,
    )

    email: str = Field(
        ...,
        title="A String value representing the user’s email address.",
        description="""
    The email address will be either
    the user’s real email address or the proxy address,

    depending on their status private email relay service.
                       """,
    )

    email_verified: Union[Literal["true"], Literal["false"], bool] = Field(
        ...,
        title="A String or Boolean value that indicates whether the service has verified the email.",
        description="""
The value of this claim is always true, because the servers
 only return verified email addresses.
The value can either be a String (”true”) or a Boolean (true).""",
    )

    is_private_email: Union[Literal["true"], Literal["false"], bool] = Field(
        ...,
        title="A String or Boolean value that indicates whether the email shared by the user is the proxy address",
        description="""
    The value can either be a String (”true” or “false”)
    or a Boolean (true or false).
""",
    )

    real_user_status: Optional[int] = Field(
        None,
        title="An Integer value that indicates whether the user appears to be a real person.",
        description="""\
Use the value of this claim to mitigate fraud.
The possible values are:
0 (or Unsupported). 1 (or Unknown), 2 (or LikelyReal).
For more information, see ASUserDetectionStatus.
This claim is present only on iOS 14 and later,
macOS 11 and later, watchOS 7 and later, tvOS 14 and later;
the claim is not present or supported for web-based apps.""",
    )

    nonce: Optional[str] = Field(
        None,
        title="A String value used to associate a client session and the identity token",
        description="""\
This value is used to mitigate replay attacks and is present
only if passed during the authorization request.""",
    )

    nonce_supported: Optional[bool] = Field(
        None,
        title="A Boolean value that indicates whether the transaction is on a nonce-supported platform.",
        description="""\
If you sent a nonce in the authorization request
but do not see the nonce claim in the identity token,
check this claim to determine how to proceed.

If this claim returns true,
you should tream nonce as mandatory and fail the transaction;
otherwise, you can proceed treating the nonce as options.""",
    )
