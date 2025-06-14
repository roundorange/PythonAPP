import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts
import FluentUI 1.0

Window {
    visible: true
    width: 640
    height: 480
    title: "Hello QML "

    ColumnLayout {
        anchors.fill: parent
        spacing: 0  // 设置子元素之间的间距

        Rectangle{
            height: 80
            Layout.fillWidth: true
            Text {
                text: "Hello, World!"
                anchors.centerIn: parent
            }
        }
        FluButton{
            text:"Standard Button"
            onClicked: {

            }
        }
        FluToggleSwitch{
            text:"Text"
        }
    }


}