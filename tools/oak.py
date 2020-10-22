#!python3

############################################################
#   OAK (Of A Kind)
#-----------------------------------------------------------
#   A module of tools for type-checking.
############################################################

import sys as _sys
import collections as _cox
import collections.abc as _abc

from . import (
    twine as _twine,
    decor as _decor,
)

#-----------------------------------------------------------
#   DECORATORS
#-----------------------------------------------------------

_DLI_FUN_TYPE = _abc.Callable[..., bool]
_DLI_REPLACE_TYPE = _abc.Iterable[tuple[str, str, str, bool]]
_DLI_REPLACE_DEFAULT = (
    # (position: str, old_sub: str, new_sub: str, stop_after: bool)
    ("<", "is_", "isnt_", True),
    ("<", "", "not_", True),    # ⬅ Fallback option.
)

_DLI_METHODS = {
    "<": {
        "contains": _twine.contains_prefix,
        "replace": _twine.replace_prefix,
    },
    "*": {
        "contains": _twine.contains,
        "replace": _twine.replace,
    },
    ">": {
        "contains": _twine.contains_suffix,
        "replace": _twine.replace_suffix,
    },
}


@_decor.double_decor
def def_logical_inverse(
    fun: _DLI_FUN_TYPE,
    replace: _DLI_REPLACE_TYPE = _DLI_REPLACE_DEFAULT,
):
    """
    Decorator that defines the "notted" (logical inverse) of the decorated function.

    Optionally accepts `replace`, which is an iterable with items of the form:
    `(position: str, old_sub: str, new_sub: str, stop_after: bool)`.

    The replacements in `replace` are attempted in order, one at a time.

    The `position` parameter specifies where to replace `old_sub` with `new_sub`
    -- it can be `"<"` (prefix), `"*"` (anywhere), or `">"` (suffix).

    The `stop_after` parameter specifies whether the replacement process should
    stop after the given replacement has been _successfully_ performed.

    The default value for `replace` is:
    ```
    (
        ("<", "is_", "isnt_", True),
        ("<", "", "not_", True),
    )
    ```
    """

    # Define generic logical inverse function, `not_fun`.
    def not_fun(*args, **kwargs):
        return not fun(*args, **kwargs)

    # Get `fun`'s info.
    fun__module = _sys.modules[fun.__module__]
    fun__name: str = fun.__name__

    # Figure out the new name for `not_fun`.
    not_fun__name: str = ""
    for (position, old_slug, new_slug, stop_after) in replace:
        methods = _DLI_METHODS[position]
        if methods["contains"](fun__name, old_slug):
            not_fun__name = methods["replace"](fun__name, old_slug, new_slug)
            if stop_after:
                break

    # Define attributes of `not_fun`.
    not_fun.__name__: str = not_fun__name
    not_fun.__doc__: str = f"The logical inverse of `{fun__module}.{fun__name}`."

    # Add `not_fun` to `fun`'s module.
    setattr(fun__module, not_fun__name, not_fun)

    # And we're done!
    return fun


#-----------------------------------------------------------
#   TYPE-CHECKING FUNCTIONS
#-----------------------------------------------------------


@def_logical_inverse
def is_of(x, kinds) -> bool:
    return isinstance(x, kinds)


@def_logical_inverse
def is_none(x) -> bool:
    return x is None


#---------------------------------------
#   from `builtins`
#---------------------------------------


# builtins.bool
@def_logical_inverse
def is_bool(x) -> bool:
    return is_of(x, bool)


# builtins.bytearray
@def_logical_inverse
def is_bytearray(x) -> bool:
    return is_of(x, bytearray)


# builtins.bytes
@def_logical_inverse
def is_bytes(x) -> bool:
    return is_of(x, bytes)


# builtins.complex
@def_logical_inverse
def is_complex(x) -> bool:
    return is_of(x, complex)


# builtins.dict
@def_logical_inverse
def is_dict(x) -> bool:
    return is_of(x, dict)


# builtins.float
@def_logical_inverse
def is_float(x) -> bool:
    return is_of(x, float)


# builtins.frozenset
@def_logical_inverse
def is_frozenset(x) -> bool:
    return is_of(x, frozenset)


# builtins.int
@def_logical_inverse
def is_int(x) -> bool:
    return is_of(x, int)


# builtins.list
@def_logical_inverse
def is_list(x) -> bool:
    return is_of(x, list)


# builtins.property
@def_logical_inverse
def is_property(x) -> bool:
    return is_of(x, property)


# builtins.range
@def_logical_inverse
def is_range(x) -> bool:
    return is_of(x, range)


# builtins.set
@def_logical_inverse
def is_set(x) -> bool:
    return is_of(x, set)


# builtins.slice
@def_logical_inverse
def is_slice(x) -> bool:
    return is_of(x, slice)


# builtins.str
@def_logical_inverse
def is_str(x) -> bool:
    return is_of(x, str)


# builtins.tuple
@def_logical_inverse
def is_tuple(x) -> bool:
    return is_of(x, tuple)


# builtins.type
@def_logical_inverse
def is_type(x) -> bool:
    return is_of(x, type) or str(type(x)).startswith("<class 'typing.")


#---------------------------------------
#   from `collections`
#---------------------------------------


# collections.deque
@def_logical_inverse
def is_Deque(x) -> bool:
    return is_of(x, _cox.deque)


# collections.ChainMap
@def_logical_inverse
def is_ChainMap(x) -> bool:
    return is_of(x, _cox.ChainMap)


# collections.Counter
@def_logical_inverse
def is_Counter(x) -> bool:
    return is_of(x, _cox.Counter)


# collections.OrderedDict
@def_logical_inverse
def is_OrderedDict(x) -> bool:
    return is_of(x, _cox.OrderedDict)


# collections.defaultdict
@def_logical_inverse
def is_DefaultDict(x) -> bool:
    return is_of(x, _cox.defaultdict)


# collections.UserDict
@def_logical_inverse
def is_UserDict(x) -> bool:
    return is_of(x, _cox.UserDict)


# collections.UserList
@def_logical_inverse
def is_UserList(x) -> bool:
    return is_of(x, _cox.UserList)


# collections.UserString
@def_logical_inverse
def is_UserString(x) -> bool:
    return is_of(x, _cox.UserString)


#---------------------------------------
#   from `collections.abc`
#---------------------------------------


# collections.abc.Container
@def_logical_inverse
def is_Container(x) -> bool:
    return is_of(x, _abc.Container)


# collections.abc.Hashable
@def_logical_inverse
def is_Hashable(x) -> bool:
    return is_of(x, _abc.Hashable)


# collections.abc.Iterable
@def_logical_inverse
def is_Iterable(x) -> bool:
    return is_of(x, _abc.Iterable)


# collections.abc.Iterator
@def_logical_inverse
def is_Iterator(x) -> bool:
    return is_of(x, _abc.Iterator)


# collections.abc.Reversible
@def_logical_inverse
def is_Reversible(x) -> bool:
    return is_of(x, _abc.Reversible)


# collections.abc.Generator
@def_logical_inverse
def is_Generator(x) -> bool:
    return is_of(x, _abc.Generator)


# collections.abc.Sized
@def_logical_inverse
def is_Sized(x) -> bool:
    return is_of(x, _abc.Sized)


# collections.abc.Callable
@def_logical_inverse
def is_Callable(x) -> bool:
    return is_of(x, _abc.Callable)


# collections.abc.Collection
@def_logical_inverse
def is_Collection(x) -> bool:
    return is_of(x, _abc.Collection)


# collections.abc.Sequence
@def_logical_inverse
def is_Sequence(x) -> bool:
    return is_of(x, _abc.Sequence)


# collections.abc.MutableSequence
@def_logical_inverse
def is_MutableSequence(x) -> bool:
    return is_of(x, _abc.MutableSequence)


# collections.abc.ByteString
@def_logical_inverse
def is_ByteString(x) -> bool:
    return is_of(x, _abc.ByteString)


# collections.abc.Set
@def_logical_inverse
def is_Set(x) -> bool:
    return is_of(x, _abc.Set)


# collections.abc.MutableSet
@def_logical_inverse
def is_MutableSet(x) -> bool:
    return is_of(x, _abc.MutableSet)


# collections.abc.Mapping
@def_logical_inverse
def is_Mapping(x) -> bool:
    return is_of(x, _abc.Mapping)


# collections.abc.MutableMapping
@def_logical_inverse
def is_MutableMapping(x) -> bool:
    return is_of(x, _abc.MutableMapping)


# collections.abc.MappingView
@def_logical_inverse
def is_MappingView(x) -> bool:
    return is_of(x, _abc.MappingView)


# collections.abc.ItemsView
@def_logical_inverse
def is_ItemsView(x) -> bool:
    return is_of(x, _abc.ItemsView)


# collections.abc.KeysView
@def_logical_inverse
def is_KeysView(x) -> bool:
    return is_of(x, _abc.KeysView)


# collections.abc.ValuesView
@def_logical_inverse
def is_ValuesView(x) -> bool:
    return is_of(x, _abc.ValuesView)


# collections.abc.Awaitable
@def_logical_inverse
def is_Awaitable(x) -> bool:
    return is_of(x, _abc.Awaitable)


# collections.abc.Coroutine
@def_logical_inverse
def is_Coroutine(x) -> bool:
    return is_of(x, _abc.Coroutine)


# collections.abc.AsyncIterable
@def_logical_inverse
def is_AsyncIterable(x) -> bool:
    return is_of(x, _abc.AsyncIterable)


# collections.abc.AsyncIterator
@def_logical_inverse
def is_AsyncIterator(x) -> bool:
    return is_of(x, _abc.AsyncIterator)


# collections.abc.AsyncGenerator
@def_logical_inverse
def is_AsyncGenerator(x) -> bool:
    return is_of(x, _abc.AsyncGenerator)
