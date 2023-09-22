# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class AuthenticateUserByName(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'username': 'str',
        'pw': 'str'
    }

    attribute_map = {
        'username': 'Username',
        'pw': 'Pw'
    }

    def __init__(self, username=None, pw=None):  # noqa: E501
        """AuthenticateUserByName - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._pw = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if pw is not None:
            self.pw = pw

    @property
    def username(self):
        """Gets the username of this AuthenticateUserByName.  # noqa: E501


        :return: The username of this AuthenticateUserByName.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AuthenticateUserByName.


        :param username: The username of this AuthenticateUserByName.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def pw(self):
        """Gets the pw of this AuthenticateUserByName.  # noqa: E501


        :return: The pw of this AuthenticateUserByName.  # noqa: E501
        :rtype: str
        """
        return self._pw

    @pw.setter
    def pw(self, pw):
        """Sets the pw of this AuthenticateUserByName.


        :param pw: The pw of this AuthenticateUserByName.  # noqa: E501
        :type: str
        """

        self._pw = pw

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AuthenticateUserByName, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthenticateUserByName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other