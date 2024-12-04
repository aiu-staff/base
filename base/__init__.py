import requests
import yaml

def find_config_by_project_name(project_name, cfg_list):
    for project in cfg_list:
        if project.get("project_name") == project_name:
            return project
    return None

