#!/usr/bin/env python
#
# Copyright 2024 Google LLC
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
import os
import pytest
import regional_endpoint_snippet

@pytest.fixture(scope="module")
def parent():
    return f"{(os.environ['DRZ_SA_ORGANIZATION'])}/sources/-/locations/sa"

def endpoint():
    return "securitycenter.me-central2.rep.googleapis.com"

def test_rep_list_finding():
    count = regional_endpoint_snippet.rep_list_finding(parent, endpoint)
    assert count > 0