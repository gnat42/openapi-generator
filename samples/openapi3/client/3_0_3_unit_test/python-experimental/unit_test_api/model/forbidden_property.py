# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class ForbiddenProperty(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class foo(
        schemas.ComposedSchema,
    ):
    
    
        class MetaOapg:
            not_schema = schemas.AnyTypeSchema
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'foo':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
        foo: typing.Union[foo, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Type[schemas.Schema],
    ) -> 'ForbiddenProperty':
        return super().__new__(
            cls,
            *args,
            foo=foo,
            _configuration=_configuration,
            **kwargs,
        )
