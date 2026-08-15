# PowerPoint no pipeline

O arquivo de entrada deve ser `.pptx`. O comando `slides:ingest`:
1. copia o original para `source/original/deck.pptx`;
2. usa LibreOffice headless para gerar PDF temporário;
3. usa Poppler (`pdftoppm`) para rasterizar cada slide em PNG;
4. extrai mídias internas de `ppt/media/` para `source/extracted-media/`;
5. escreve `source/slides-manifest.json`.

Os PNGs são obrigatórios no vídeo. O Remotion pode adicionar camadas sobre eles.
