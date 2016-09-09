#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

import getpass
from applicationinsights import TelemetryClient
from applicationinsights.exceptions import enable
from azure.cli.core import __version__ as core_version

client = {}

def init_telemetry():
    try:
        instrumentation_key = '02b91c82-6729-4241-befc-e6d02ca4fbba'

        global client #pylint: disable=global-statement
        client = TelemetryClient(instrumentation_key)

        client.context.application.id = 'Azure CLI'
        client.context.application.ver = core_version
        client.context.user.id = hash(getpass.getuser())

        enable(instrumentation_key)
    except Exception: #pylint: disable=broad-except
        # Never fail the command because of telemetry
        pass

def user_agrees_to_telemetry():
    # TODO: agreement, needs to take Y/N from the command line
    # and needs a "skip" param to not show (for scripts)
    return True

def telemetry_flush():
    try:
        client.flush()
    except Exception: #pylint: disable=broad-except
        # Never fail the command because of telemetry
        pass