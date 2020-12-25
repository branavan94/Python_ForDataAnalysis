"""
WSGI config for apirest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apirest.settings')

application = get_wsgi_application()


#ML Registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.utime_regressor.Xgb_regressor import Xgb_regressor


try:
	registry = MLRegistry()
	xgb = Xgb_regressor()

	registry.add_algorithm(endpoint_name = "utime_regressor",
		algorithm_object = Xgb_regressor(),
		algorithm_name = "Xgb Regressor",
		algorithm_status = "production",
		algorithm_version = "0.0.1",
		owner = "Brana",
		algorithm_description = "Xgb Regressor with some preprocessing",
		algorithm_code = inspect.getsource(Xgb_regressor))

except Exception as e:
	print("Exception while loading the algorithm to the registry", str(e))
