
from openai import OpenAI

class AIInternshipMeetingReportGenerator:
    def __init__(self, api_key, model = "gpt-4o-mini"):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.system_prompt = '''
        Ты помощник, который помогает создавать отчеты о встречах по проектам.
      Описание заказчика: {client_description}"
      Описание Проекта : {project_description}
      Направление Проекта и возможные технологии: {technologies}
      Вот все  участники этого проекта {members}. Не все участники могут присутствовать на встече.
      Тебе нужно учитывать  кто из участников , кроме руководителя и помощьника присутствуют на встрече.

       Твоя задача — проанализировать распознанный текст и составить отчет о встрече с учетом выступлений каждого присутствующего участника.
        '''
        self.user_prompt = '''
    Дай подробный отчет о встрече , основываясь на распечатке встречи.
    Определи участников встречи.
Освети следующие разделы
- Общее впечатление от встречи:
- Что сделано:
- Проблемы и трудности:
- Задачи на неделю для всех и включая каждого присутствующего на встрече участника:
- проанализировать выступления каждого участника
Ниже представлен распечатка встречи:{document}
     '''
    def generate_prompt(self, project_cfg, document_content):
        system_prompt = self.system_prompt.format(
                    client_description=project_cfg["client_description"],
                    project_description=project_cfg["project_description"],
                    technologies=project_cfg["technologies"],
                    members=project_cfg["members"]
                )
        user_prompt = self.user_prompt.format(document=document_content)

        return system_prompt , user_prompt


    def generate_response(self, project_cfg, document_content):
        system_prompt, user_prompt = self.generate_prompt(project_cfg, document_content)

        chat_completion = self.client.chat.completions.create(
            messages=[
               {
                "role": "system",
                "content": system_prompt

               },
              {
                  "role": "user",
                  "content": user_prompt,
              }
           ],
            model=self.model
         )

        model_info = f"используемая модель: {self.model}"  + '\n'
        return model_info + chat_completion.choices[0].message.content



class AIInternshipMeetingTelegramReportGenerator:
    def __init__(self, api_key, model = "gpt-4o-mini"):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.system_prompt = '''
        Ты помощник, который помогает создавать отчеты о встречах по проектам.
      Описание заказчика: {client_description}"
      Описание Проекта : {project_description}
      Направление Проекта и возможные технологии: {technologies}
      Вот все  участники этого проекта {members}. Не все участники могут присутствовать на встече.
      Тебе нужно учитывать  кто из участников , кроме руководителя и помощьника присутствуют на встрече.

       Твоя задача — проанализировать распознанный текст и составить отчет о встрече с учетом выступлений каждого присутствующего участника.
        '''
        self.user_prompt = '''
    Дай подробный отчет о встрече , основываясь на распечатке встречи.
    Определи участников встречи.
Освети следующие разделы
- Общее впечатление от встречи:
- Что сделано:
- Проблемы и трудности:
- Задачи на неделю для всех и включая каждого присутствующего на встрече участника:
- проанализировать выступления каждого участника
Ниже представлен распечатка встречи:{document}
     '''
    def generate_prompt(self, project_cfg, document_content):
        system_prompt = self.system_prompt.format(
                    client_description=project_cfg["client_description"],
                    project_description=project_cfg["project_description"],
                    technologies=project_cfg["technologies"],
                    members=project_cfg["members"]
                )
        user_prompt = self.user_prompt.format(document=document_content)

        return system_prompt , user_prompt


    def generate_response(self, project_cfg, document_content):
        system_prompt, user_prompt = self.generate_prompt(project_cfg, document_content)

        chat_completion = self.client.chat.completions.create(
            messages=[
               {
                "role": "system",
                "content": system_prompt

               },
              {
                  "role": "user",
                  "content": user_prompt,
              }
           ],
            model=self.model
         )

        model_info = f"используемая модель: {self.model}"  + '\n'
        return model_info + chat_completion.choices[0].message.content

