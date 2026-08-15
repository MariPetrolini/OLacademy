# Skill: diagramas de rede

Antes de criar ou alterar storyboard, SVG, TSX ou qualquer asset visual de uma aula, executar `npm run voice:release:check -- <pasta-da-aula>` e `npm run audio:provenance:check -- <pasta-da-aula>`. Bloquear se a liberação do texto falado ou a proveniência do áudio não estiver válida; antes disso, não gravar nem gerar assets.

Usar SVG ou componentes React, não imagens geradas, para topologias e fluxos técnicos. Dispositivos precisam de rótulos; enlaces, direção e estado devem ser inequívocos. Distinguir frame, packet e segmento. Não usar ícones de fornecedor sem necessidade/licença.
