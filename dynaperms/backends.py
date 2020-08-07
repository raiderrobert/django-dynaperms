from functools import lru_cache
from typing import Set, Iterable

from django.contrib.auth.backends import ModelBackend
from django.utils.functional import cached_property
from .utils import get_all_dynamic_perm_names, get_dynamic_perms


class DynamicBackend(ModelBackend):

    @cached_property
    def _get_all_dynamic_perms(self) -> Iterable[str]:
        return get_all_dynamic_perm_names()

    @lru_cache()
    def _get_user_dynamic_perms(self, user_obj) -> Set[str]:
        """
        Based on a user obj, check a bunch of functions and return them if they're valid
        """
        perms = set()

        for name, funcs in get_dynamic_perms().items():
            authorized = any([func(user_obj) for func in funcs])

            if authorized:
                perms.add(name)

        return perms

    def get_all_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous or obj is not None:
            return set()

        if user_obj.is_superuser:
            return self._get_all_dynamic_perms
        else:
            return self._get_user_dynamic_perms(user_obj)
