#!/usr/bin/python3

import json
from subprocess import Popen, PIPE
from logger import dump_stderr, log_filename


class Azure(object):
    def get_group_id(resource_group: str):
        if resource_group is None:
            raise Exception("Expected an argument, resource_group.")

        p_cmd = ["az", "group", "show"]

        p_cmd.extend(["--resource-group", resource_group])
        p_cmd.extend(["--output", "json"])

        p = Popen(p_cmd, stdout=PIPE, stderr=PIPE)
        p_stdout, p_stderr = p.communicate()

        p_output = json.loads(p_stdout.decode(encoding="UTF-8"))

        az_group_id = p_output["id"]

        if az_group_id is None:
            raise NameError("No id.")

        return az_group_id

    def create_sp_rbac(resource_group: str, role: str):
        if resource_group is None:
            raise Exception("Expected an argument, resource_group.")

        if role is None:
            raise Exception("Expected an argument, role.")

        p_cmd = ["az", "ad", "sp", "create-for-rbac"]

        p_cmd.extend([
            "--scope", resource_group,
            "--role", role,
            "--sdk-auth"
        ])

        p = Popen(p_cmd, stdout=PIPE, stderr=PIPE)
        p_stdout, p_stderr = p.communicate()
        p_ecode = p.returncode

        if p_ecode != 0:
            dump_stderr(p_stderr)
            raise Exception(
                f"Command exited with code {p_ecode}. See {log_filename} for details.")

        return json.loads(p_stdout.decode(encoding="UTF-8"))

    def get_acr_id(registry: str):
        p_cmd = ["az", "acr", "show"]

        p_cmd.extend([
            "--name", registry,
            "--output", "json"
        ])

        p = Popen(p_cmd, stdout=PIPE, stderr=PIPE)
        p_stdout, p_stderr = p.communicate()

        p_output = json.loads(p_stdout.decode(encoding="UTF-8"))

        az_acr_id = p_output["id"]

        if az_acr_id is None:
            raise NameError("No id.")

        return az_acr_id

    def create_role(client_id: str, registry_id: str, role: str):
        p_cmd = ["az", "role", "assignment", "create"]

        p_cmd.extend([
            "--assignee", client_id,
            "--scope", registry_id,
            "--role", role
        ])

        p = Popen(p_cmd, stdout=PIPE, stderr=PIPE)
        p_stdout, p_stderr = p.communicate()
        p_ecode = p.returncode

        if p_ecode != 0:
            dump_stderr(p_stderr)
            raise Exception(
                f"Command exited with code {p_ecode}. See {log_filename} for details.")
