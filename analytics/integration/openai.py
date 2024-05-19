from openai import OpenAI

from analytics.models import Feedback
from users.models import UserModel


class OpenaiAPI():
    def __init__(self) -> None:
        self.client = OpenAI()

    def get_insights(self, user: UserModel, feedback: Feedback) -> str:
        user_characteristics = ', '.join([characteristic.name for characteristic in user.characteristics.all()])
        content = ''

        if user_characteristics:
            content += 'Sou {user_characteristics} e '

        content += feedback.content

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system", 
                    "content": "Você é um assistente especializado em diversidade, equidade, inclusão (DEI) e cultura organizacional. \
                        Forneça insights para que a empresa possa entender e definir plano de ação para melhor atender o feedback do colaborador\
                        visando criar um ambiente adaptado às necessidades deste e de outros colaboradores e, assim, transformar a empresa em o melhor lugar para trabalhar.\
                        A sua resposta deve começar com 'Os insights para este feedback é:' e após isso a sua resposta com links de sites que contenham esse conteúdo"
                },
                {
                    "role": "user",  
                    "content": content
                }
            ]
        )

        return '\n'.join([choice.message.content for choice in response.choices])
