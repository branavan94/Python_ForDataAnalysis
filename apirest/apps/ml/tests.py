from django.test import TestCase
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.utime_regressor.Xgb_regressor import Xgb_regressor

class MLTests(TestCase):
	def test_rf_algorithm(self):
		input_data = {"id": "04t6-jw9czg",
                    "duration": 130.35667,
                    "codec": "mpeg4",
                    "width": 176,
                    "height": 144,
                    "bitrate": 54590,
                    "framerate": 12.0,
                    "i": 27,
                    "p": 1537,
                    "b": 0,
                    "frames": 1564,
                    "i_size": 64483,
                    "p_size": 825054,
                    "b_size": 0,
                    "size": 889537,
                    "o_codec": "mpeg4",
                    "o_bitrate": 56000,
                    "o_framerate": 12.0,
                    "o_width": 176,
                    "o_height": 144,
                    "umem": 22508}

		my_alg = Xgb_regressor()
		response = my_alg.compute_prediction(input_data)
		self.assertEqual("OK",response['status'])
	def test_registry(self):
		registry = MLRegistry()
		self.assertEqual(len(registry.endpoints),0)
		endpoint_name = "utime_regressor"
		algorithm_object = Xgb_regressor()
		algorithm_name = "Xgb Regressor"
		algorithm_status = "production"
		algorithm_version = "0.0.1"
		algorithm_owner = "Brana"
		algorithm_description = "Xgb Regressor with some preprocessing"
		algorithm_code = inspect.getsource(Xgb_regressor)

		registry.add_algorithm(endpoint_name,algorithm_object, algorithm_name, algorithm_status,
								 algorithm_version, algorithm_owner,
								algorithm_description, algorithm_code)

		self.assertEqual(len(registry.endpoints),1)

