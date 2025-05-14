class FigureManager:
    def __init__(self):
        self.figures = {}

    def add_figure(self, name):
        def decorator(cls):
            self.figures[name] = cls
            return cls
        return decorator

    def get_figure(self, name):
        return self.figures.get(name)

class FigureCreator:
    def __init__(self, fm):
        self.fm = fm

    def create_figure(self, figure_type, params):
        fig_class = self.fm.get_figure(figure_type)
        if fig_class:
            return fig_class(*params)
        raise ValueError(f"Unknown figure type: {figure_type}")

class ProcessData:
    def __init__(self, fc: FigureCreator):
        self.fc = fc

    def process_data(self, data):
        return [self.fc.create_figure(fig_type, params) for fig_type, *params in data]
