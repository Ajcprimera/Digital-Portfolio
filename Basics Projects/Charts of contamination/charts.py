import matplotlib.pyplot as plt

def generate_bar_chart(labels, values): 
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Years')
    ax.set_ylabel('Global Emission')
    ax.set_title('')
    plt.show()
