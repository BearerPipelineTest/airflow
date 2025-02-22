# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from typing import Dict, List, Union

KUBERNETES_CLUSTER_COMMANDS: Dict[str, Union[str, List[str]]] = {
    "name": "K8S cluster management commands",
    "commands": [
        "setup-env",
        "create-cluster",
        "build-k8s-image",
        "upload-k8s-image",
        "configure-cluster",
        "deploy-airflow",
        "delete-cluster",
    ],
}
KUBERNETES_INSPECTION_COMMANDS: Dict[str, Union[str, List[str]]] = {
    "name": "K8S inspection commands",
    "commands": ["status", "logs"],
}

KUBERNETES_TESTING_COMMANDS: Dict[str, Union[str, List[str]]] = {
    "name": "K8S testing commands",
    "commands": ["tests", "shell", "k9s", "logs"],
}
KUBERNETES_PARAMETERS: Dict[str, List[Dict[str, Union[str, List[str]]]]] = {
    "breeze k8s setup-env": [
        {
            "name": "K8S setup flags",
            "options": ["--force"],
        }
    ],
    "breeze k8s create-cluster": [
        {
            "name": "K8S cluster creation flags",
            "options": [
                "--force",
                "--forwarded-port-number",
                "--api-server-port",
                "--python",
                "--kubernetes-version",
            ],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s build-k8s-image": [
        {
            "name": "Build image flags",
            "options": [
                "--python",
                "--rebuild-base-image",
                "--image-tag",
            ],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s upload-k8s-image": [
        {
            "name": "Upload image flags",
            "options": [
                "--python",
                "--kubernetes-version",
                "--image-tag",
            ],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s configure-k8s-cluster": [
        {
            "name": "Configure cluster flags",
            "options": [
                "--python",
                "--kubernetes-version",
            ],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s deploy-airflow": [
        {
            "name": "Airflow deploy flags",
            "options": [
                "--python",
                "--kubernetes-version",
                "--executor",
                "--upgrade",
                "--wait-time-in-seconds",
            ],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s delete-cluster": [
        {
            "name": "K8S cluster delete flags",
            "options": ["--python", "--kubernetes-version"],
        },
        {
            "name": "K8S multi-cluster flags",
            "options": ["--all"],
        },
    ],
    "breeze k8s status": [
        {
            "name": "K8S cluster status flags",
            "options": ["--python", "--kubernetes-version", "--wait-time-in-seconds"],
        },
        {
            "name": "K8S multi-cluster flags",
            "options": ["--all"],
        },
    ],
    "breeze k8s logs": [
        {
            "name": "K8S logs flags",
            "options": ["--python", "--kubernetes-version"],
        },
        {
            "name": "K8S multi-cluster flags",
            "options": ["--all"],
        },
    ],
    "breeze k8s tests": [
        {
            "name": "K8S tests flags",
            "options": ["--python", "--kubernetes-version", "--executor", "--force-venv-setup"],
        },
        {
            "name": "Parallel options",
            "options": [
                "--run-in-parallel",
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
            ],
        },
    ],
    "breeze k8s run-complete-tests": [
        {
            "name": "K8S setup & tests flags",
            "options": [
                "--parallelism",
                "--python-versions",
                "--kubernetes-versions",
                "--include-success-outputs",
                "--executor",
                "--force-venv-setup",
                "--image-tag",
                "--wait-time-in-seconds",
                "--skip-rebuilding-base-image",
                "--skip-recreating-namespaces",
                "--skip-deploying-test-resources",
                "--skip-recreating-clusters",
                "--skip-deploying-airflow",
                "--skip-deleting-clusters",
            ],
        }
    ],
    "breeze k8s k9s": [
        {
            "name": "K8S k9s flags",
            "options": [
                "--python",
                "--kubernetes-version",
            ],
        }
    ],
    "breeze k8s shell": [
        {
            "name": "K8S shell flags",
            "options": ["--python", "--kubernetes-version", "--executor", "--force-venv-setup"],
        }
    ],
}
