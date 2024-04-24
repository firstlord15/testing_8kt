appium_server_url = 'http://localhost:4723'

shorts = '(//android.widget.ImageView[@resource-id="com.google.android.youtube:id/image"])[2]'
home = '(//android.widget.ImageView[@resource-id="com.google.android.youtube:id/image"])[1]'

el1_uiselector = 'new UiSelector().className("android.widget.ImageView").instance(1)'
el2_uiselector = 'new UiSelector().className("android.widget.ImageView").instance(11)'
main_screen_view = 'new UiSelector().resourceId("com.google.android.youtube:id/watch_player")'
navigationBar = 'new UiSelector().resourceId("android:id/navigationBarBackground")'

share = 'new UiSelector().description("Поделиться")'