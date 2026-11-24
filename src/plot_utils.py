import os
import matplotlib.pyplot as plt

def save_fig(fig_id, chapter=2, tight_layout=True, fig_extension="png", resolution=300):
    """
    Сохраняет текущую фигуру matplotlib в папку images/chapter{chapter}/{fig_id}.{ext}.
    
    Параметры:
        fig_id (str): имя файла без расширения.
        chapter (int): номер главы для организации папок.
        tight_layout (bool): применить plt.tight_layout() перед сохранением.
        fig_extension (str): расширение файла (png, pdf, svg).
        resolution (int): DPI изображения.
    """
    path = os.path.join("images", f"chapter{chapter}", f"{fig_id}.{fig_extension}")
    os.makedirs(os.path.dirname(path), exist_ok=True)  # Создаёт папку, если её нет
    
    if tight_layout:
        plt.tight_layout()
    
    plt.savefig(path, format=fig_extension, dpi=resolution)