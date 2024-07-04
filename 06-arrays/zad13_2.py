import matplotlib.pyplot as plt

def create_bar_chart():
    # Data
    categories = ['Car', 'Public Transport', 'Bike', 'Foot']
    employees_count = [25, 19, 32, 7]

    # Plotting the bar chart
    plt.bar(categories, employees_count, color=['blue', 'orange', 'green', 'red'])
    
    # Adding title and labels
    plt.title('Employee Commuting Methods')
    plt.xlabel('Commute Method')
    plt.ylabel('Number of Employees')

    # Display the bar chart
    plt.show()

# Run the program
if __name__ == "__main__":
    create_bar_chart()