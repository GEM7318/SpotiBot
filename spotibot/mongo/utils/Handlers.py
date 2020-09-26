
import json
import re


def object_handler(object_to_search: object, key_to_find: str, default=None):
    """Getter utility function to handle attribute extraction from base
    dictionaries as well as SpotiBot and/or Mongo objects.

    Args:
        object_to_search: Object within which to find the attribute value
        key_to_find: Name of the attribute to find
        default: Value to return attribute doesn't exist within object

    """
    if isinstance(object_to_search, dict):
        return object_to_search.get(key_to_find, default)

    else:
        try:
            return vars(object_to_search).get(key_to_find)
        except:
            return default


def get_serializable(attr_to_jsonify):
    """Attempts to run serialization method on an attribute or a list of
    attributes.

    Args:
        attr_to_jsonify: Attribute to attempt to serialize

    Returns:
        Either the serializable form of the attribute or its original form
        if to_dict() method cannot be called on it
    """
    if isinstance(attr_to_jsonify, list):

        try:
            # v_json = [val.to_dict() for val in attr_to_jsonify]
            return [val.to_dict() for val in attr_to_jsonify]
        except:
            return attr_to_jsonify
            # v_json = [val for val in attr_to_jsonify]

    else:
        try:
            # v_json = attr_to_jsonify.to_dict()
            return attr_to_jsonify.to_dict()
        except:
            # v_json = attr_to_jsonify
            return attr_to_jsonify

    # return v_json


# def type_to_str(field, to_replace):
#     stringified = str(field)
#
#     matches = re.findall(r"class\s'(\w+)'", stringified)
#
#     if matches:
#         field = matches[0]
#         for old, new in to_replace.items():
#             field = field.replace(old, new)
#
#     return field


# def is_iterable(val):
#     if isinstance(val, str):
#         return False
#     else:
#         try:
#             iter(val)
#             return True
#         except:
#             return False


# def has_items(v):
#     try:
#         for k, v in vars(v).items():
#             pass
#         return True
#     except:
#         return False


def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except:
        return False


# def is_serializable(list_of_dicts: list):
#     assert isinstance(list_of_dicts, list), f"Argument is not of type <'list>'"
#     cnt_ser = [1 if is_jsonable(v) else 0 for v in list_of_dicts]
#     return True if sum(cnt_ser) == len(list_of_dicts) else False