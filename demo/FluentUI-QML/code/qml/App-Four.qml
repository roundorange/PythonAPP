import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import FluentUI 1.0

Rectangle {
    id: qmlbackground
    anchors.fill: parent
    // anchors.bottomMargin : 10
    color: "#CBFCF0"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0  // 设置子元素之间的间距

        // Rectangle{
        //     id: showtext
        //     Layout.fillWidth: true
        //     height: 50
        //     color: qmlbackground.color
        //     Text {
        //         anchors.centerIn: parent
        //         font.pixelSize: 20
        //         text: "重心计算器"
        //     }
        // }
        // 页面内容区域
        SwipeView {
            id: swipeView
            Layout.fillWidth: true
            Layout.fillHeight: true
            interactive: true  // 禁用滑动切换
            currentIndex: tabBar.currentIndex

            Item {
                PageA{
                    id: people
                }
            }
            Item {
                PageB{
                    id: goods
                }
            }
            Item {
                PageC{
                    id: result
                }
            }
            Item {
                PageD{
                    id: info
                }
            }
        }
        RowLayout {
            Layout.fillWidth: true
            anchors.bottomMargin : 0
            spacing: 0  // 设置子元素之间的间距

            Button {
                text: "页面一"
                id: control
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                // anchors.fill: parent
                // Layout.alignment: Qt.AlignCenter
                font.pixelSize: 20
                background: Rectangle {
                    radius: 10
                    height: 50
                    color: "#0066B4"
                }
                contentItem: Text {
                    text: parent.text
                    font.pixelSize: 16
                    opacity: enabled ? 1.0 : 0.3
                    color: "#FFFFFF"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
                onClicked: {
                    console.log("QML Button is clicked")
                    swipeView.currentIndex = 0
                }
            }
            Button {
                text: "页面二"
                id: control2
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                // anchors.fill: parent
                // Layout.alignment: Qt.AlignCenter
                font.pixelSize: 20
                background: Rectangle {
                    radius: 10
                    height: 50
                    color: "#0066B4"
                }
                contentItem: Text {
                    text: parent.text
                    font.pixelSize: 16
                    opacity: enabled ? 1.0 : 0.3
                    color: "#FFFFFF"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
                onClicked: {
                    console.log("QML Button is clicked")
                    swipeView.currentIndex = 1
                }
            }
            Button {
                text: "页面三"
                id: control3
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                // anchors.fill: parent
                // Layout.alignment: Qt.AlignCenter
                font.pixelSize: 20
                background: Rectangle {
                    radius: 10
                    height: 50
                    color: "#0066B4"
                }
                contentItem: Text {
                    text: parent.text
                    font.pixelSize: 16
                    opacity: enabled ? 1.0 : 0.3
                    color: "#FFFFFF"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
                onClicked: {
                    console.log("QML Button is clicked")
                    swipeView.currentIndex = 2
                }
            }
            Button {
                text: "页面四"
                id: control4
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                // anchors.fill: parent
                // Layout.alignment: Qt.AlignCenter
                font.pixelSize: 20
                background: Rectangle {
                    radius: 10
                    height: 50
                    color: "#0066B4"
                }
                contentItem: Text {
                    text: parent.text
                    font.pixelSize: 16
                    opacity: enabled ? 1.0 : 0.3
                    color: "#FFFFFF"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    elide: Text.ElideRight
                }
                onClicked: {
                    console.log("QML Button is clicked")
                    swipeView.currentIndex = 3
                }
            }
        }
        // 自定义高度的TabBar
        TabBar {
            id: tabBar
            Layout.minimumHeight: 50
            Layout.maximumHeight: 50
            Layout.fillWidth: true
            Layout.fillHeight: true
            currentIndex: swipeView.currentIndex

            // 自定义样式
            background: Rectangle {
                color: qmlbackground.color
            }

            // 添加选项卡按钮
            TabButton {
                anchors.top: parent.top
                height: parent.height
                Layout.fillHeight: true
                text: "APP"
                background: Rectangle {
                    color: parent.checked ? "lightblue" : "#9E9E9E"
                    radius: 5
                }
                contentItem: Text {
                    text: parent.text
                    color: "red"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
            // 添加选项卡按钮
            TabButton {
                anchors.top: parent.top
                height: parent.height
                Layout.fillHeight: true
                text: "控制"
                background: Rectangle {
                    color: parent.checked ? "lightgreen" : "#9E9E9E"
                    radius: 5
                }
                contentItem: Text {
                    text: parent.text
                    color: "red"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
            // 添加选项卡按钮
            TabButton {
                anchors.top: parent.top
                height: parent.height
                Layout.fillHeight: true
                text: "消息"
                background: Rectangle {
                    color: parent.checked ? "lightpink" : "#9E9E9E"
                    radius: 5
                }
                contentItem: Text {
                    text: parent.text
                    color: "red"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
            // 添加选项卡按钮
            TabButton {
                anchors.top: parent.top
                height: parent.height
                Layout.fillHeight: true
                text: "关于"
                background: Rectangle {
                    color: parent.checked ? "#c9ace5" : "#9E9E9E"
                    radius: 5
                }
                contentItem: Text {
                    text: parent.text
                    color: "red"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
        }
    }
}