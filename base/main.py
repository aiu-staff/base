from dotenv import load_dotenv
import os
from deepmerge import always_merger

from .github import load_yaml_from_private_github
from . import find_config_by_project_name
if __name__ == "__main__":
    GITHUB_API_KEY = os.getenv("GIT_API_KEY")

    CFG_PROJECT_INFO_URL = "https://github.com/aiu-interns-karate-groza-newbies-ph/karate-do-groza-newbies/blob/main/project_info.yaml"
    
    
    test = load_yaml_from_private_github(CFG_PROJECT_INFO_URL, GITHUB_API_KEY)


    CFG = [
    {"project_name": "CDTI",

      "base_dir": "/content/drive/MyDrive/uii/teamleads/Химяк Павел/2024.09.03_DTCI_newbies/журналы встречь",
      "project_info_url" : "https://github.com/NeuronsUII/CDTI_OCR_newbies/blob/main/project_info.yaml",
    },
   {"project_name": "sechenov",

      "base_dir": "/content/drive/MyDrive/uii/teamleads/Химяк Павел/Создание ИИ-системы для автоматизированной оценки рациона (Сеченовский Университет) гр.2/журналы встречь",

     "project_info_url": "https://github.com/NeuronsUII/Sechenov_gr2/blob/main/project_info.yaml"
  },
    {
    "project_name": "karate_do_groza",
    "base_dir": "/content/drive/MyDrive/uii/teamleads/Химяк Павел/Стажировка организация Ассоциация шотокан карате до Гроза  (новички)/журналы встречь",
    "project_info_url": "https://github.com/aiu-interns-karate-groza-newbies-ph/karate-do-groza-newbies/blob/main/project_info.yaml"
    }
]
    CFG_PROJECT_NAME  = "sechenov"
project_cfg = find_config_by_project_name(CFG_PROJECT_NAME, CFG)
api_key = os.getenv("GIT_API_KEY") # Вставьте ваш API ключ
project_info = load_yaml_from_private_github(project_cfg["project_info_url"], api_key)
project_cfg = always_merger.merge(project_info, project_cfg)
print(project_cfg)

