import QtQuick

Rectangle {
    width: 360
    height: 360
    Text
    {
        anchors.centerIn: parent
        text: "Button"
    }
    MouseArea
    {
        anchors.fill: parent
        onClicked: {
            Qt.quit();
        }
    }
}