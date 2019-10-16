import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 应用参数
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

search_button=driver.find_element_by_id("com.android.settings:id/search")
print("放大镜的大小:",search_button.size)
print("放大镜的位置:",search_button.location)
print("包名:",driver.current_package)
print("界面名:",driver.current_activity)
# driver.swipe(100,2000,100,200)
# 从存储滑动到更多
# more_button=driver.find_element_by_xpath("//*[@text='更多']")
# dianchi_button=driver.find_element_by_xpath("//*[@text='电池']")
# driver.scroll(dianchi_button,more_button)
# 轻巧更多按钮
TouchAction(driver).tap(driver.find_element_by_xpath('//*[@text="更多"]')).perform()
# 在设置应用中启动到短信应用
# driver.start_activity("com.android.mms",".ui.ConversationList")
# 是设置程序置于后台5秒
# driver.background_app(5)
# time.sleep(3)
# 获取当前设备的分辨率
print("分辨率:",driver.get_window_size())
driver.get_screenshot_as_file("setting.png")
# 退出driver
driver.quit()