import streamlit as st
from clarifai.client.auth import create_stub
from clarifai.client.auth.helper import ClarifaiAuthHelper
from clarifai.client.user import User
from clarifai.modules.css import ClarifaiStreamlitCSS
from google.protobuf import json_format, timestamp_pb2

st.set_page_config(layout="wide")
ClarifaiStreamlitCSS.insert_default_css(st)

# This must be within the display() function.
auth = ClarifaiAuthHelper.from_streamlit(st)
stub = create_stub(auth)
userDataObject = auth.get_user_app_id_proto()

st.title("Simple example to list inputs")


IMAGE_FILE_LOCATION = 'LOCAL IMAGE PATH'
with open(IMAGE_FILE_LOCATION, "rb") as f:
    file_bytes = f.read()


prompt = "What is this?"
inference_params = dict(temperature=0.2, max_tokens=100)

model_prediction = Model("https://clarifai.com/victor_g/Victor_Img_class/models/victor-tl-classifier").predict(inputs = [Inputs.get_multimodal_input(input_id="", image_bytes = file_bytes, raw_text=prompt)], inference_params=inference_params)
print(model_prediction.outputs[0].data.text.raw)

  # Stream inputs from the app. list_inputs give list of dictionaries with inputs and its metadata .
  input_obj = User(user_id=userDataObject.user_id).app(app_id=userDataObject.app_id).inputs()
  all_inputs = input_obj.list_inputs()

  #Check for no of inputs in the app and compare it with no of inputs to be displayed.
  if len(all_inputs) < (mtotal):
    raise Exception(
        f"No of inputs is less than {mtotal}. Please add more inputs or reduce the inputs to be displayed !"
    )

  else:
    data = []
    #added "data_url" which gives the url of the input.
    for inp in range(mtotal):
      data.append({
          "id": all_inputs[inp].id,
          "data_url": all_inputs[inp].data.image.url,
          "status": all_inputs[inp].status.description,
          "created_at": timestamp_pb2.Timestamp.ToDatetime(all_inputs[inp].created_at),
          "modified_at": timestamp_pb2.Timestamp.ToDatetime(all_inputs[inp].modified_at),
          "metadata": json_format.MessageToDict(all_inputs[inp].data.metadata),
      })

  st.dataframe(data)
