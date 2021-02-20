import json
import os
from dataclasses import dataclass

from .gen import AliSmsSync, SendSmsQueryParams, AliSmsBase


@dataclass
class TestConfig(object):
    access_key: str
    access_secret: str
    sign_name: str
    template_code: str
    mobile: str


def load_config() -> TestConfig:
    config_file = os.path.join(os.path.dirname(__file__), "..", "config.json")
    assert os.path.exists(config_file)

    with open(config_file) as fp:
        d = json.load(fp)
        return TestConfig(**d)


def test_str_signature():
    result = AliSmsBase.compute_str_signature("source", "secret")
    assert result == "Jv4yi8SobFhg5t1C7nWLbhBSFZQ="

    result = AliSmsBase.compute_str_signature("中文unicode", "secret")
    assert result == "szlfHs3WVaO/HgY3Cg7/uyXDaRw="


def test_send_sms():
    c = load_config()

    sms = AliSmsSync(access_key=c.access_key, access_secret=c.access_secret)
    query = SendSmsQueryParams(
        PhoneNumbers=c.mobile,
        SignName=c.sign_name,
        TemplateCode=c.template_code,
        TemplateParam=json.dumps({"code": "238672"}, separators=(",", ":")),
    )
    ret = sms.send_sms(query)
    assert ret is not None
    assert ret.Code == "OK"
