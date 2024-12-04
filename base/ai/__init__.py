
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
      Тебе нужно учитывать  кто из участников , кроме руководителя и помощника присутствуют на встрече.

       Твоя задача — проанализировать распознанный текст и составить отчет о встрече с учетом выступлений каждого присутствующего участника.
        '''
        self.user_prompt = '''
    На основе следующего подробного отчета о встрече составь краткий мини-отчет по заданной структуре.
    
Структура:

Проект: Укажи название проекта и его краткое описание (если имеется).
Встреча: Укажи номер встречи и дату проведения.
1. Общее впечатление: Опиши общий ход встречи, например, была ли активной, кто участвовал (например, заказчик, команда).
2. Как идет процесс по проекту (что сделано, какие проблемы): Опиши ключевые моменты прогресса, проблемы, задачи и выводы.
3. Объем базы данных: Оцени объем базы данных. Варианты: нет, маленькая, средняя, достаточная.
4. Сколько студентов выполнили задачи из поставленных (укажи в формате X/Y колличество/общее колличество участников).
5. Заполнены ли таблицы, занесен ли отчет в Трелло доску: Укажи, да или нет.
6. Все ли отчеты сданы стажерами (укажи в формате X/Y)
7. Сколько пассивных студентов: (укажи в формате X/Y)
8. Сколько средних студентов: (укажи в формате X/Y)
9. Сколько активных студентов:(укажи в формате X/Y)
10. Сколько неадекватных студентов: Укажи количество (если таких нет, напиши '-').
11. Укладываемся ли в срок по проекту: Да или нет.
12. Какие есть риски, из-за которых мы можем не уложиться в срок по проекту: Опиши, если есть.
13. Связь с заказчиком: Опиши, как осуществляется связь (например, общая группа в Telegram, email).
Подробный отчет:{document}

Мини-отчет:
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

