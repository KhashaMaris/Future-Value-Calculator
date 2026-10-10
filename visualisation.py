import matplotlib.pyplot as plt

def plot_investments(ax,years,values,label):
    ax.plot(years, values, marker="o", label=label)
    
    for year, value in zip(years,values):
        ax.annotate(
            f"${value:,.2f}",
            xy=(year,value),
            textcoords="offset points",
            xytext=(0,8),
            ha="center"
        )
        
def show_chart(years,recurring_values,lumpsum_values,monthly_values):
    fig, ax = plt.subplots(figsize=(11,6))
    
    plot_investments(ax,years,recurring_values,"Yearly contributions only")
    
    plot_investments(ax,years,lumpsum_values,"Initial lump sum + yearly contributions")
    
    plot_investments(ax,years,monthly_values,"Initial lump sum + monthly contributions")
    
    ax.set_title("Investment Growth Over Time")
    ax.set_xlabel("Years")
    ax.set_ylabel("Future Value")
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.tight_layout()
    plt.show()