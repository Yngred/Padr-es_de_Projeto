class VideoConverterFacade:
    def __init__(self):git add .

        self.loader = VideoLoader()
        self.format_converter = FormatConverter()
        self.quality_adjuster = QualityAdjuster()

    def convert_video(self, filename, format):
       
        video = self.loader.load(filename)
        video = self.format_converter.convert(video, format)
        video = self.quality_adjuster.adjust(video)
        return video

class VideoLoader:
    def load(self, filename):
        print(f"Carregando vídeo do arquivo {filename}")
        return "Vídeo carregado"

class FormatConverter:
    def convert(self, video, format):
        print(f"Convertendo vídeo para o formato {format}")
        return f"Vídeo convertido para {format}"

class QualityAdjuster:
    def adjust(self, video):
        print("Ajustando a qualidade do vídeo")
        return f"Qualidade ajustada do {video}"