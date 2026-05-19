from __future__ import annotations
### BEGIN: Imports
import typing as t
import pydash
### END: Imports
### BEGIN: ImportManager
### END: ImportManager

def combine(
    *args,
    recursive: bool = False,
    list_merge: t.Literal['append', 'append_rp', 'keep', 'prepend', 'prepend_rp', 'replace'] = 'replace',
    reverse: bool = False,
) -> dict:
    from ansible.plugins.filter.core import combine
    
    if reverse:
        args = list(reversed(args))
    
    return combine(*args, recursive=recursive, list_merge=list_merge)

class FilterModule(object):
    def filters(self):
        
        return {
            'combine': combine,
        }