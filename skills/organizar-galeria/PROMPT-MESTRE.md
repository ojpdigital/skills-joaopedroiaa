Você vai organizar a minha galeria olhando folhas de 16 miniaturas. Cada folha é uma imagem `folha-NNN.jpg` com 4x4 fotos numeradas de 1 a 16 (número amarelo no canto de cada miniatura).

Para cada folha que eu te passar, abra a imagem e, para cada número de 1 a 16 que tem foto:
1. Escolha UMA pasta desta lista (use exatamente estes nomes): pessoas, familia-e-amigos, viagem-e-paisagem, comida, animais, carros-e-objetos, prints-de-tela, documentos-e-texto, arte-e-memes, outros.
   - `prints-de-tela`: qualquer captura de tela de app, site, conversa ou documento no celular/computador.
   - Na dúvida entre duas, escolha a que ajuda a achar a foto depois.
2. Escreva 2 ou 3 tags curtas em português, minúsculas, sem acento, do que se vê (ex.: praia, casamento, gato, recibo).

Responda SOMENTE com JSON, sem texto em volta, neste formato (uma chave por folha):
{"folha-001": [{"n": 1, "pasta": "comida", "tags": ["pizza", "mesa"]}, {"n": 2, "pasta": "pessoas", "tags": ["retrato", "oculos"]}], "folha-002": [...]}

Regras: não invente número que não tem foto; não escreva nome de pessoa; não mexa nem renomeie nenhum arquivo (quem copia é o script, depois que eu confirmar a conta por pasta).
