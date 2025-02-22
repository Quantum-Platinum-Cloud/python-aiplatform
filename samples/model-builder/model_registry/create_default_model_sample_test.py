# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import create_default_model_sample

import test_constants as constants


def test_create_default_model_sample(mock_sdk_init, mock_init_model):
    # Create a model with alias 'default'.
    create_default_model_sample.create_default_model_sample(
        model_id=constants.MODEL_NAME,
        project=constants.PROJECT,
        location=constants.LOCATION,
    )

    # Check client initialization.
    mock_sdk_init.assert_called_with(
        project=constants.PROJECT, location=constants.LOCATION
    )

    # Check that the model was created.
    mock_init_model.assert_called_with(model_name=constants.MODEL_NAME)
