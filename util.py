from PySide6.QtWidgets import QMessageBox


def make_message_box(
    title: str,
    text: str,
    icon: QMessageBox.Icon = None,
    buttons: QMessageBox.StandardButton = None,
) -> QMessageBox:
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)

    if icon:
        msg_box.setIcon(icon)

    if buttons:
        msg_box.setStandardButtons(buttons)

    msg_box.exec()

    return msg_box
