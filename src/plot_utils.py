import os
import matplotlib.pyplot as plt

def save_fig(fig_id, chapter=2, tight_layout=True, fig_extension="png", resolution=300):
    """
    Сохраняет график строго в папку images/chapter{chapter}/ от корня проекта.
    """
    # 1. Определяем абсолютный путь к файлу src/plot_utils.py
    current_file = os.path.abspath(__file__)
    
    # 2. Находим корень проекта: 
    # src/plot_utils.py -> src/ -> mml-companion-notes/ (корень)
    project_root = os.path.dirname(os.path.dirname(current_file))
    
    # 3. Формируем путь до папки images
    output_dir = os.path.join(project_root, "images", f"chapter{chapter}")
    
    # 4. Создаем папку, если её нет
    os.makedirs(output_dir, exist_ok=True)
    
    # 5. Полный путь к файлу
    path = os.path.join(output_dir, f"{fig_id}.{fig_extension}")
    
    if tight_layout:
        plt.tight_layout()
        
    plt.savefig(path, format=fig_extension, dpi=resolution)