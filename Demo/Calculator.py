# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Demo.Calculator_forward import _Demo_CalculatorPrx_t

from Ice.Object import Object

from Ice.ObjectPrx import ObjectPrx
from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from collections.abc import Awaitable
    from collections.abc import Sequence


class CalculatorPrx(ObjectPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::Demo::Calculator``.
    """

    def divisor(self, n1: float, n2: float, context: dict[str, str] | None = None) -> float:
        return Calculator._op_divisor.invoke(self, ((n1, n2), context))

    def divisorAsync(self, n1: float, n2: float, context: dict[str, str] | None = None) -> Awaitable[float]:
        return Calculator._op_divisor.invokeAsync(self, ((n1, n2), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> CalculatorPrx | None:
        return checkedCast(CalculatorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[CalculatorPrx | None ]:
        return checkedCastAsync(CalculatorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> CalculatorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> CalculatorPrx | None:
        return uncheckedCast(CalculatorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Calculator"

IcePy.defineProxy("::Demo::Calculator", CalculatorPrx)

class Calculator(Object, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::Demo::Calculator``.
    """

    _ice_ids: Sequence[str] = ("::Demo::Calculator", "::Ice::Object", )
    _op_divisor: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Calculator"

    @abstractmethod
    def divisor(self, n1: float, n2: float, current: Current) -> float | Awaitable[float]:
        pass

Calculator._op_divisor = IcePy.Operation(
    "divisor",
    "divisor",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_double, False, 0), ((), IcePy._t_double, False, 0)),
    (),
    ((), IcePy._t_double, False, 0),
    ())

__all__ = ["Calculator", "CalculatorPrx", "_Demo_CalculatorPrx_t"]
