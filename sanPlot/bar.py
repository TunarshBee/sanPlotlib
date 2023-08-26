from matplotlib import pyplot as plt
import numpy as np

print(plt.style.available)

class Bar:
    def __init__(
        self,
        x_values,
        y_values,
        title: str = None,
        x_ttl: str = None,
        y_ttl: str = None,
        label: str = None,
        graphStyle: str = None,
        cmcStyle: bool = None,
        color: str = None,
        save: str = None,
        alpha: int = None,
        width: int = None,
        idxwidth: int = None,
    ):
        self.x_values = x_values
        self.y_values = y_values
        self.title = title
        self.x_ttl = x_ttl
        self.y_ttl = y_ttl
        self.label = label
        self.style = graphStyle
        self.cmcStyle = cmcStyle
        self.color = color
        self.save = save
        self.width = width
        self.alpha = alpha
        self.idxwidth = idxwidth

    def render(self):
        plt.style.use(self.style) if self.style else plt.style.use("seaborn")

        x_indexes = np.arange(len(self.x_values))
        plt.bar(
            x_indexes,
            self.y_values,
            color=self.color if self.color else None,
            alpha=self.alpha if self.alpha else None,
            label=self.label if self.label else None,
        )
        # if plt is more than one,
        # you must specify idxwidth if you are plotting multiple bar charts at once
        plt.bar(
            x_indexes(self.idxwidth),
            self.y_values,
            width=self.width,
            color=self.color,
            alpha=self.alpha,
            label=self.label,
        ) if self.idxwidth else " "
        plt.xticks(ticks=x_indexes, labels=self.x_values)
        plt.xlabel(self.x_ttl) if self.x_ttl else ""
        plt.ylabel(self.y_ttl) if self.y_ttl else ""
        plt.title(self.title) if self.title else ""
        plt.legend(loc="upper left") if self.label else ""
        plt.savefig(self.save) if self.save else ""
        plt.tight_layout()
        plt.show()


products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [1200, 1800, 900, 1500]
# Create a Bar instance and render the bar chart
bar_chart = Bar(products,sales,title='Sales Performance by Product',x_ttl='Products',y_ttl='Sales',color='teal',save='barchart.png')
bar_chart.render()