Xpath = {
    "Login": "(//androidx.compose.ui.platform.ComposeView[@resource-id=\"com.ajaxsystems:id/compose_view\"])"
             "[1]/android.view.View/android.view.View/android.widget.Button",
    "emailForm": "//android.widget.EditText[@resource-id=\"com.ajaxsystems:id/authLoginEmail\"]",
    "passwordForm": "//android.widget.EditText[@resource-id=\"com.ajaxsystems:id/authLoginPassword\"]",
    "loginButton": "(//androidx.compose.ui.platform.ComposeView[@resource-id=\"com.ajaxsystems:id/compose_view\"])"
                   "[4]/android.view.View/android.view.View/android.widget.Button",
    "wrongLoginData": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/snackbar_text\"]",
    "addHubButton": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/text\"]",
    "sidebarDrawer": "//android.widget.ImageView[@resource-id=\"com.ajaxsystems:id/menuDrawer\"]"

}

SideBar = {
    "Settings": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/title\" and @text=\"App Settings\"]",
    "Help": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/title\" and @text=\"Help\"]",
    "Report": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/title\" and @text=\"Report a Problem\"]",
    "AddHub": "(//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/text\"])[2]",
    "Terms": "//android.widget.TextView[@resource-id=\"com.ajaxsystems:id/documentation_text\"]"
}
