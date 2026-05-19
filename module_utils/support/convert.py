### BEGIN: Imports
import typing as t
import datetime
from ...module_utils._app.methods import (
    pydash, _data,
)
### END: Imports
### BEGIN: ImportManager
### END: ImportManager

class Convert:
    @staticmethod
    def to_lofs(
        data: t.Mapping[str, t.Sequence[t.Any]], 
        defaults: t.Mapping = {},
        combines: t.Sequence | t.Mapping = [],
        combine_args: t.Mapping = {},
    ) -> list[dict]:
        data = dict(data)
        defaults = dict(defaults)
        combine_args = dict(combine_args)
        
        keys_ = data_keys(data)
        ret = []

        for item in range(0, len(data[keys_[0]])):
            new_item = defaults.copy()

            if len(combines) > 0 and data_has(combines, str(item)):
                new_item = data_combine(new_item, data_get(combines, str(item)), **combine_args)

            for key_ in keys_:
                data_set(new_item, key_, data[key_][item])

            ret.append(new_item)

        return ret