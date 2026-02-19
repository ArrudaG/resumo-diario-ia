from google import genai
from src.config.settings import GEMINI_API_KEY

client = genai.Client(api_key = GEMINI_API_KEY)

def gerar_resumo(noticias):
    response = client.models.generate_content(

        model="gemini-2.5-flash",
        contents=(f"""Você é um analista financeiro que atua no mercado brasileiro
                    
                    Tarefa:
                    Produzir um resumo diário sobre a bolsa de valores baseado nas noticias fornecidas
                     
                    Objetivo:
                    Identificar possíveirs impactos diretos ou indiretos no mercado de ações brasileiro
                    
                    Instruções:
                    - Explique de forma clara e didática
                    - Evite jargões excessivamente técnicos
                    - Destaque riscos e oportunidades
                    - Caso necessário, explique brevemente conceitos importantes
                    
                    Formato de saída:
                    1. Visão geral do cenário
                    2. Principais impactos no mercado
                    3. Riscos potenciais
                    4. Oportunidades potenciais

                    Notícias:
                    {noticias}"""),
    )

    return response.text
