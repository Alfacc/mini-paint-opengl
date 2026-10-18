from PIL import Image

# Arquivo para gerenciar a logica de exportar a matriz de pixels do canvas em imagem
def Exportar(canvas, caminho_arquivo="desenho.png"):
  #astype para Image não reportar problemas sobre o tipo
  imagem = Image.fromarray(canvas.matriz_pixels.astype('uint8'), mode="RGB")

  imagem.save(caminho_arquivo)
  print(f"Imagem foi salva com sucesso: {caminho_arquivo}")