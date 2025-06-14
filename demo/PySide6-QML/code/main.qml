import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    anchors.fill: parent
    color: "#00A0D6"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0  // 设置子元素之间的间距

        Rectangle {
            Layout.fillWidth: true
            height: 50
            // radius: 5
            Text {
                anchors.centerIn: parent
                font.pixelSize: 20;
                text: backend.text
            }
            // color: "#A0A0A0"
        }
    }
}