from __future__ import annotations
### BEGIN: Imports
import typing as t
import pydash
### END: Imports
### BEGIN: ImportManager
### END: ImportManager

class FilterModule(object):
    def filters(self):
        from ..module_utils.support.convert import Convert
        
        return {
            # 'to_path_segments': to_path_segments,
            # 'to_lofs': Convert.to_lofs,
        }