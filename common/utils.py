from importlib import import_module

from django.utils.module_loading import module_has_submodule
from ninja_extra.controllers.registry import ControllerRegistry


def auto_discover_controllers(api) -> None:
    from django.apps import apps

    installed_apps = [
        v for k, v in apps.app_configs.items() if not v.name.startswith("django.")
    ]
    possible_module_name = ["api", "controllers", "views"]

    for app_module in installed_apps:
        try:
            app_module_ = import_module(app_module.name)
            for module in possible_module_name:
                if module_has_submodule(app_module_, module):
                    mod_path = "%s.%s" % (app_module.name, module)
                    import_module(mod_path)
            api.register_controllers(*ControllerRegistry.get_controllers().values())
        except ImportError as ex:  # pragma: no cover
            raise ex
