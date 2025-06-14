import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    anchors.fill: parent
    color: "lightblue"

    Text{
        anchors.centerIn: parent
        text: backend.text
    }
}