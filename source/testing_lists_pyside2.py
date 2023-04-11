from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QMessageBox
import sys


def show_list(items):
    # Create a QListWidget
    list_widget = QListWidget()

    # Add items to the list
    for item in items:
        list_item = QListWidgetItem(item)
        list_widget.addItem(list_item)

    # Show the message box with the list widget as its contents
    message_box = QMessageBox()
    message_box.setWindowTitle("Select an item")
    message_box.setIcon(QMessageBox.Question)
    message_box.setText("Please select an item:")
    message_box.setStandardButtons(QMessageBox.Cancel)

    message_box.setDefaultButton(QMessageBox.Cancel)
    message_box.setEscapeButton(QMessageBox.Cancel)
    message_box.addButton("OK", QMessageBox.AcceptRole)

    message_box.layout().addWidget(list_widget)

    result = message_box.exec_()

    # Return the index of the selected item
    if result == QMessageBox.AcceptRole:
        selected_item = list_widget.currentItem()
        selected_index = list_widget.row(selected_item)
        return selected_index
    else:
        return None


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Define the items list
    items = ["Item 1", "Item 2", "Item 3"]

    items = pt.

    # Call the show_list function
    selected_index = show_list(items)

    print(selected_index)

    # Print the selected index
    #if selected_index is not None:
    #    print(f"Selected index: {selected_index}")

    # Run the event loop
    sys.exit(app.exec_())
