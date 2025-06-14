import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import FluentUI 1.0

Rectangle {
    id: background
    anchors.fill: parent
    color: "#CBFCF0"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10  // 设置子元素之间的间距

        Rectangle{
            id: showtext
            Layout.fillWidth: true
            height: 50
            color: background.color
            Text {
                anchors.centerIn: parent
                font.pixelSize: 20
                text: backend.text
            }
        }

        FluButton{
            text:"按钮"
            Layout.alignment: Qt.AlignCenter
            implicitHeight: 80;
            implicitWidth: 80;
            font.pixelSize: 20
            background: Rectangle {
                radius: 15
            }
            onClicked: {
                backend.debug("qml Button clicked")
                console.log("qml print")
            }
        }
    }

}