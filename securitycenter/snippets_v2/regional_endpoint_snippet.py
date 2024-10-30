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

# [START securitycenter_regional_endpoint_list_findings]
def rep_list_finding(parent, endpoint) -> int:
    """
    lists all findings for a parent
    Args:
        parent: Parent resource for which findings to be listed. Must be in one of the following formats:
                "organizations/{organization_id}/sources/{sources}/locations/{location}"
                "projects/{project_id}/sources/{sources}/locations/{location}"
                "folders/{folder_id}/sources/{sources}/locations/{location}"
        endpoint: Endpoint for this request. For example "securitycenter.googleapis.com", "securitycenter.me-central2.rep.googleapis.com"
    Returns:
        int: return the count of all findings for a source
    """
    from google.cloud import securitycenter_v2 as securitycenter
    from google.api_core.client_options import ClientOptions
    # Override endpoint and create a client.
    options = ClientOptions(api_endpoint=endpoint)
    client = securitycenter.SecurityCenterClient(client_options=options)

    finding_result_iterator = client.list_findings(request={"parent": parent})
    for count, finding_result in enumerate(finding_result_iterator):
        print(
            "{}: name: {} resource: {}".format(
                count, finding_result.finding.name, finding_result.finding.resource_name
            )
        )
    return count

# [END securitycenter_regional_endpoint_list_findings]
