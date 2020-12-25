import pickle 
import pandas as pd 
import numpy as np 

class Xgb_regressor:
	def __init__(self):
		path_to_model = "../models/"
		self.model = pickle.load(open(path_to_model+"finalized_model_Xgb.sav",'rb'))


	def preprocessing(self,input_data):
		input_data = pd.DataFrame(input_data,index=[0])

		for column in ["codec" , "o_codec"]:
		    input_data[column] = input_data[column].astype('category')
		    input_data[column+"_cat"] = input_data[column].cat.codes
		    del input_data[column]
		del input_data['b_size']
		del input_data['id']
		input_data.fillna(0)

		return input_data

	def predict(self, input_data):
		return self.model.predict(input_data.values)

	def postprocessing(self, input_data):
		return { "Transcoding time": input_data, "status":"OK"}

	def compute_prediction(self,input_data):
		try:
			input_data = self.preprocessing(input_data)
			prediction = self.predict(input_data)[0]
			prediction = self.postprocessing(prediction)

		except Exception as e:
			print(str(e))
			return {"status" : "Error", "message": str(e)}

		return prediction





